import base64
from abc import abstractclassmethod, ABCMeta


class EnAndDecode(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def decode():
        pass

    @abstractclassmethod
    def encode():
        pass


class Base64(EnAndDecode):
    def __init__(self) -> None:
        super().__init__()

    def encode(string) -> str:
        base64_bytes = string.encode("utf-8")
        answer = base64.b64encode(base64_bytes)
        return answer.decode("utf-8")

    def decode(string) -> str:
        base64_bytes = string.encode("utf-8")
        answer = base64.b64decode(base64_bytes)
        return answer.decode("utf-8")
