from ext.commands import command


@command(name="Hello")
async def cmdHello():
    print("Hello!")


@cmdHello.onError
async def errHello():
    print("Something bad happened :(")
