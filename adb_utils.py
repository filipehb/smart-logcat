import subprocess
import datetime
from adb.client import Client as AdbClient


class AdbUtils:
    def __init__(self, ip="127.0.0.1", port=5037):
        subprocess.run(["adb", "devices"])
        self.client = AdbClient(host=ip, port=port)
        self.devices = []

    def get_client_version(self):
        return self.client.version()

    def list_all_devices(self):
        for device in self.client.devices():
            self.devices.append(device.serial)
        return self.devices

    # Exemple "example.package"
    def is_installed_apk(self, device, apk_package):
        return device.is_installed(apk_package)

    def install_apk(self, device, apk_path):
        device.install(apk_path)

    # Exemple "example.package"
    def uninstall_apk(self, device, apk_package):
        device.install(apk_package)
        return self.is_installed_apk(device, apk_package)

    def get_device_name(self, device):
        model = device.shell("getprop ro.product.model")
        manufacturer = device.shell("getprop ro.product.manufacturer")
        full_name = manufacturer + " " + model
        return full_name.replace("\n", "").replace("\r", "")

    def _dump_logcat(connection):
        while True:
            data = connection.read(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        connection.close()

    def get_device_logcat(self, device):
        return device.shell("logcat", handler=self._dump_logcat)

    def get_screen_shot(self, device):
        result = device.screencap()
        with open(datetime.datetime.now().replace(" ","").replace("-","").replace(":","").replace(".","") + ".png", "wb") as fp:
            fp.write(result)


if __name__ == '__main__':
    adb1 = AdbUtils()
    # print(adb1.list_all_devices())
    for device in adb1.list_all_devices():
        print(adb1.get_device_name(adb1.client.device(serial=device)))
        print(adb1.get_device_logcat(adb1.client.device(serial=device)))
