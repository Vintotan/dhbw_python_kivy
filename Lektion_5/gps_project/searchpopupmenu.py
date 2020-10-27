from kivy.app import App 
from kivy.clock import Clock 
from kivy.network.urlrequest import UrlRequest 
from urllib import parse
from kivymd.uix.dialog import MDInputDialog
import certifi


class SearchPopupMenu(MDInputDialog):
    title = "Suche nach der Adresse"
    text_button_ok = 'Suche'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback 

    def callback(self):
        address = self.text_field.text 
        self.geocode_get_lon_lat(address)

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def geocode_get_lat_lon(self, address):
        with open('app_id.txt', 'r') as f:
            app_id = f.read()
        with open('app_code.txt', 'r') as f:
            app_code = f.read()
        address = parse.quote(address)
        url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("Erfolgreiche Suche")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def failure(self, urlrequest, result):
        print("Fehlerhafte Suche")
        print(result)

    def error(self, urlrequest, result):
        print("Fehlgeschlagene Suche")
        print(result)


    