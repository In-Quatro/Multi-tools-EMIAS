from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setEnabled(True)
        Window.resize(426, 210)
        Window.setMinimumSize(QtCore.QSize(426, 210))
        Window.setMaximumSize(QtCore.QSize(426, 210))
        Window.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Main = QtWidgets.QTabWidget(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(0, 0, 428, 211))
        self.Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Main.setStyleSheet("")
        self.Main.setTabPosition(QtWidgets.QTabWidget.North)
        self.Main.setElideMode(QtCore.Qt.ElideNone)
        self.Main.setObjectName("Main")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.combo_model = QtWidgets.QComboBox(self.tab)
        self.combo_model.setGeometry(QtCore.QRect(248, 55, 111, 22))
        self.combo_model.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.combo_model.setObjectName("combo_model")
        self.combo_model.addItem("")
        self.combo_model.setItemText(0, "")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ip.setGeometry(QtCore.QRect(60, 55, 101, 22))
        self.lineEdit_ip.setText("")
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lbl_ip = QtWidgets.QLabel(self.tab)
        self.lbl_ip.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.lbl_ip.setObjectName("lbl_ip")
        self.lbl_model = QtWidgets.QLabel(self.tab)
        self.lbl_model.setGeometry(QtCore.QRect(198, 60, 47, 13))
        self.lbl_model.setObjectName("lbl_model")

        # Кнопка "Копировать"
        self.btn_copy = QtWidgets.QPushButton(self.tab)
        self.btn_copy.setGeometry(QtCore.QRect(391, 54, 24, 24))
        self.btn_copy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy.setIcon(icon)
        self.btn_copy.setObjectName("btn_copy")
        self.btn_copy.clicked.connect(self.send_to_clipboard_printer)

        self.line_print_2 = QtWidgets.QFrame(self.tab)
        self.line_print_2.setGeometry(QtCore.QRect(10, 80, 403, 21))
        self.line_print_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_print_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_print_2.setObjectName("line_print_2")

        # Кнопка "Удалить IP"
        self.btn_clear_ip = QtWidgets.QPushButton(self.tab)
        self.btn_clear_ip.setGeometry(QtCore.QRect(163, 54, 24, 24))
        self.btn_clear_ip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_ip.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear_ip.setIcon(icon1)
        self.btn_clear_ip.setObjectName("btn_clear_ip")
        self.btn_clear_ip.clicked.connect(self.lineEdit_ip.clear)


        self.lbl_print = QtWidgets.QLabel(self.tab)
        self.lbl_print.setGeometry(QtCore.QRect(10, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_print.setFont(font)
        self.lbl_print.setObjectName("lbl_print")
        self.line_print_1 = QtWidgets.QFrame(self.tab)
        self.line_print_1.setGeometry(QtCore.QRect(10, 30, 403, 21))
        self.line_print_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_print_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_print_1.setObjectName("line_print_1")
        self.lineEdit_cnt = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_cnt.setGeometry(QtCore.QRect(364, 55, 22, 22))
        self.lineEdit_cnt.setObjectName("lineEdit_cnt")

        # Кнопка "Очистить очередь печати"
        self.btn_claer_spooler = QtWidgets.QPushButton(self.tab)
        self.btn_claer_spooler.setGeometry(QtCore.QRect(44, 100, 38, 40))
        self.btn_claer_spooler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_claer_spooler.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icon_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_claer_spooler.setIcon(icon2)
        self.btn_claer_spooler.setIconSize(QtCore.QSize(35, 35))
        self.btn_claer_spooler.setObjectName("btn_claer_spooler")
        self.btn_claer_spooler.clicked.connect(self.send_to_clipboard_clear_spooler)

        # Кнопка "Печать тестовой страницы"
        self.btn_test_page = QtWidgets.QPushButton(self.tab)
        self.btn_test_page.setEnabled(True)
        self.btn_test_page.setGeometry(QtCore.QRect(87, 100, 37, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_test_page.sizePolicy().hasHeightForWidth())
        self.btn_test_page.setSizePolicy(sizePolicy)
        self.btn_test_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_test_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/icon_test_page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_test_page.setIcon(icon3)
        self.btn_test_page.setIconSize(QtCore.QSize(32, 32))
        self.btn_test_page.setObjectName("btn_test_page")
        self.btn_test_page.clicked.connect(self.send_to_clipboard_test_page)

        # Кнопка "Удаления принтера"
        self.btn_del_printer = QtWidgets.QPushButton(self.tab)
        self.btn_del_printer.setGeometry(QtCore.QRect(129, 100, 38, 40))
        self.btn_del_printer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_del_printer.setAccessibleName("")
        self.btn_del_printer.setAccessibleDescription("")
        self.btn_del_printer.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/icon_delete_printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_del_printer.setIcon(icon4)
        self.btn_del_printer.setIconSize(QtCore.QSize(32, 32))
        self.btn_del_printer.setObjectName("btn_del_printer")
        self.btn_del_printer.clicked.connect(self.send_to_clipboard_del_printer)

        # Кнопка "Перезагрузка АРМ"
        self.btn_reboot = QtWidgets.QPushButton(self.tab)
        self.btn_reboot.setGeometry(QtCore.QRect(172, 100, 38, 40))
        self.btn_reboot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reboot.setAccessibleName("")
        self.btn_reboot.setAccessibleDescription("")
        self.btn_reboot.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/icon_reboot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reboot.setIcon(icon5)
        self.btn_reboot.setIconSize(QtCore.QSize(32, 32))
        self.btn_reboot.setObjectName("btn_reboot")
        self.btn_reboot.clicked.connect(self.send_to_clipboard_reboot)

        # Кнопка "Перезагрузки CUPS"
        self.btn_cups = QtWidgets.QPushButton(self.tab)
        self.btn_cups.setGeometry(QtCore.QRect(215, 100, 38, 40))
        self.btn_cups.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cups.setAccessibleName("")
        self.btn_cups.setAccessibleDescription("")
        self.btn_cups.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/icon_cups.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cups.setIcon(icon6)
        self.btn_cups.setIconSize(QtCore.QSize(32, 32))
        self.btn_cups.setObjectName("btn_cups")
        self.btn_cups.clicked.connect(self.send_to_clipboard_cups)

        # Кнопка "Сделать принтер по умолчанию"
        self.btn_default = QtWidgets.QPushButton(self.tab)
        self.btn_default.setGeometry(QtCore.QRect(258, 100, 38, 40))
        self.btn_default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_default.setAccessibleName("")
        self.btn_default.setAccessibleDescription("")
        self.btn_default.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/icon_default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_default.setIcon(icon7)
        self.btn_default.setIconSize(QtCore.QSize(32, 32))
        self.btn_default.setObjectName("btn_default")
        self.btn_default.clicked.connect(self.send_to_clipboard_default)

        # Кнопка "Переименовать АРМ"
        self.btn_rename = QtWidgets.QPushButton(self.tab)
        self.btn_rename.setGeometry(QtCore.QRect(300, 100, 37, 40))
        self.btn_rename.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_rename.setAccessibleName("")
        self.btn_rename.setAccessibleDescription("")
        self.btn_rename.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/icon_rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rename.setIcon(icon8)
        self.btn_rename.setIconSize(QtCore.QSize(25, 25))
        self.btn_rename.setObjectName("btn_rename")
        self.btn_rename.clicked.connect(self.send_to_clipboard_rename)

        # Кнопка "Пароль"
        self.btn_password = QtWidgets.QPushButton(self.tab)
        self.btn_password.setGeometry(QtCore.QRect(342, 100, 37, 40))
        self.btn_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_password.setAccessibleName("")
        self.btn_password.setAccessibleDescription("")
        self.btn_password.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/icon_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_password.setIcon(icon9)
        self.btn_password.setIconSize(QtCore.QSize(25, 25))
        self.btn_password.setObjectName("btn_password")
        self.btn_password.clicked.connect(self.send_to_clipboard_password)

        # Вкладка "Сканирование (HP)"
        self.Main.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_scan_hp = QtWidgets.QLabel(self.tab_2)
        self.label_scan_hp.setGeometry(QtCore.QRect(10, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_scan_hp.setFont(font)
        self.label_scan_hp.setObjectName("label_scan_hp")
        self.line_scan_hp = QtWidgets.QFrame(self.tab_2)
        self.line_scan_hp.setGeometry(QtCore.QRect(10, 30, 401, 21))
        self.line_scan_hp.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_scan_hp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_scan_hp.setObjectName("line_scan_hp")

        # Кнопка "Настроить по hostname"
        self.btn_copy_hostname = QtWidgets.QPushButton(self.tab_2)
        self.btn_copy_hostname.setGeometry(QtCore.QRect(180, 110, 24, 24))
        self.btn_copy_hostname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_hostname.setText("")
        self.btn_copy_hostname.setIcon(icon)
        self.btn_copy_hostname.setObjectName("btn_copy_hostname")
        self.btn_copy_hostname.clicked.connect(self.send_to_clipboard_hostname)

        # Кнопка "Настроить по IP"
        self.btn_copy_ip = QtWidgets.QPushButton(self.tab_2)
        self.btn_copy_ip.setGeometry(QtCore.QRect(180, 150, 24, 24))
        self.btn_copy_ip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_ip.setText("")
        self.btn_copy_ip.setIcon(icon)
        self.btn_copy_ip.setObjectName("btn_copy_ip")
        self.btn_copy_ip.clicked.connect(self.send_to_clipboard_ip_arm)

        # Кнопка "Очистить все"
        self.btn_clear_all = QtWidgets.QPushButton(self.tab_2)
        self.btn_clear_all.setGeometry(QtCore.QRect(150, 67, 24, 24))
        self.btn_clear_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_all.setText("")
        self.btn_clear_all.setIcon(icon1)
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.btn_clear_all.clicked.connect(self.clear_all_scan)

        # Кнопка "Очистить hostname"
        self.btn_clear_hostname = QtWidgets.QPushButton(self.tab_2)
        self.btn_clear_hostname.setGeometry(QtCore.QRect(151, 110, 24, 24))
        self.btn_clear_hostname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_hostname.setText("")
        self.btn_clear_hostname.setIcon(icon1)
        self.btn_clear_hostname.setObjectName("btn_clear_hostname")
        self.btn_clear_hostname.clicked.connect(self.clear_hostname_hp)

        # Кнопка "Очистить IP"
        self.btn_clear_ip_scan_hp = QtWidgets.QPushButton(self.tab_2)
        self.btn_clear_ip_scan_hp.setGeometry(QtCore.QRect(151, 150, 24, 24))
        self.btn_clear_ip_scan_hp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_ip_scan_hp.setText("")
        self.btn_clear_ip_scan_hp.setIcon(icon1)
        self.btn_clear_ip_scan_hp.setObjectName("btn_clear_ip_scan_hp")
        self.btn_clear_ip_scan_hp.clicked.connect(self.clear_ip_hp)

        self.lineEdit_ip_arm = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ip_arm.setGeometry(QtCore.QRect(11, 152, 131, 22))
        self.lineEdit_ip_arm.setObjectName("lineEdit_ip_arm")
        self.lineEdit_login = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_login.setGeometry(QtCore.QRect(11, 67, 131, 22))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lbl_hostname = QtWidgets.QLabel(self.tab_2)
        self.lbl_hostname.setGeometry(QtCore.QRect(13, 92, 105, 16))
        self.lbl_hostname.setObjectName("lbl_hostname")
        self.lbl_ip_arm = QtWidgets.QLabel(self.tab_2)
        self.lbl_ip_arm.setGeometry(QtCore.QRect(13, 134, 71, 16))
        self.lbl_ip_arm.setObjectName("lbl_ip_arm")
        self.lbl_login = QtWidgets.QLabel(self.tab_2)
        self.lbl_login.setGeometry(QtCore.QRect(13, 48, 97, 16))
        self.lbl_login.setObjectName("lbl_login")
        self.lineEdit_hostname = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_hostname.setGeometry(QtCore.QRect(11, 110, 131, 22))
        self.lineEdit_hostname.setObjectName("lineEdit_hostname")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(211, 67, 200, 106))
        self.textEdit.setObjectName("textEdit")
        self.Main.addTab(self.tab_2, "")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(-210, 910, 300, 200))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        Window.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(Window)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(Window)
        self.Main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Multi Tools EMIAS"))
        Window.setWindowIcon(QtGui.QIcon('emias.ico'))
        self.combo_model.setItemText(1, _translate("Window", "HP LaserJet M401"))
        self.combo_model.setItemText(2, _translate("Window", "HP LaserJet M404"))
        self.combo_model.setItemText(3, _translate("Window", "HP LaserJet M501"))
        self.combo_model.setItemText(4, _translate("Window", "HP LaserJet M425"))
        self.combo_model.setItemText(5, _translate("Window", "HP LaserJet M426"))
        self.combo_model.setItemText(6, _translate("Window", "Pantum BP5100"))
        self.combo_model.setItemText(7, _translate("Window", "Pantum BM5100"))
        self.lbl_ip.setText(_translate("Window", "IP адрес:"))
        self.lbl_model.setText(_translate("Window", "Модель:"))
        self.btn_copy.setToolTip(_translate("Window", "Копировать в буфер"))
        self.btn_clear_ip.setToolTip(_translate("Window", "Очистить поле"))
        self.lbl_print.setText(_translate("Window", "<html><head/><body><p><span style=\" font-weight:600;\">Печать</span></p></body></html>"))
        self.lineEdit_cnt.setToolTip(_translate("Window", "Номер принтера"))
        self.btn_claer_spooler.setToolTip(_translate("Window", "Очистить очередь печати"))
        self.btn_test_page.setToolTip(_translate("Window", "Тестовая страница"))
        self.btn_del_printer.setToolTip(_translate("Window", "Удалить принтер"))
        self.btn_reboot.setToolTip(_translate("Window", "Перезагрузка АРМ"))
        self.btn_cups.setToolTip(_translate("Window", "Перезагрузить службы CUPS"))
        self.btn_default.setToolTip(_translate("Window", "Сделать принтер по умолчнию"))
        self.btn_rename.setToolTip(_translate("Window", "Периеименовать hostname АРМ"))
        self.btn_password.setToolTip(_translate("Window", "Пароль (o123456O)"))
        self.Main.setTabText(self.Main.indexOf(self.tab), _translate("Window", "Печать"))
        self.label_scan_hp.setText(_translate("Window", "<html><head/><body><p><span style=\" font-weight:600;\">Сканирование</span></p></body></html>"))
        self.btn_copy_hostname.setToolTip(_translate("Window", "Копировать в буфер"))
        self.btn_copy_ip.setToolTip(_translate("Window", "Копировать в буфер"))
        self.btn_clear_all.setToolTip(_translate("Window", "Очистить все поля"))
        self.btn_clear_hostname.setToolTip(_translate("Window", "Очистить поле"))
        self.btn_clear_ip_scan_hp.setToolTip(_translate("Window", "Очистить поле"))
        self.lbl_hostname.setText(_translate("Window", "Имя (hostname) АРМ:"))
        self.lbl_ip_arm.setText(_translate("Window", "IP адрес АРМ:"))
        self.lbl_login.setText(_translate("Window", "Имя пользователя:"))
        self.Main.setTabText(self.Main.indexOf(self.tab_2), _translate("Window", "Сканирование (HP)"))
        self.actionExit.setText(_translate("Window", "Exit"))

    def send_to_clipboard_printer(self):
        ip = self.lineEdit_ip.text().replace(" ", "")
        drivers = {
            "HP-LaserJet-M425": "/opt/Printer_Drivers/Ochered/4-ya ochered/HP-LaserJet-400-MFP-M425.ppd",
            "HP-LaserJet-M426": "/opt/Printer_Drivers/Ochered/4-ya ochered/HP-LaserJet-400-MFP-M425.ppd",
            "HP-LaserJet-M401": "/opt/Printer_Drivers/Ochered/4-ya ochered/HP-LaserJet-400-M401.ppd",
            "HP-LaserJet-M404": "/opt/Printer_Drivers/Ochered/4-ya ochered/HP-LaserJet-400-M401.ppd",
            "HP-LaserJet-M501": "/opt/Printer_Drivers/Ochered/4-ya ochered/HP-LaserJet-400-M401.ppd",
            "BP5100": "/home/admin/PANTUM_5100.ppd",
            "BM5100": "/home/admin/PANTUM_5100.ppd"
        }
        cnt = ''
        if self.lineEdit_cnt.text() != '':
            cnt = '-' + self.lineEdit_cnt.text()
        models = self.combo_model.currentText().replace(' ', '-').replace('Pantum-', '')
        model = models
        ftp = "wget -nc /home/admin ftp://printer:z123456Z@srv-ftp02/13_ochered/PPD/PANTUM_5100.ppd"
        models += cnt
        if models:
            install = f"/usr/sbin/lpadmin -p '{models}' -v 'socket://{ip}:9100' -P '{drivers[model]}'"
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

    def send_to_clipboard_clear_spooler(self):
        command = "lprm -;lpstat -t"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_test_page(self):
        command = "lpr /usr/share/cups/data/default-testpage.pdf;lpstat -t"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_del_printer(self):
        command = "/usr/sbin/lpadmin -x "
        QApplication.clipboard().setText(command)

    def send_to_clipboard_reboot(self):
        command = "systemctl reboot -i"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_cups(self):
        command = "systemctl restart cups"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_default(self):
        command = "/usr/sbin/lpadmin -d "
        QApplication.clipboard().setText(command)

    def send_to_clipboard_rename(self):
        command = "hostnamectl set-hostname "
        QApplication.clipboard().setText(command)

    def send_to_clipboard_password(self):
        command = "o123456O"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_hostname(self):
        login = self.lineEdit_login.text().replace(" ", "")
        hostname = self.lineEdit_hostname.text().replace(" ", "")
        command = f"\\\{hostname}.mosgorzdrav.local\scan\{login}"
        QApplication.clipboard().setText(command)

    def send_to_clipboard_ip_arm(self):
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
