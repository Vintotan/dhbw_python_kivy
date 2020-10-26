import kivy
from kivy import * # -> laedt gesamtes Kivy-Framework in die Datei
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

# Grids mit Items wie Spalten und Zeilen
class MyGrid(Widget):
    name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    
class Six_App(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Six_App().run()

