from kivy.app import App
from kivy.uix.widget import Widget
from dialogs import alertPopup
from kivy.logger import Logger
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
Config.window_icon = "icon.png"
dropdown = DropDown()
#Window.minimum_height = 600
#Window.minimum_width = 800
#Window.maximize()

class SmartLogcat(Widget):
    def search(self, text):
        print('texto digitado: {}'.format(text))
    
    def take_screenshot(self):
        print('foto tirada')

    def _popule_serials(self):
        labelSerial = Label(text="Devices")
        for target_list in expression_list:
            l = Label(text=target_list)
            dropdown.add_widget(l)
        
        labelSerial.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(labelSerial, 'text', x))

class SmartLogcatApp(App):
    icon = 'icon.png'

    def build(self):
        return SmartLogcat()
    
    def _serial_warning(self):
        alertPopup('Warning', 'Command failed. Ensure you have selected a correct serial port')

if __name__ == '__main__':
    Logger.info('Aplicação iniciada')
    SmartLogcatApp().run()