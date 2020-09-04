import pytest
from aescbc.cipher import Cipher


class TestCipher:
    def test_init(self):
        assert (
            len(Cipher().key) == 32
        ), "32 chars as hexdecimal representation, thats 2 chars per byte."

    @pytest.mark.parametrize(
        "encrypted, expected",
        [
            (
                "vgohYh7cvK6ilLEfvUv14bH5ieoCd9kIhepesMc7t4S/t39Tqua39WwhrYH5XZANJpZSPFd1At5iYQTjc7fiqg==",
                "東京都新宿区西新宿2-8-1",
            ),
            (
                "k4Cn5y4hHkmaGEkPnPm7fd1U1fErpT/HgPeEdf3rzk7fgUuY758CLzy4RodtKoGdmZC88omyW3rsHzPJrJS8iw==",
                "東京都新宿区西新宿2-8-1",
            ),
            (
                "pN3ufw37XGb64bc8TZICXmpUW9ngldA8hwOpaMbQLrux7IEnW+XpQ0AuwkJp/qMCcHr6//+fXcxvTB9u4My3nQ==",
                "東京都新宿区西新宿2-8-1",
            ),
            (
                "hlWzzaiGDIZU3XtmVxfcp5AF2p5vgu2Gh1z3XAArGXCqyOrzPvi0LNdcH1yGoRoNgj+I4DVCh/E7lQYHb5UlSw==",
                "東京都新宿区歌舞伎町1-4-1",
            ),
            (
                "1Z6UuSyCL/ZX2K7x/aA1ABYmsnL9/Rf9OfNKJMrXS6UxMtH9qLUHEh10EkZj1Xga0kpBZM211X0ehdyK26lBhQ==",
                "東京都新宿区歌舞伎町1-4-1",
            ),
            (
                "vN/Q2bXrpiqUB2JmwiEf0EnsRCCKeUvIYLtOfUDMOzTh/X6lQ8PxX2i6GChfI7tb8e+BXk9IfbAlfb8AgUexGA==",
                "東京都新宿区歌舞伎町1-4-1",
            ),
        ],
    )
    def test_decrypt(self, encrypted, expected):
        assert Cipher().decrypt(encrypted) == expected
