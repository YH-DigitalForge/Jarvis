from __future__ import annotations
from typing import Any, Optional
from .mixin import JSONSerializable
from .type_hints import JSON


class Field:
    def __init__(self, value: Any) -> None:
        self._value: Any = value
    
    @property
    def value(self) -> Any:
        return self._value
    
    @value.setter
    def value(self, new) -> Any:
        self._value = new
    
    def __repr__(self) -> str:
        return "Field(value={})".format(self._value)
    
    def __str__(self) -> str:
        return self.__repr__()
    

class Config(JSONSerializable):
    """
    Config object which stores values using keyword arguments.
    
    
    """
    def __init__(self, **attrs) -> None:
        for key, value in attrs.items():
            setattr(self, '_' + key, value)
            setattr(
                self,
                key,
                Field(value)
            )
        print(self.__dict__)

    def serialize(self) -> JSON:
        return {key[1:]: value for key, value in self.__dict__.items()}

    @classmethod
    def deserialize(cls, serialized: JSON) -> "Config":
        return cls(**serialized)

    def get(self, key: str) -> Optional[Any]:
        return getattr(self, '_' + key, None)

    def set(self, key: str, value: Any) -> None:
        setattr(self, '_' + key, value)
        setattr(
            self,
            key,
            Field(value)
        )
