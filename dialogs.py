from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

def alertPopup(title, msg):
    popup = Popup(title=title,
                      content=Label(text=msg),
                      size_hint=(None, None), size=(dp(600), dp(200)))
    popup.open()