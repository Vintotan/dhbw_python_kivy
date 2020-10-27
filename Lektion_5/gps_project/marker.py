from locationpopupmenu import LocationPopupMenu
from kivy.garden.mapview import MapMarkerPopup


class Marker(MapMarkerPopup):
    source = "marker.png"  # Klassenvariable der Klasse Marker; jedes Objet kann auf die Klassenvariable "source" zurückgreifen
    market_data = []

    # Definieren das Anklicken eines Markers
    def on_release(self):
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.8, .9]
        menu.open()
