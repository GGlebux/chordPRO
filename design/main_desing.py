# Form implementation generated from reading ui file '/home/gglebux/PycharmProjects/chordPRO/design/main_desing.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 552)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-image: url(\"../resources/img.png\"); /* Замените на путь к вашей картинке */\n"
"    background-repeat: no-repeat; /* Повторять картинку или нет */\n"
"    background-position: center; /* Позиционирование картинки */\n"
"  }")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(parent=self.splitter)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.id_box = QtWidgets.QSpinBox(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id_box.sizePolicy().hasHeightForWidth())
        self.id_box.setSizePolicy(sizePolicy)
        self.id_box.setMinimum(1)
        self.id_box.setMaximum(5000)
        self.id_box.setObjectName("id_box")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.splitter_3 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(parent=self.splitter_3)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.note_box = QtWidgets.QComboBox(parent=self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_box.sizePolicy().hasHeightForWidth())
        self.note_box.setSizePolicy(sizePolicy)
        self.note_box.setEditable(False)
        self.note_box.setObjectName("note_box")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.note_box.addItem("")
        self.horizontalLayout_2.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtWidgets.QLabel(parent=self.splitter_4)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.type_box = QtWidgets.QComboBox(parent=self.splitter_4)
        self.type_box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_box.sizePolicy().hasHeightForWidth())
        self.type_box.setSizePolicy(sizePolicy)
        self.type_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.type_box.setEditable(True)
        self.type_box.setCurrentText("13")
        self.type_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.type_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.type_box.setPlaceholderText("")
        self.type_box.setModelColumn(0)
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.horizontalLayout_2.addWidget(self.splitter_4)
        self.splitter_5 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_4 = QtWidgets.QLabel(parent=self.splitter_5)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.diff_box = QtWidgets.QComboBox(parent=self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diff_box.sizePolicy().hasHeightForWidth())
        self.diff_box.setSizePolicy(sizePolicy)
        self.diff_box.setEditable(False)
        self.diff_box.setObjectName("diff_box")
        self.diff_box.addItem("")
        self.diff_box.addItem("")
        self.diff_box.addItem("")
        self.horizontalLayout_2.addWidget(self.splitter_5)
        self.splitter_6 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_6.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_5 = QtWidgets.QLabel(parent=self.splitter_6)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.user_defined_box = QtWidgets.QComboBox(parent=self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_defined_box.sizePolicy().hasHeightForWidth())
        self.user_defined_box.setSizePolicy(sizePolicy)
        self.user_defined_box.setEditable(False)
        self.user_defined_box.setObjectName("user_defined_box")
        self.user_defined_box.addItem("")
        self.user_defined_box.addItem("")
        self.horizontalLayout_2.addWidget(self.splitter_6)
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.searchButton.setIconSize(QtCore.QSize(16, 16))
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QtCore.QSize(0, 200))
        self.table.setStyleSheet("/* Основные стили QTableWidget */\n"
"QTableWidget {\n"
"  background-color: transparent; /* Убираем фон таблицы */\n"
"  border: none;         /* Убираем рамку таблицы */\n"
"  selection-background-color: #a3d2e2; /* Цвет выделения */\n"
"  gridline-color: #cccccc;    /* Цвет сетки таблицы */\n"
"}\n"
"\n"
"/* Стили для ячеек */\n"
"QTableWidget::item {\n"
"  background-color: transparent; /* Прозрачный фон ячейки */\n"
"  padding: 5px;\n"
"  border-bottom: 1px solid #cccccc; /* Вертикальные разделители */\n"
"  color: white;         /* Белый текст */\n"
"}\n"
"\n"
"/* Стили для заголовков столбцов */\n"
"QTableWidget::horizontalHeader {\n"
"  background-color: #f0f0f0;\n"
"  padding: 5px;\n"
"  border-bottom: 2px solid #cccccc;\n"
"  color: black;        /* Черный текст для заголовков */\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader::section {\n"
"  background-color: #f0f0f0;\n"
"  text-align: center;\n"
"  padding: 5px;\n"
"  border: 1px solid #cccccc;\n"
"  border-bottom: 2px solid #cccccc;\n"
"  color: black;        /* Черный текст для заголовков */\n"
"}\n"
"\n"
"/* Стили для заголовков строк */\n"
"QTableWidget::verticalHeader {\n"
"  background-color: transparent; /* Прозрачный фон */\n"
"  border: none;         /* Убираем рамку */\n"
"  color: white;        /* Белый текст для заголовков строк */\n"
"}\n"
"\n"
"QTableWidget::verticalHeader::section {\n"
"  background-color: transparent; /* Прозрачный фон */\n"
"  padding: 5px;\n"
"  border: none;         /* Убираем рамку */\n"
"  color: white;        /* Белый текст для заголовков строк */\n"
"}\n"
"\n"
"/* Стили для выделенной ячейки */\n"
"QTableWidget::item:selected {\n"
"  background-color: #a3d2e2; /* Цвет выделения */\n"
"  color: black;       /* Цвет текста */\n"
"}\n"
"\n"
"/* Стили для ячеек с текстом */\n"
"QTableWidget::item:focus {\n"
"  outline: none;         /* Убираем фокус */\n"
"  border: 1px solid #cccccc;  /* Добавляем рамку при фокусе */\n"
"}")
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.table.setGridStyle(QtCore.Qt.PenStyle.DashDotDotLine)
        self.table.setWordWrap(False)
        self.table.setCornerButtonEnabled(False)
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setBold(False)
        font.setItalic(True)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setSortIndicatorShown(True)
        self.table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.table)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        self.edit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.edit_button.setObjectName("edit_button")
        self.verticalLayout.addWidget(self.edit_button)
        self.update_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setObjectName("update_button")
        self.verticalLayout.addWidget(self.update_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.view_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_button.sizePolicy().hasHeightForWidth())
        self.view_button.setSizePolicy(sizePolicy)
        self.view_button.setObjectName("view_button")
        self.verticalLayout_2.addWidget(self.view_button)
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.id_box, self.note_box)
        MainWindow.setTabOrder(self.note_box, self.type_box)
        MainWindow.setTabOrder(self.type_box, self.diff_box)
        MainWindow.setTabOrder(self.diff_box, self.user_defined_box)
        MainWindow.setTabOrder(self.user_defined_box, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.remove_button)
        MainWindow.setTabOrder(self.remove_button, self.edit_button)
        MainWindow.setTabOrder(self.edit_button, self.add_button)
        MainWindow.setTabOrder(self.add_button, self.update_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "Нота:"))
        self.note_box.setItemText(0, _translate("MainWindow", "A#"))
        self.note_box.setItemText(1, _translate("MainWindow", "C#"))
        self.note_box.setItemText(2, _translate("MainWindow", "D#"))
        self.note_box.setItemText(3, _translate("MainWindow", "F#"))
        self.note_box.setItemText(4, _translate("MainWindow", "G#"))
        self.note_box.setItemText(5, _translate("MainWindow", "Ab"))
        self.note_box.setItemText(6, _translate("MainWindow", "Bb"))
        self.note_box.setItemText(7, _translate("MainWindow", "Cb"))
        self.note_box.setItemText(8, _translate("MainWindow", "Db"))
        self.note_box.setItemText(9, _translate("MainWindow", "Eb"))
        self.note_box.setItemText(10, _translate("MainWindow", "Gb"))
        self.note_box.setItemText(11, _translate("MainWindow", "A"))
        self.note_box.setItemText(12, _translate("MainWindow", "B"))
        self.note_box.setItemText(13, _translate("MainWindow", "C"))
        self.note_box.setItemText(14, _translate("MainWindow", "D"))
        self.note_box.setItemText(15, _translate("MainWindow", "E"))
        self.note_box.setItemText(16, _translate("MainWindow", "F"))
        self.note_box.setItemText(17, _translate("MainWindow", "G"))
        self.label_3.setText(_translate("MainWindow", "Тип:"))
        self.type_box.setItemText(0, _translate("MainWindow", "13"))
        self.type_box.setItemText(1, _translate("MainWindow", "7(#9)"))
        self.type_box.setItemText(2, _translate("MainWindow", "9"))
        self.type_box.setItemText(3, _translate("MainWindow", "9b5"))
        self.type_box.setItemText(4, _translate("MainWindow", "7"))
        self.type_box.setItemText(5, _translate("MainWindow", "dim7"))
        self.type_box.setItemText(6, _translate("MainWindow", "aug"))
        self.type_box.setItemText(7, _translate("MainWindow", "maj"))
        self.type_box.setItemText(8, _translate("MainWindow", "11"))
        self.type_box.setItemText(9, _translate("MainWindow", "maj9"))
        self.type_box.setItemText(10, _translate("MainWindow", "m"))
        self.type_box.setItemText(11, _translate("MainWindow", "7b5"))
        self.type_box.setItemText(12, _translate("MainWindow", "m7"))
        self.type_box.setItemText(13, _translate("MainWindow", "dim"))
        self.type_box.setItemText(14, _translate("MainWindow", "6"))
        self.type_box.setItemText(15, _translate("MainWindow", "7(#5)"))
        self.type_box.setItemText(16, _translate("MainWindow", "7sus4"))
        self.type_box.setItemText(17, _translate("MainWindow", "maj7"))
        self.type_box.setItemText(18, _translate("MainWindow", "5"))
        self.type_box.setItemText(19, _translate("MainWindow", "m6"))
        self.type_box.setItemText(20, _translate("MainWindow", "7(b9)"))
        self.type_box.setItemText(21, _translate("MainWindow", "m9"))
        self.type_box.setItemText(22, _translate("MainWindow", "sus4"))
        self.type_box.setItemText(23, _translate("MainWindow", "6-Sep"))
        self.type_box.setItemText(24, _translate("MainWindow", "m11"))
        self.type_box.setItemText(25, _translate("MainWindow", "m7b5"))
        self.type_box.setItemText(26, _translate("MainWindow", "9(#11)"))
        self.type_box.setItemText(27, _translate("MainWindow", "9(#5)"))
        self.type_box.setItemText(28, _translate("MainWindow", "7(#11)"))
        self.type_box.setItemText(29, _translate("MainWindow", "maj13"))
        self.type_box.setItemText(30, _translate("MainWindow", "6(#11)"))
        self.type_box.setItemText(31, _translate("MainWindow", "sus2"))
        self.type_box.setItemText(32, _translate("MainWindow", "m(maj7)"))
        self.type_box.setItemText(33, _translate("MainWindow", "13(b9)"))
        self.type_box.setItemText(34, _translate("MainWindow", "+(#11)"))
        self.type_box.setItemText(35, _translate("MainWindow", "13(#11)"))
        self.type_box.setItemText(36, _translate("MainWindow", "7(b13)"))
        self.type_box.setItemText(37, _translate("MainWindow", "add9"))
        self.type_box.setItemText(38, _translate("MainWindow", "13(#9)"))
        self.type_box.setItemText(39, _translate("MainWindow", "m13"))
        self.type_box.setItemText(40, _translate("MainWindow", "m6/9"))
        self.type_box.setItemText(41, _translate("MainWindow", "m(maj9)"))
        self.label_4.setText(_translate("MainWindow", "Сложность:"))
        self.diff_box.setItemText(0, _translate("MainWindow", "beginner"))
        self.diff_box.setItemText(1, _translate("MainWindow", "intermediate"))
        self.diff_box.setItemText(2, _translate("MainWindow", "advanced"))
        self.label_5.setText(_translate("MainWindow", "Добавленный:"))
        self.user_defined_box.setItemText(0, _translate("MainWindow", "Yes"))
        self.user_defined_box.setItemText(1, _translate("MainWindow", "No"))
        self.searchButton.setText(_translate("MainWindow", "🔎"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Нота"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Аппликатура"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Структура"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сложность"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Добавленный"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.remove_button.setText(_translate("MainWindow", "Удалить"))
        self.edit_button.setText(_translate("MainWindow", "Изменить"))
        self.update_button.setText(_translate("MainWindow", "Обновить"))
        self.view_button.setText(_translate("MainWindow", "Отобразить"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
