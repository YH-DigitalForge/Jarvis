from abc import abstractmethod, ABCMeta


class SerializableMixin(metaclass=ABCMeta):
    """
    Make an instance of class can be serialized as JSON object.
    """

    @abstractmethod
    def serialize(self) -> dict:
        ...

    @classmethod
    @abstractmethod
    def deserialize(self, serialized: dict) -> "SerializableMixin":
        ...
