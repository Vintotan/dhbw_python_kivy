from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button


# Erzeugen des Widget
class MyPaintWidget(Widget):
    def on_touch_down(self, touch):  # Methode der Klasse "MyPaintWidget"
        color = (random(), 1, 1)
        with self.canvas:  # Klassenvariable der Oberklasse "Widget"
            Color(*color, mode='hsv')
            # Color(1, 0, 0) # '1, 0, 0' sind Argumente - eigentliche Parameter der Klasse "Color" lauten 'red, green, blue'
            d = 30. 
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y)) # bei ud handelt es sich um ein Dictionary

    def on_touch_move(self, touch):  # Methode der Klasse "MyPaintWidget", weil "self" als Parameter uebergeben wird
        touch.ud['line'].points += [touch.x, touch.y]


# Erzeugen der Basis-Kivy-App
class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()  # Objekt wird erzeugt aus der Klasse "MyPaintWidget()"
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):  # obj -> Einfluss auf alle erzeugten Objekte tätigen
        self.painter.canvas.clear()


# Aufruf Hauptprogramm
if __name__ == '__main__':
    MyPaintApp().run()