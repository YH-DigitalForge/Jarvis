"""
Kakao Voice Recognition & Synthesis API Wrapper
---
@author Lapis0875
@copyright 2020
"""
from typing import Optional, Any, Union, Dict, Literal
import aiofile
import aiohttp

JSON = Dict[str, Any]
FORMAT = Literal["json", "text", "bytes"]


class KakaoVoice:
    """
    Kakao REST API-Voice Wrapper.
    """

    def __init__(self, key: str):
        self.key = key
        self.kakao_url = "https://kakaoi-newtone-openapi.kakao.com/"

    async def _post(self, url: str, data: Union[bytes, str], *, headers: JSON = None, resultFormat: FORMAT) \
            -> [JSON, str, bytes]:
        """Post request to Kakao API.

        Parameters
        -----------
        url: str
            The sub url of Kakao API. ex) v1/recognize
        data: Union[bytes, str]
            HTTP Request body.
        * (below is keyword-only arguments)
        headers: JSON (Dict[str, Any])
            HTTP Request headers.
        resultFormat: FORMAT (Literal["json", "text", "bytes"])
            FORMAT Literal to define result format.

        Raises
        -------
        TypeError
            Invalid resultFormat value.

        """
        async with aiohttp.request(
                method="post",
                url=self.kakao_url + url,
                headers=headers,
                data=data
        ) as response:
            if resultFormat == "json":
                return await response.json(encoding="utf-8")
            elif resultFormat == "text":
                return await response.text(encoding="utf-8")
            elif resultFormat == "bytes":
                return await response.read()
            else:
                raise TypeError("Response only can be processed to json/text/bytes.")

    async def recognize(self, data: bytes) -> str:
        res = await self._post(
            "v1/recognize",
            data,
            headers={
                "Content-Type": "application/octet-stream",
                "Authorization": f"KakaoAK {self.key}",
                "Transfer-Encoding": "chunked"
            },
            resultFormat="text"
        )

        print(res)

    async def chunkedRecognize(self, data: bytes) -> str:

        headers = {
        }
        res = await self._post(
            "v1/recognize",
            data,
            headers={
                "Content-Type": "application/octet-stream",
                "Authorization": f"KakaoAK {self.key}",
                "Transfer-Encoding": "chunked"
            },
            resultFormat="json"
        )

        print(res)

    async def synthesize(self, content: str, filename: str):
        """
        Synthesize voice using given xml content.

        Parameters
        -----------
        content: str
            The coroutine to register as the local error handler.
        filename: str
            A name of file to store synthesized audio.

        Raises
        -------
        TypeError
            The coroutine passed is not actually a coroutine.
        """
        if not isinstance(content, str):
            raise TypeError("content must be str object containing xml file content!")

        res = await self._post(
            "v1/synthesize",
            content,
            headers={
                "Content-Type": "application/xml",
                "Authorization": f"KakaoAK {self.key}"
            },
            resultFormat="bytes"
        )
        async with aiofile.AIOFile(filename=filename, mode="wb") as resultFile:
            await resultFile.write(res)
