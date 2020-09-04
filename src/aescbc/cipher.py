import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Padding
from dataclasses import dataclass, field


@dataclass
class Cipher:
    key: bytes = field(init=False)

    def __post_init__(self):
        key = "secret_key"
        self.key = (
            hashlib.md5(key.encode("utf-8"))
            .hexdigest()
            .encode("utf-8")
        )

    def encrypt(self, raw: str) -> str:
        iv = Random.get_random_bytes(AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        data = Padding.pad(raw.encode("utf-8"), AES.block_size)
        return base64.b64encode(iv + aes.encrypt(data)).decode("utf-8")

    def decrypt(self, encrypted: str) -> str:
        enc = base64.b64decode(encrypted.encode("utf-8"))
        iv = enc[: AES.block_size]
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        data = Padding.unpad(aes.decrypt(enc[AES.block_size:]), AES.block_size)
        return data.decode("utf-8")
