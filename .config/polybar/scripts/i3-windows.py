#!/usr/bin/env python3
from i3ipc.aio import Connection
from i3ipc import Event

import asyncio
import sys

LENGTH_LIMIT = 40

async def main():
    i3 = await Connection().connect()

    def on_window_focus(i3, e):
        data = e.ipc_data["container"]["name"]
        if len(data) > LENGTH_LIMIT:
            data = data[:LENGTH_LIMIT-3] + "..."
        print(data)
        sys.stdout.flush()
        
    i3.on(Event.WINDOW_FOCUS, on_window_focus)
    i3.on(Event.WINDOW_TITLE, on_window_focus)
    await i3.main()

asyncio.run(main())
