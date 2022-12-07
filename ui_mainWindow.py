# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1087, 465)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.groupBox_3 = QGroupBox(self.tab_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 0, 176, 319))
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.originY_spinBox = QSpinBox(self.groupBox_3)
        self.originY_spinBox.setObjectName(u"originY_spinBox")
        self.originY_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.originY_spinBox, 2, 1, 1, 2)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 4, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_3)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_5.addWidget(self.red_spinBox, 6, 1, 1, 2)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 7, 0, 1, 1)

        self.destX_spinBox = QSpinBox(self.groupBox_3)
        self.destX_spinBox.setObjectName(u"destX_spinBox")
        self.destX_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.destX_spinBox, 3, 1, 1, 2)

        self.originX_spinBox = QSpinBox(self.groupBox_3)
        self.originX_spinBox.setObjectName(u"originX_spinBox")
        self.originX_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.originX_spinBox, 1, 1, 1, 2)

        self.blue_spinBox = QSpinBox(self.groupBox_3)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_5.addWidget(self.blue_spinBox, 8, 1, 1, 2)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 5, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox_3)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_5.addWidget(self.id_lineEdit, 0, 1, 1, 2)

        self.green_spinBox = QSpinBox(self.groupBox_3)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_5.addWidget(self.green_spinBox, 7, 1, 1, 2)

        self.addEnd_pushButton = QPushButton(self.groupBox_3)
        self.addEnd_pushButton.setObjectName(u"addEnd_pushButton")

        self.gridLayout_5.addWidget(self.addEnd_pushButton, 9, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 8, 0, 1, 1)

        self.originX_label_5 = QLabel(self.groupBox_3)
        self.originX_label_5.setObjectName(u"originX_label_5")

        self.gridLayout_5.addWidget(self.originX_label_5, 0, 0, 1, 1)

        self.destY_spinBox = QSpinBox(self.groupBox_3)
        self.destY_spinBox.setObjectName(u"destY_spinBox")
        self.destY_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.destY_spinBox, 4, 1, 1, 2)

        self.originX_label_6 = QLabel(self.groupBox_3)
        self.originX_label_6.setObjectName(u"originX_label_6")

        self.gridLayout_5.addWidget(self.originX_label_6, 1, 0, 1, 1)

        self.showListParticle_pushButton = QPushButton(self.groupBox_3)
        self.showListParticle_pushButton.setObjectName(u"showListParticle_pushButton")

        self.gridLayout_5.addWidget(self.showListParticle_pushButton, 10, 0, 1, 3)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_5.addWidget(self.label_20, 3, 0, 1, 1)

        self.originY_label_3 = QLabel(self.groupBox_3)
        self.originY_label_3.setObjectName(u"originY_label_3")

        self.gridLayout_5.addWidget(self.originY_label_3, 2, 0, 1, 1)

        self.addToStart_pushButton = QPushButton(self.groupBox_3)
        self.addToStart_pushButton.setObjectName(u"addToStart_pushButton")

        self.gridLayout_5.addWidget(self.addToStart_pushButton, 9, 0, 1, 2)

        self.speed_spinBox = QSpinBox(self.groupBox_3)
        self.speed_spinBox.setObjectName(u"speed_spinBox")
        self.speed_spinBox.setMaximum(99999)

        self.gridLayout_5.addWidget(self.speed_spinBox, 5, 1, 1, 2)

        self.particle_PlainText = QPlainTextEdit(self.tab_7)
        self.particle_PlainText.setObjectName(u"particle_PlainText")
        self.particle_PlainText.setGeometry(QRect(240, 0, 181, 311))
        self.idSort_pushButton = QPushButton(self.tab_7)
        self.idSort_pushButton.setObjectName(u"idSort_pushButton")
        self.idSort_pushButton.setGeometry(QRect(10, 340, 75, 23))
        self.distanceSort_pushButton = QPushButton(self.tab_7)
        self.distanceSort_pushButton.setObjectName(u"distanceSort_pushButton")
        self.distanceSort_pushButton.setGeometry(QRect(100, 340, 75, 23))
        self.speedSort_pushButton = QPushButton(self.tab_7)
        self.speedSort_pushButton.setObjectName(u"speedSort_pushButton")
        self.speedSort_pushButton.setGeometry(QRect(180, 340, 75, 23))
        self.label_21 = QLabel(self.tab_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(60, 313, 121, 20))
        self.tabWidget = QTabWidget(self.tab_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(430, 0, 621, 331))
        self.Table = QWidget()
        self.Table.setObjectName(u"Table")
        self.particle_tableWidget = QTableWidget(self.Table)
        self.particle_tableWidget.setObjectName(u"particle_tableWidget")
        self.particle_tableWidget.setGeometry(QRect(10, 50, 541, 291))
        self.search_lineEdit = QLineEdit(self.Table)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setGeometry(QRect(40, 10, 71, 21))
        self.search_pushButton = QPushButton(self.Table)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(130, 10, 101, 23))
        self.show_pushButton = QPushButton(self.Table)
        self.show_pushButton.setObjectName(u"show_pushButton")
        self.show_pushButton.setGeometry(QRect(250, 10, 101, 21))
        self.originX_label_7 = QLabel(self.Table)
        self.originX_label_7.setObjectName(u"originX_label_7")
        self.originX_label_7.setGeometry(QRect(20, 10, 21, 20))
        self.tabWidget.addTab(self.Table, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clearDraw_pushButton = QPushButton(self.tab_2)
        self.clearDraw_pushButton.setObjectName(u"clearDraw_pushButton")

        self.gridLayout_2.addWidget(self.clearDraw_pushButton, 0, 0, 1, 1)

        self.only_particles_pushButton = QPushButton(self.tab_2)
        self.only_particles_pushButton.setObjectName(u"only_particles_pushButton")

        self.gridLayout_2.addWidget(self.only_particles_pushButton, 0, 1, 1, 1)

        self.draw_pushButton = QPushButton(self.tab_2)
        self.draw_pushButton.setObjectName(u"draw_pushButton")

        self.gridLayout_2.addWidget(self.draw_pushButton, 1, 0, 1, 1)

        self.close_particle_pushButton = QPushButton(self.tab_2)
        self.close_particle_pushButton.setObjectName(u"close_particle_pushButton")

        self.gridLayout_2.addWidget(self.close_particle_pushButton, 1, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2.addTab(self.tab_7, "")

        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1087, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.addEnd_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Azul:", None))
        self.originX_label_5.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.originX_label_6.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.showListParticle_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.originY_label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.addToStart_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.idSort_pushButton.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.distanceSort_pushButton.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.speedSort_pushButton.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ORDENAR PARTICULAS", None))
        self.search_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.show_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Todo", None))
        self.originX_label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Table), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.clearDraw_pushButton.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.only_particles_pushButton.setText(QCoreApplication.translate("MainWindow", u"SOLO PARTICULAS", None))
        self.draw_pushButton.setText(QCoreApplication.translate("MainWindow", u"DIBUJAR", None))
        self.close_particle_pushButton.setText(QCoreApplication.translate("MainWindow", u"PARTICULAS MAS CERCANAS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

