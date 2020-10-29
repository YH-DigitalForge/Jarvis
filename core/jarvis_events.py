from typing import NoReturn

from chronous import BaseEvent
from chronous.events import EventContext


class JarvisEvent(BaseEvent):
    """
    Base class of Jarvis Events (Phase, Task, Voice, Devices, ...)
    """

    def __init__(self, name: str):
        super(JarvisEvent, self).__init__(name=f"jarvis.{name}")

    @staticmethod
    def listener(ec: EventContext, *args, **kwargs):
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


class PhaseEvent(JarvisEvent):
    """
    Base class of Jarvis Phase Events (Init, Close, ...).
    """

    def __init__(self, name: str):
        super(PhaseEvent, self).__init__(name=f"phase.{name}")

    @staticmethod
    def listener(ec: EventContext, *args, **kwargs):
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


class SetupEvent(PhaseEvent):
    """
    Jarvis Setup event
    """
    def __init__(self) -> None:
        super(SetupEvent, self).__init__(name="setup")

    @staticmethod
    def listener(ec: EventContext) -> NoReturn:
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


class InitEvent(PhaseEvent):
    """
    Jarvis Initialization event
    """
    def __init__(self) -> None:
        super(InitEvent, self).__init__(name="init")

    @staticmethod
    def listener(ec: EventContext) -> NoReturn:
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


class CloseEvent(PhaseEvent):
    """
    Jarvis Close event
    """
    def __init__(self) -> None:
        super(CloseEvent, self).__init__(name="close")

    @staticmethod
    def listener(ec: EventContext) -> NoReturn:
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


class VoiceEvent(JarvisEvent):
    """
    Jarvis Voice event
    """
    def __init__(self) -> None:
        super(VoiceEvent, self).__init__(name="voice")

    @staticmethod
    def listener(ec: EventContext, data: bytes) -> NoReturn:
        """Base listener structure

        Parameters
        -----------
        ec: EventContext object containing Event information.
            The coroutine to register as the local error handler.
        data: bytes
             bytes object containing voice audio data.

        Raises
        -------
        Exception
            An exception or error occured during executing listener.
        """


