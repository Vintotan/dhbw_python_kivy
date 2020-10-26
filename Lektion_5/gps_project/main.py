from kivymd.app import MDApp
from map_view import FarmersMapView
import sqlite3


class MainApp(MDApp):
    connection = None
    cursor = None

    # Initialisiert die GPS-Funktion
    def on_start(self):

        # Database verbinden
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()


if __name__ == "__main__":
    MainApp().run()

