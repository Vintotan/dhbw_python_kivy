from kivy.garden.mapview import MapView
from kivy.clock import Clock 
from kivy.app import App 
from marker import Marker


class FarmersMapView(MapView):
    get_markets_timer = None
    market_names = []

    # Karte initiieren bzw. eine Exception gesetzt (falls Werte nicht vorhanden)
    def start_get_markets(self):
        # Exception-Handling (Python)
        try: 
            self.get_markets_timer.cancel()
        except:
            pass

        self.get_markets_timer = Clock.schedule_once(self.get_markets, 1)

    # Karte erzeugen
    def get_markets(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        print(markets)
        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):
        # Erzeugen der Marker
        lat, lon = market[21], market[20]
        marker = Marker(lat=lat, lon=lon)
        marker.market_data = market

        # Marker auf die Karte setzen
        self.add_widget(marker)

        # Namen der Markets in Liste einfuegen/aufzaehlen
        name = market[1]
        self.market_names.append(name)