from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import re
from kivy.app import App


class UI(ScreenManager):
    pass


class Scr_landing(Screen):
    pass


class PurpleBackground(Screen):
    pass


class Scr_invest(Screen):
    def __init__(self, **kwargs):
        super(Scr_invest, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.phone_input = TextInput(hint_text='Enter phone number')
        self.add_widget(self.phone_input)

        self.id_input = TextInput(hint_text='Enter ID number')
        self.add_widget(self.id_input)

        self.phone_input.bind(text=self.on_phone_input)
        self.id_input.bind(text=self.on_id_input)

    def on_phone_input(self, instance, value):
        if re.match(r'^[0-9]{10}$', value):
            self.phone_input.background_color = (0, 1, 0, 1)  # สีเขียว
        else:
            self.phone_input.background_color = (1, 0, 0, 1)  # สีแดง

    def on_id_input(self, instance, value):
        if re.match(r'^[0-9]{13}$', value):
            self.id_input.background_color = (0, 1, 0, 1)  # สีเขียว
        else:
            self.id_input.background_color = (1, 0, 0, 1)  # สีแดง


class investApp(App):
    def build(self):
        return UI()


if __name__ == "__main__":
    investApp().run()
