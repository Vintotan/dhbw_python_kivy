from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

from kivy.uix.screenmanager import Screen 


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="KivyMD App", 
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
        )
        return screen


if __name__ == "__main__":
    MainApp().run()