from .mixin import SerializableMixin


class Config(SerializableMixin):
    def serialize(self) -> dict:
        data: dict = self.__dict__.copy()
        return {}

    @classmethod
    def deserialize(self, serialized: dict) -> "SerializableMixin":
        pass