from chronous.events import EventContext
from core import jarvis_instance


@jarvis_instance.listen("jarvis.phase.setup")
async def onSetup(ec: EventContext):
    print("PhaseEvent.{0}".format(ec.event.name))


@jarvis_instance.listen("jarvis.phase.init")
async def onSetup(ec: EventContext):
    print("PhaseEvent.{0}".format(ec.event.name))


@jarvis_instance.listen("jarvis.phase.close")
async def onSetup(ec: EventContext):
    print("PhaseEvent.{0}".format(ec.event.name))


@jarvis_instance.listen("jarvis.voice")
async def onSetup(ec: EventContext, data: bytes):
    print("JarvisEvent.{0}".format(ec.event.name))
    recognized = await jarvis_instance.KakaoClient.recognize(
        data=data
    )
    print(recognized)

jarvis_instance.run()
