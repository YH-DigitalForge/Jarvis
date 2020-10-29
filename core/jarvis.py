from typing import NoReturn, Any, Dict, Optional
from aiofile import AIOFile
import json
from chronous import BaseArchitecture, BaseEvent
import logging

from .dialogFormatter import DialogFormatter
from .jarvis_events import SetupEvent, InitEvent, CloseEvent, VoiceEvent
from .KakaoVoice import KakaoVoice

logger = logging.getLogger("jarvis.core")


class Jarvis(BaseArchitecture):
    """
    Jarvis Class
    """

    def __init__(self, config_dir: str) -> None:
        """
        Initialize Jarvis instance.

        Parameters
        -----------
        config_dir: str
            A str object containing path of config file.
        """
        super(Jarvis, self).__init__(name="Jarvis")
        self.config_dir: str = config_dir
        self.config: Dict[str, Any] = {}
        self.KakaoClient: Optional[KakaoVoice] = None
        self.register_event(SetupEvent())
        self.register_event(InitEvent())
        self.register_event(CloseEvent())
        self.register_event(VoiceEvent())
        self.dialogFormatter = DialogFormatter("%")

    async def process(self) -> NoReturn:
        """
        Jarvis process.

        Raises
        -------
        Exception
            Any exception raised during process loop can be raised.
        """
        # Setup Jarvis
        await self.setup()
        # Initialize Jarvis
        await self.init()
        # Run main process
        await self.main()
        # Close process
        await self.close()

    async def setup(self) -> NoReturn:
        """
        Jarvis Setup Phase

        In this phase, Jarvis loads several config files in its directory.

        Raises
        -------
        Exception:
            Any exception raised during process loop can be raised.
        """
        async with AIOFile(self.config_dir, "rt") as afp:
            self.config: Dict[str, Any] = json.loads(await afp.read())
        await self.dispatch("jarvis.phase.setup")

    async def init(self) -> NoReturn:
        """
        Jarvis Initialization Phase

        Raises
        -------
        Exception:
            Any exception raised during process loop can be raised.
        """
        self.KakaoClient = KakaoVoice(self.config["api"]["kakao"]["key"])
        await self.dispatch("jarvis.phase.init")

    async def main(self) -> NoReturn:
        """
        Jarvis Main Loop

        Raises
        -------
        Exception:
            Any exception raised during process loop can be raised.
        """
        while True:
            """
            Main Process Loop
            """
            async with AIOFile(filename="./resource/dialog/error/command_not_found.xml", mode="rt", encoding="utf-8") as dialogFile:
                dialog: str = await dialogFile.read()
                print(dialog)
                await self.KakaoClient.synthesize(
                    content=self.dialogFormatter.format(
                        dialog,
                        voice_type="WOMMAN_READ_CALM",
                        command="오늘 날씨 알려줘"
                    ),
                    filename="./test/result.wav"
                )
            async with AIOFile(filename="./test/result.wav", mode="rb") as voiceFile:
                data = await voiceFile.read()
                await self.dispatch("jarvis.voice", data=data)

            return

    async def close(self) -> NoReturn:
        """
        Jarvis Close Phase

        Raises
        -------
        Exception:
            Any exception raised during process loop can be raised.
        """
        await self.dispatch("jarvis.phase.close")


jarvis_instance: Jarvis = Jarvis(config_dir="./config.json")
