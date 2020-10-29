# Jarvis

Jarvis is a voice assistant designed for IOT hub on raspberry pi.

## Features

Jarvis is based on event driven architecture, so it registers and dispatches its events to listeners.
This makes Jarvis easy to be extended and modularized.

### 1. Jarvis - Event
```python
from chronous.events import EventContext
from core import jarvis_instance


@jarvis_instance.listen("jarvis.phase.setup")
async def onSetup(ec: EventContext):
    print("PhaseEvent.{0}".format(ec.event.name))


@jarvis_instance.listen("jarvis.phase.init")
async def onSetup(ec: EventContext):
    print("PhaseEvent.{0}".format(ec.event.name))

jarvis_instance.run()
```
Jarvis can register listeners into its instance. Developers can easily extend Jarvis's features by simply adding more listeners.

### 2. Jarvis - Commands
```python
from ext.commands import command


@command(name="Hello")
async def cmdHello():
    print("Hello!")


@cmdHello.onError
async def errHello():
    print("Something bad happened :(")
```
Jarvis supports command system. Command system helps developers to easily define voice commands and extend them.

### 3. Jarvis - Devices
```python
from ext.devices import Device
```
Jarvis supports device wrappers. These device wrappers helps developers to easily control devices connected on Jarvis.