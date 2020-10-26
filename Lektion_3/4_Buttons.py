import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs): # -> ** bedeutet unendliche Anzahl von kwargs
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        
        self.inside = GridLayout()  # -> Objekt (Tabelle) wird erzeugt
        self.inside.cols = 2
        
        self.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)
        
        self.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)
        
        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        
        self.add_widget(self.inside)
        
        # Button
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
    def pressed(self, instance): # Methode der Klasse MyGrid => kann auf jedes erzeugte Objekt von MyGrid angewendet werden
        first_name = self.first_name.text
        last_name = self.last_name.text
        email = self.email.text
        
        print("First Name: ", first_name, "Last Name: ", last_name, "Email: ", email)
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()