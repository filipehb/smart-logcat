from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from dialogs import showInformationDialog
from adb_utils import AdbUtils

class SmartLogcat():
    def __init__(self, window):
        """Construtor."""
        #Adb Utils
        adbutils = AdbUtils()
        # Widgets
        self.comboBoxSerial = window.comboBoxSerial
        self.lineEditSearch = window.lineEditSearch
        self.plainTextEditLog = window.plainTextEditLog
        self.pushButtonSaveLog = window.pushButtonSaveLog
        self.pushButtonTakeScreenshot = window.pushButtonTakeScreenshot
        # Conectando um método ao evento de clique do botão.
        self.pushButtonSaveLog.clicked.connect(self.pushButtonSaveLog_on_button_clicked)
        self.pushButtonTakeScreenshot.clicked.connect(self.pushButtonTakeScreenshot_on_button_clicked)

    def pushButtonSaveLog_on_button_clicked(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        text = self.plainTextEditLog.text()
        # Verificando se algo foi digitado.
        #if text:
            #self.label.setText(text)
        #else:
            #self.label.setText('Digite algo no campo de texto :)')

    def pushButtonTakeScreenshot_on_button_clicked(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        text = self.plainTextEditLog.text()
        # Verificando se algo foi digitado.
        #if text:
            #self.label.setText(text)
        #else:
            #self.label.setText('Digite algo no campo de texto :)')

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

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = loadUi('main.ui')
    ui = SmartLogcat(window=window)
    window.show()
    sys.exit(app.exec_())