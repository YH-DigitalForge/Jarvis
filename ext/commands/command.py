"""
Jarvis Command module.
"""
import asyncio
from functools import wraps
import inspect
from typing import Callable, Coroutine, Optional, Any, ClassVar, Tuple, List, Dict

CoroutineFunction = Callable[..., Coroutine]
Function = Callable[..., Any]
Decorator = Callable[[Function], Any]
Args = List[Any]
Kwargs = Dict[str, Any]


class Command:
    """
    Base command class.
    """

    # Command Callback Data
    _callback: CoroutineFunction
    _callback_spec: inspect.FullArgSpec
    _typings: Dict[str, str]

    def __init__(self, callback: CoroutineFunction, *, name: Optional[str] = None,
                 error_handler: Optional[CoroutineFunction] = None) -> None:
        if not asyncio.iscoroutinefunction(callback):
            raise TypeError("Command callback must be a coroutine function")
        self._callback = callback
        self.name = name if name is not None else callback.__name__
        if not isinstance(self.name, str):
            raise TypeError("Name of a command must be a coroutine function")
        self.error_handler = error_handler

    @property
    def callback(self) -> CoroutineFunction:
        return self._callback

    @callback.setter
    def callback(self, callback: CoroutineFunction):
        if not asyncio.iscoroutinefunction(callback):
            raise TypeError("Command callback must be a coroutine function")
        callback_argspec = inspect.getfullargspec(callback)

        self._callback = callback

    def onError(self, coro: CoroutineFunction) -> CoroutineFunction:
        """A decorator that registers a coroutine as a local error handler.

        Parameters
        -----------
        coro: coroutine
            The coroutine to register as the local error handler.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine.
        """
        if not asyncio.iscoroutinefunction(coro):
            raise TypeError("Command error handler must be a coroutine function")

        # Code inspection
        argspec = inspect.getfullargspec(coro)
        if argspec.varargs is not None:
            pass
        elif len(argspec.args) != 2:
            # error_handler(command, error)
            raise AttributeError("Error handler must have two arguments : command object, error object")
        elif "command" not in argspec.varkw or "error" not in argspec.varkw:
            raise AttributeError("Error handler lacks keyword arguments : it must receive 'command' and 'error'")
        self.error_handler = coro
        return coro

    async def invoke(self, *args, **kwargs) -> Any:
        """
        Invoke self.task and return result.
        :param args: arguments to pass to self.task
        :param kwargs: keyword arguments to pass to self.task
        """
        try:
            return await self._callback(*args, **kwargs)
        except Exception as e:
            await self.error_handler(e)
            return None


def command(*, name: Optional[str] = None, error_handler: Optional[CoroutineFunction] = None) \
        -> Callable[[CoroutineFunction], Command]:
    def wrapper(task: CoroutineFunction) -> Command:
        cmd = Command(task, name=name, error_handler=error_handler)
        return cmd

    return wrapper
