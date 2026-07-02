#!/usr/bin/env python3

from .atservice import AsyncATService

from textual.app import App
from textual.widgets import Footer, Header



# call_command("Random", CMD_RANDOM(mode=CMD_RANDOM.Mode.NO_UPDATE_SEED))


class SecureCoreApp(App):

    def __init__(self, atservice: AsyncATService):
        super().__init__()
        self._atservice = atservice

    def compose(self):
        """Create child widgets for the app."""
        yield Header()
        yield Footer()


if __name__ == "__main__":
    atservice = AsyncATService()
    app = SecureCoreApp(atservice=atservice)
    app.run()
