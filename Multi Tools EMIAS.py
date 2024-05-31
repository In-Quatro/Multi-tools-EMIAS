from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Window(object):

    def create_button(self, parent, b_size, icon_path, i_size=None):
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(*b_size))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if i_size:
            button.setIconSize(QtCore.QSize(*i_size))
        button.setIcon(icon)
        return button

    def setupUi(self, Window):
        # Параметры окна
        Window.setEnabled(True)
        Window.resize(426, 210)
        Window.setMinimumSize(QtCore.QSize(426, 210))
        Window.setMaximumSize(QtCore.QSize(426, 210))
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Main = QtWidgets.QTabWidget(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(0, 0, 428, 211))
        self.Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Main.setTabPosition(QtWidgets.QTabWidget.North)
        self.Main.setElideMode(QtCore.Qt.ElideNone)

        # Вкладка 1
        self.tab = QtWidgets.QWidget()
        self.Main.addTab(self.tab, "")

        # Вкладка 2
        self.tab_2 = QtWidgets.QWidget()
        self.Main.addTab(self.tab_2, "")

        font = QtGui.QFont()
        font.setPointSize(14)

        # Выпадающий список моделей принтера
        self.combo_model = QtWidgets.QComboBox(self.tab)
        self.combo_model.setGeometry(QtCore.QRect(248, 55, 111, 22))
        self.combo_model.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        for _ in range(8):
            self.combo_model.addItem("")

        self.lineEdit_ip = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ip.setGeometry(QtCore.QRect(60, 55, 101, 22))

        self.lbl_ip = QtWidgets.QLabel(self.tab)
        self.lbl_ip.setGeometry(QtCore.QRect(10, 60, 47, 13))

        self.lbl_model = QtWidgets.QLabel(self.tab)
        self.lbl_model.setGeometry(QtCore.QRect(198, 60, 47, 13))

        # Линии
        self.line_print_1 = QtWidgets.QFrame(self.tab)
        self.line_print_1.setGeometry(QtCore.QRect(10, 30, 403, 21))
        self.line_print_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_print_1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_print_2 = QtWidgets.QFrame(self.tab)
        self.line_print_2.setGeometry(QtCore.QRect(10, 80, 403, 21))
        self.line_print_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_print_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_scan_hp = QtWidgets.QFrame(self.tab_2)
        self.line_scan_hp.setGeometry(QtCore.QRect(10, 30, 401, 21))
        self.line_scan_hp.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_scan_hp.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.lbl_print = QtWidgets.QLabel(self.tab)
        self.lbl_print.setGeometry(QtCore.QRect(10, 0, 151, 41))
        self.lbl_print.setFont(font)

        self.lbl_scan_hp = QtWidgets.QLabel(self.tab_2)
        self.lbl_scan_hp.setGeometry(QtCore.QRect(10, 0, 151, 41))
        self.lbl_scan_hp.setFont(font)



        self.lineEdit_cnt = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_cnt.setGeometry(QtCore.QRect(364, 55, 22, 22))

        self.lineEdit_ip_arm = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ip_arm.setGeometry(QtCore.QRect(11, 152, 131, 22))

        self.lineEdit_login = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_login.setGeometry(QtCore.QRect(11, 67, 131, 22))

        self.lbl_hostname = QtWidgets.QLabel(self.tab_2)
        self.lbl_hostname.setGeometry(QtCore.QRect(13, 92, 105, 16))

        self.lbl_ip_arm = QtWidgets.QLabel(self.tab_2)
        self.lbl_ip_arm.setGeometry(QtCore.QRect(13, 134, 71, 16))

        self.lbl_login = QtWidgets.QLabel(self.tab_2)
        self.lbl_login.setGeometry(QtCore.QRect(13, 48, 97, 16))

        self.lineEdit_hostname = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_hostname.setGeometry(QtCore.QRect(11, 110, 131, 22))

        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(211, 67, 200, 106))

        # Кнопка "Копировать"
        self.btn_copy = self.create_button(
            self.tab,
            (391, 54, 24, 24),
            "icons/icon_copy.png"
        )
        self.btn_copy.clicked.connect(self.send_clipboard_printer)

        # Кнопка "Удалить IP"
        self.btn_clear_ip = self.create_button(
            self.tab,
            [163, 54, 24, 24],
            "icons/icon_delete.png"
        )
        self.btn_clear_ip.clicked.connect(self.lineEdit_ip.clear)

        # Кнопка "Очистить очередь печати"
        self.btn_claer_spooler = self.create_button(
            self.tab,
            [44, 100, 38, 40],
            "icons/icon_clear.png",
            [35, 35]
        )
        self.btn_claer_spooler.clicked.connect(self.send_clipboard_clr_spooler)

        # Кнопка "Печать тестовой страницы"
        self.btn_test_page = self.create_button(
            self.tab,
            [87, 100, 37, 40],
            "icons/icon_test_page.png",
            [32, 32]
        )
        self.btn_test_page.clicked.connect(self.send_clipboard_test_page)

        # Кнопка "Удаления принтера"
        self.btn_del_printer = self.create_button(
            self.tab,
            [129, 100, 38, 40],
            "icons/icon_delete_printer.png",
            [32, 32]
        )
        self.btn_del_printer.clicked.connect(self.send_clipboard_del_printer)

        # Кнопка "Перезагрузка АРМ"
        self.btn_reboot = self.create_button(
            self.tab,
            (172, 100, 38, 40),
            "icons/icon_reboot.png",
            (32, 32)
        )
        self.btn_reboot.clicked.connect(self.send_clipboard_reboot)

        # Кнопка "Перезагрузки CUPS"
        self.btn_cups = self.create_button(
            self.tab,
            (215, 100, 38, 40),
            "icons/icon_cups.png",
            (32, 32)
        )
        self.btn_cups.clicked.connect(self.send_clipboard_cups)

        # Кнопка "Сделать принтер по умолчанию"
        self.btn_default = self.create_button(
            self.tab,
            (258, 100, 38, 40),
            "icons/icon_default.png",
            (32, 32)
        )
        self.btn_default.clicked.connect(self.send_clipboard_default)

        # Кнопка "Переименовать АРМ"
        self.btn_rename = self.create_button(
            self.tab,
            (300, 100, 37, 40),
            "icons/icon_rename.png",
            (25, 25)
        )
        self.btn_rename.clicked.connect(self.send_clipboard_rename)

        # Кнопка "Пароль"
        self.btn_password = self.create_button(
            self.tab,
            (342, 100, 37, 40),
            "icons/icon_password.png",
            (25, 25)
        )
        self.btn_password.clicked.connect(self.send_clipboard_password)

        # Кнопка "Настроить по hostname"
        self.btn_copy_hostname = self.create_button(
            self.tab_2,
            (180, 110, 24, 24),
            "icons/icon_copy.png"
        )
        self.btn_copy_hostname.clicked.connect(self.send_clipboard_hostname)

        # Кнопка "Настроить по IP"
        self.btn_copy_ip = self.create_button(
            self.tab_2,
            (180, 150, 24, 24),
            "icons/icon_copy.png"
        )
        self.btn_copy_ip.clicked.connect(self.send_clipboard_ip_arm)

        # Кнопка "Очистить все"
        self.btn_clear_all = self.create_button(
            self.tab_2,
            (150, 67, 24, 24),
            "icons/icon_delete.png"
        )
        self.btn_clear_all.clicked.connect(self.clear_all_scan)

        # Кнопка "Очистить hostname"
        self.btn_clear_hostname = self.create_button(
            self.tab_2,
            (151, 110, 24, 24),
            "icons/icon_delete.png"
        )
        self.btn_clear_hostname.clicked.connect(self.clear_hostname_hp)

        # Кнопка "Очистить IP"
        self.btn_clear_ip_scan_hp = self.create_button(
            self.tab_2,
            (151, 150, 24, 24),
            "icons/icon_delete.png"
        )
        self.btn_clear_ip_scan_hp.clicked.connect(self.clear_ip_hp)

        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(-210, 910, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)

        Window.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(Window)
        self.retranslateUi(Window)
        self.Main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def combobox_menu(self):
        """Комбобокс для моделей."""
        models = [
            "HP LaserJet M401",
            "HP LaserJet M404",
            "HP LaserJet M501",
            "HP LaserJet M425",
            "HP LaserJet M426",
            "Pantum BP5100",
            "Pantum BM5100"
        ]
        for idx, model in enumerate(models, start=1):
            self.combo_model.setItemText(idx, model)

    def title_tip(self):
        """Надписи и подсказки."""
        _translate = QtCore.QCoreApplication.translate
        titles = {
            self.lbl_ip: "IP адрес:",
            self.lbl_model: "Модель:",
            self.lbl_print: "<span style=\"font-weight:600;\">Печать",
            self.lbl_scan_hp: "<span style=\"font-weight:600;\">Сканирование",
            self.lbl_hostname: "Имя (hostname) АРМ:",
            self.lbl_ip_arm: "IP адрес АРМ:",
            self.lbl_login: "Имя пользователя:",
        }
        tips = {
            self.btn_copy: "Копировать в буфер",
            self.btn_clear_ip: "Очистить поле",
            self.lineEdit_cnt: "Номер принтера",
            self.btn_claer_spooler: "Очистить очередь печати",
            self.btn_test_page: "Тестовая страница",
            self.btn_del_printer: "Удалить принтер",
            self.btn_reboot: "Перезагрузка АРМ",
            self.btn_cups: "Перезагрузить службы CUPS",
            self.btn_default: "Сделать принтер по умолчнию",
            self.btn_rename: "Периеименовать hostname АРМ",
            self.btn_password: "Пароль (o123456O)",
            self.btn_copy_hostname: "Копировать в буфер",
            self.btn_copy_ip: "Копировать в буфер",
            self.btn_clear_all: "Очистить все поля",
            self.btn_clear_hostname: "Очистить поле",
            self.btn_clear_ip_scan_hp: "Очистить поле",
        }

        for widget, text in {**titles, **tips}.items():
            if isinstance(widget, QtWidgets.QLabel):
                widget.setText(_translate("Window", text))
            else:
                widget.setToolTip(_translate("Window", text))



    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Multi Tools EMIAS"))
        Window.setWindowIcon(QtGui.QIcon('emias.ico'))
        self.combobox_menu()
        self.title_tip()
        self.Main.setTabText(self.Main.indexOf(self.tab),
                             _translate("Window", "Печать"))
        self.Main.setTabText(self.Main.indexOf(self.tab_2),
                             _translate("Window", "Сканирование (HP)"))
        self.actionExit.setText(_translate("Window", "Exit"))


    def send_clipboard_printer(self):
        ip = self.lineEdit_ip.text().replace(" ", "")
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
        cnt = ''
        if self.lineEdit_cnt.text() != '':
            cnt = '-' + self.lineEdit_cnt.text()
        models = self.combo_model.currentText().replace(' ', '-').replace('Pantum-', '')
        model = models
        ftp = ("wget -nc /home/admin "
               "ftp://printer:z123456Z"
               "@srv-ftp02/13_ochered/PPD/PANTUM_5100.ppd")
        models += cnt
        if models:
            install = (f"/usr/sbin/lpadmin -p '{models}' -v "
                       f"'socket://{ip}:9100' -P '{drivers[model]}'")
            enable = f"/usr/sbin/cupsenable {models}"
            accept = f"/usr/sbin/cupsaccept {models}"
            default = f"/usr/sbin/lpadmin -d {models}"
            options = f"lpoptions -d {models}"
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
        command = "lprm -;lpstat -t"
        QApplication.clipboard().setText(command)

    def send_clipboard_test_page(self):
        command = "lpr /usr/share/cups/data/default-testpage.pdf;lpstat -t"
        QApplication.clipboard().setText(command)

    def send_clipboard_del_printer(self):
        command = "/usr/sbin/lpadmin -x "
        QApplication.clipboard().setText(command)

    def send_clipboard_reboot(self):
        command = "systemctl reboot -i"
        QApplication.clipboard().setText(command)

    def send_clipboard_cups(self):
        command = "systemctl restart cups"
        QApplication.clipboard().setText(command)

    def send_clipboard_default(self):
        command = "/usr/sbin/lpadmin -d "
        QApplication.clipboard().setText(command)

    def send_clipboard_rename(self):
        command = "hostnamectl set-hostname "
        QApplication.clipboard().setText(command)

    def send_clipboard_password(self):
        command = "o123456O"
        QApplication.clipboard().setText(command)

    def send_clipboard_hostname(self):
        login = self.lineEdit_login.text().replace(" ", "")
        hostname = self.lineEdit_hostname.text().replace(" ", "")
        command = f"\\\{hostname}.mosgorzdrav.local\scan\{login}"
        QApplication.clipboard().setText(command)

    def send_clipboard_ip_arm(self):
        login = self.lineEdit_login.text()
        ip = self.lineEdit_ip_arm.text()
        command = f"\\\{ip}\scan\{login}".replace(" ", "")
        QApplication.clipboard().setText(command)

    def clear_hostname_hp(self):
        self.lineEdit_hostname.clear()

    def clear_ip_hp(self):
        self.lineEdit_ip_arm.clear()

    def clear_all_scan(self):
        self.lineEdit_login.clear()
        self.textEdit.clear()
        self.clear_ip_hp()
        self.clear_hostname_hp()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
