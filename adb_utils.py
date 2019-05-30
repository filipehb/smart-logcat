from adb.client import Client as AdbClient

class AdbUtils:
    def __init__(self, ip = "127.0.0.1", port = 5037):
        self.client = AdbClient(host=ip, port=port)

    def get_client_version(self):
        return self.client.version()

    def list_all_devices(self):
        for device in self.client.devices():
            return device.serial

    #Exemple "example.package"
    def is_installed_apk(self, device, apk_package):
        return device.is_installed(apk_package)

    def install_apk(self, device, apk_path):
        device.install(apk_path)

    #Exemple "example.package"
    def uninstall_apk(self, device, apk_package):
        device.install(apk_package)
        return self.is_installed_apk(device, apk_package)

    def get_device_name(self, device):
        model = device.shell("getprop ro.product.model")
        manufacturer = device.shell("getprop ro.product.manufacturer")
        full_name = manufacturer + " " + model
        return full_name.replace("\n", "").replace("\r", "")


if __name__ == '__main__':
    adb1 = AdbUtils()
    #print(adb1.list_all_devices())
    print(adb1.get_device_name(adb1.client.device(serial=adb1.list_all_devices())))
