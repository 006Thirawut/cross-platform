from kivy.app import App
from kivy.uix.screenmanager import Screen

class UI(Screen):
    def add_item(self):
        #น้ำค่าที่พิมพ์ผ่านช่อง textinput ไปเพิ่มใน spinner
        self.ids.spin_lang.values.append(self.ids.txt_input.text)

class spinnerApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    spinnerApp().run()