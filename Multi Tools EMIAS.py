from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Window(object):
    def create_button(self, parent, b_size, icon_path, i_size=None):
        """Создание кнопок."""
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

    def create_widget(self, parent, size, widget_type, bold=False):
        """Создание виджетов."""
        widget_types = {
            "line": QtWidgets.QFrame,
            "lineEdit": QtWidgets.QLineEdit,
            "label": QtWidgets.QLabel,
            "textEdit": QtWidgets.QTextEdit
        }
        widget = widget_types.get(widget_type)(parent)
        widget.setGeometry(*size)

        if widget_type == "line":
            widget.setFrameShape(QtWidgets.QFrame.HLine)
            widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        elif widget_type == "label" and bold:
            widget.setFont(self.font)
        return widget

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

        self.font = QtGui.QFont()
        self.font.setPointSize(14)

        # Выпадающий список моделей принтера
        self.combo_model = QtWidgets.QComboBox(self.tab)
        self.combo_model.setGeometry(QtCore.QRect(248, 55, 111, 22))
        self.combo_model.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        for _ in range(8):
            self.combo_model.addItem("")

        # QFrame (Линии)
        self.line_print_1 = self.create_widget(
            self.tab,
            (10, 30, 403, 21),
            "line"
        )
        self.line_print_2 = self.create_widget(
            self.tab,
            (10, 80, 403, 21),
            "line",
        )
        self.line_scan_hp = self.create_widget(
            self.tab_2,
            (10, 30, 401, 21),
            "line",
        )

        # QLineEdit
        self.lineEdit_ip = self.create_widget(
            self.tab,
            (60, 55, 101, 22),
            "lineEdit"
        )
        self.lineEdit_cnt = self.create_widget(
            self.tab,
            (364, 55, 22, 22),
            "lineEdit"
        )
        self.lineEdit_login = self.create_widget(
            self.tab_2,
            (11, 67, 131, 22),
            "lineEdit"
        )
        self.lineEdit_ip_arm = self.create_widget(
            self.tab_2,
            (11, 152, 131, 22),
            "lineEdit"
        )
        self.lineEdit_hostname = self.create_widget(
            self.tab_2,
            (11, 110, 131, 22),
            "lineEdit"
        )

        # QLabel
        self.lbl_print = self.create_widget(
            self.tab,
            (10, 0, 151, 41),
            "label",
            True
        )
        self.lbl_scan_hp = self.create_widget(
            self.tab_2,
            (10, 0, 151, 41),
            "label",
            True
        )
        self.lbl_ip = self.create_widget(
            self.tab,
            (10, 60, 47, 13),
            "label"
        )
        self.lbl_model = self.create_widget(
            self.tab,
            (198, 60, 47, 13),
            "label"
        )
        self.lbl_hostname = self.create_widget(
            self.tab_2,
            (13, 92, 105, 16),
            "label"
        )
        self.lbl_ip_arm = self.create_widget(
            self.tab_2,
            (13, 134, 71, 16),
            "label"
        )
        self.lbl_login = self.create_widget(
            self.tab_2,
            (13, 48, 97, 16),
            "label"
        )
        self.textEdit = self.create_widget(
            self.tab_2,
            (211, 67, 200, 106),
            "textEdit"
        )

        # Кнопка "Копировать"
        self.btn_copy = self.create_button(
            self.tab,
            (391, 54, 24, 24),
            "icons/icon_copy.png"
        )
        self.btn_copy.clicked.connect(self.send_clipboard_printer)

        # Кнопка "Удалить IP"
        self.btn_clr_ip = self.create_button(
            self.tab,
            (163, 54, 24, 24),
            "icons/icon_delete.png"
        )
        self.btn_clr_ip.clicked.connect(self.lineEdit_ip.clear)

        # Кнопка "Очистить очередь печати"
        self.btn_clr_spooler = self.create_button(
            self.tab,
            (44, 100, 38, 40),
            "icons/icon_clear.png",
            (35, 35)
        )
        self.btn_clr_spooler.clicked.connect(self.send_clipboard_clr_spooler)

        # Кнопка "Печать тестовой страницы"
        self.btn_test_page = self.create_button(
            self.tab,
            (87, 100, 37, 40),
            "icons/icon_test_page.png",
            (32, 32)
        )
        self.btn_test_page.clicked.connect(self.send_clipboard_test_page)

        # Кнопка "Удаления принтера"
        self.btn_del_printer = self.create_button(
            self.tab,
            (129, 100, 38, 40),
            "icons/icon_delete_printer.png",
            (32, 32)
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
        self.btn_clear_hostname.clicked.connect(self.lineEdit_hostname.clear)

        # Кнопка "Очистить IP"
        self.btn_clear_ip_scan_hp = self.create_button(
            self.tab_2,
            (151, 150, 24, 24),
            "icons/icon_delete.png"
        )
        self.btn_clear_ip_scan_hp.clicked.connect(self.lineEdit_ip_arm.clear)

        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(-210, 910, 300, 200))
        self.quickWidget.setResizeMode(
            QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        Window.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(Window)
        self.retranslateUi(Window)
        self.Main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def combobox_menu(self):
        """Выпадающий список для моделей."""
        models = (
            "HP LaserJet M401",
            "HP LaserJet M404",
            "HP LaserJet M501",
            "HP LaserJet M425",
            "HP LaserJet M426",
            "Pantum BP5100",
            "Pantum BM5100"
        )
        for idx, model in enumerate(models, start=1):
            self.combo_model.setItemText(idx, model)

    def title_tip(self):
        """Надписи и подсказки."""
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
            self.btn_clr_ip: "Очистить поле",
            self.lineEdit_cnt: "Номер принтера",
            self.btn_clr_spooler: "Очистить очередь печати",
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
                widget.setText(self._translate("Window", text))
            else:
                widget.setToolTip(self._translate("Window", text))

    def retranslateUi(self, Window):
        self._translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(self._translate("Window", "Multi Tools EMIAS"))
        Window.setWindowIcon(QtGui.QIcon(fr'logo.ico'))
        self.combobox_menu()
        self.title_tip()
        self.Main.setTabText(
            self.Main.indexOf(self.tab),
            self._translate("Window", "Печать"))
        self.Main.setTabText(
            self.Main.indexOf(self.tab_2),
            self._translate("Window", "Сканирование (HP)"))
        self.actionExit.setText(self._translate("Window", "Exit"))

    def send_clipboard_printer(self):
        """Команда для установки принтера."""
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
        cnt = ""
        if self.lineEdit_cnt.text() != '':
            cnt = '-' + self.lineEdit_cnt.text()
        model = self.combo_model.currentText().replace(' ', '-').replace('Pantum-', '')
        ftp = ("wget -nc /home/admin "
               "ftp://printer:z123456Z"
               "@srv-ftp02/13_ochered/PPD/PANTUM_5100.ppd")
        if model:
            install = (f"/usr/sbin/lpadmin -p "
                       f"'{model + cnt if cnt else model}' -v "
                       f"'socket://{ip}:9100' -P '{drivers[model]}'")
            enable = f"/usr/sbin/cupsenable {model}"
            accept = f"/usr/sbin/cupsaccept {model}"
            default = f"/usr/sbin/lpadmin -d {model}"
            options = f"lpoptions -d {model}"
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

    def send_clipboard_cups(self):
        """Команда для перезагрузки службы CUPS."""
        command = "systemctl restart cups"
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
        login = self.lineEdit_login.text()
        hostname = self.lineEdit_hostname.text()
        command = (fr"\{hostname}.mosgorzdrav.local\scan\{login}"
                   .replace(" ", ""))
        QApplication.clipboard().setText(command)

    def send_clipboard_ip_arm(self):
        """Команда для настройки сканирования через 'ip-адрес' АРМ."""
        login = self.lineEdit_login.text()
        ip = self.lineEdit_ip_arm.text()
        command = fr"\{ip}\scan\{login}".replace(" ", "")
        QApplication.clipboard().setText(command)

    def clear_all_scan(self):
        """Команда для очистки всех полей на вкладке 'Сканирование'."""
        self.lineEdit_login.clear()
        self.textEdit.clear()
        self.lineEdit_ip_arm.clear()
        self.lineEdit_hostname.clear()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
