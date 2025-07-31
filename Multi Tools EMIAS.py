from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets, uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QTableWidgetItem, QDialog)
import sys, os

class MainWindow(QMainWindow):
    """"Главное окно."""
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(self.resource_path('ui\multi_tools.ui'), self)
        self.setWindowIcon(QtGui.QIcon(self.resource_path('ui\icons\logo.ico')))
        self.btn_clear_ip.clicked.connect(self.le_ip.clear)
        self.btn_copy.clicked.connect(self.send_clipboard_printer)
        self.btn_claer_spooler.clicked.connect(self.send_clipboard_clr_spooler)
        self.btn_test_page.clicked.connect(self.send_clipboard_test_page)
        self.btn_del_printer.clicked.connect(self.send_clipboard_del_printer)
        self.btn_reboot.clicked.connect(self.send_clipboard_reboot)
        self.btn_reboot_prn.clicked.connect(self.send_clipboard_reboot_printer)
        self.btn_reset_prn.clicked.connect(self.send_clipboard_reset_printer)
        self.btn_default.clicked.connect(self.send_clipboard_default)
        self.btn_rename.clicked.connect(self.send_clipboard_rename)
        self.btn_password.clicked.connect(self.send_clipboard_password)
        self.btn_copy_hostname.clicked.connect(self.send_clipboard_hostname)
        self.btn_copy_ip.clicked.connect(self.send_clipboard_ip_arm)
        self.btn_clear_all.clicked.connect(self.clear_all_scan)
        self.btn_clear_hostname.clicked.connect(self.le_hostname.clear)
        self.btn_clear_ip_scan.clicked.connect(self.le_ip_arm.clear)
        self.btn_copy_check_hostname.clicked.connect(
            lambda:
            self.send_clipboard_check_smb_folder(self.le_hostname.text()))
        self.btn_copy_check_ip.clicked.connect(
            lambda:
            self.send_clipboard_check_smb_folder(self.le_ip_arm.text()))


    def resource_path(self, relative_path):
        """Получает абсолютный путь к ресурсу,
        работает как в режиме разработки, так и в скомпилированном виде."""
        try:
            # PyInstaller создает временную папку и сохраняет путь к ней
            # в атрибуте `_MEIPASS`
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def send_clipboard_printer(self):
        """Команда для установки принтера."""
        ip = self.le_ip.text().replace(" ", "")
        folder_1 = "/opt/Printer_Drivers/Ochered/4-ya ochered/"
        folder_2 = "/home/admin/"
        drivers = {
            "HP-LaserJet-M425": f"{folder_1}HP-LaserJet-400-MFP-M425.ppd",
            "HP-LaserJet-M426": f"{folder_1}HP-LaserJet-400-MFP-M425.ppd",
            "HP-LaserJet-M401": f"{folder_1}HP-LaserJet-400-M401.ppd",
            "HP-LaserJet-M404": f"{folder_1}HP-LaserJet-400-M401.ppd",
            "HP-LaserJet-M501": f"{folder_1}HP-LaserJet-400-M401.ppd",
            "BP5100": f"{folder_2}PANTUM_5100.ppd",
            "BM5100": f"{folder_2}PANTUM_5100.ppd"
        }
        cnt = ""
        if self.le_cnt.text() != '':
            cnt = '-' + self.le_cnt.text()
        model = self.cb_model.currentText().replace(' ', '-').replace('Pantum-', '')
        ftp = ("wget -nc /home/admin "
               "ftp://printer:z123456Z"
               "@srv-ftp02/13_ochered/PPD/PANTUM_5100.ppd")
        if model:
            install = (f"/usr/sbin/lpadmin -p "
                       f"'{model + cnt if cnt else model}' -v "
                       f"'socket://{ip}:9100' -P '{drivers[model]}'")
            enable = f"/usr/sbin/cupsenable {model}{cnt}"
            accept = f"/usr/sbin/cupsaccept {model}{cnt}"
            default = f"/usr/sbin/lpadmin -d {model}{cnt}"
            options = f"lpoptions -d {model}{cnt}"
            test_page = "lpr /usr/share/cups/data/default-testpage.pdf"
            status = "lpstat -t"
            commands = [
                install,
                enable,
                accept,
                default,
                options,
                test_page,
                status
            ]
            if '5100' in model:
                commands.insert(0, ftp)
            command = ";".join(commands)
            QApplication.clipboard().setText(command)


    def send_clipboard_clr_spooler(self):
        """Команда для чистки очереди печати."""
        command = "lprm -;lpstat -t"
        QApplication.clipboard().setText(command)


    def send_clipboard_test_page(self):
        """Команда для печати тестовой страницы с принтера."""
        command = "lpr /usr/share/cups/data/default-testpage.pdf;lpstat -t"
        QApplication.clipboard().setText(command)

    def send_clipboard_del_printer(self):
        """Команда для удаления принтера."""
        command = "/usr/sbin/lpadmin -x "
        QApplication.clipboard().setText(command)

    def send_clipboard_reboot(self):
        """Команда для перезагрузки АРМ."""
        command = "systemctl reboot -i"
        QApplication.clipboard().setText(command)

    def send_clipboard_reboot_printer(self):
        """Команда для перезагрузки принтера."""
        ip = self.le_ip.text().replace(" ", "")
        oid = '1.3.6.1.2.1.43.5.1.1.3.1'
        value = 4
        command = f"snmpset -v1 -c public {ip} {oid} i {value}"
        QApplication.clipboard().setText(command)

    def send_clipboard_reset_printer(self):
        """Команда для сброса настроек принтера."""
        ip = self.le_ip.text().replace(" ", "")
        oid = '1.3.6.1.2.1.43.5.1.1.3.1'
        value = 6
        command = f"snmpset -v1 -c public {ip} {oid} i {value}"
        QApplication.clipboard().setText(command)

    def send_clipboard_default(self):
        """Команда для устаовки принтера по умолчанию."""
        command = "/usr/sbin/lpadmin -d "
        QApplication.clipboard().setText(command)

    def send_clipboard_rename(self):
        """Команда для смены 'hostname' АРМ."""
        command = "hostnamectl set-hostname "
        QApplication.clipboard().setText(command)

    def send_clipboard_password(self):
        """Пароль."""
        command = "o123456O"
        QApplication.clipboard().setText(command)

    def send_clipboard_hostname(self):
        """Команда для настройки сканирования через 'hostname' АРМ."""
        login = self.le_login.text()
        hostname = self.le_hostname.text()
        command = (fr"\\{hostname}.mosgorzdrav.local\scan\{login}"
                   .replace(" ", ""))
        QApplication.clipboard().setText(command)

    def send_clipboard_ip_arm(self):
        """Команда для настройки сканирования через 'ip-адрес' АРМ."""
        login = self.le_login.text()
        ip = self.le_ip_arm.text()
        command = fr"\\{ip}\scan\{login}".replace(" ", "")
        QApplication.clipboard().setText(command)

    def clear_all_scan(self):
        """Команда для очистки всех полей на вкладке 'Сканирование'."""
        self.le_login.clear()
        self.te_temp.clear()
        self.le_ip_arm.clear()
        self.le_hostname.clear()

    def send_clipboard_check_smb_folder(self, host):
        login = self.le_login.text()
        smb = fr'\\{host}.mosgorzdrav.local\scan\{login}'.replace(" ", "")
        command = fr'net use {smb} /user:scan ol23lrm'
        QApplication.clipboard().setText(command)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
