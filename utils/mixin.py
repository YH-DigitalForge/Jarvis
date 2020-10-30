from abc import abstractmethod, ABCMeta
from typing import Any
from .type_hints import JSON


class Serializable(metaclass=ABCMeta):
    """
    Make an instance of class can be serialized as bytes object.
    """

    @abstractmethod
    def serialize(self) -> Any:
        ...

    @classmethod
    @abstractmethod
    def deserialize(cls, serialized: Any) -> "Serializable":
        ...


class JSONSerializable(Serializable):
    """
    Make an instance of class can be serialized as JSON object.
    """

    @abstractmethod
    def serialize(self) -> JSON:
        ...

    @classmethod
    @abstractmethod
    def deserialize(cls, serialized: JSON) -> "JSONSerializable":
        ...

class BytesSerializable(Serializable):
    """
    Make an instance of class can be serialized as bytes object.
    """

    @abstractmethod
    def serialize(self) -> bytes:
        ...

    @classmethod
    @abstractmethod
    def deserialize(cls, serialized: bytes) -> "BytesSerializable":
        ...