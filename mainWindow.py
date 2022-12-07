from PySide2.QtWidgets import QMainWindow, QFileDialog ,QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor
from ui_mainWindow import Ui_MainWindow
from PySide2.QtCore import Slot
from particle import Particle, Point
from particle_list import  Particle_List
from algorithms import *

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.myPoints = []
        self.particle_list = Particle_List()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addToStart_pushButton.clicked.connect(self.click_addStart)
        self.ui.addEnd_pushButton.clicked.connect(self.click_addEnd)
        self.ui.showListParticle_pushButton.clicked.connect(self.click_show)
        self.ui.actionAbrir.triggered.connect(self.action_abrir)
        self.ui.actionGuardar.triggered.connect(self.action_guardar)
        self.ui.search_pushButton.clicked.connect(self.search_tableParticle)
        self.ui.show_pushButton.clicked.connect(self.show_tableParticle)
        self.ui.draw_pushButton.clicked.connect(self.draw_particle)
        self.ui.clearDraw_pushButton.clicked.connect(self.clear_draws)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.idSort_pushButton.clicked.connect(self.sort_by_id)
        self.ui.distanceSort_pushButton.clicked.connect(self.sort_by_distance)
        self.ui.speedSort_pushButton.clicked.connect(self.sort_by_speed)
        self.ui.close_particle_pushButton.clicked.connect(self.get_points_particles)
        self.ui.only_particles_pushButton.clicked.connect(self.draw_points)


    def wheelEvent(self, event):
        if (event.delta() > 0):
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def search_tableParticle(self):
        id = self.ui.search_lineEdit.text()
        encontrado = False
        for particle in self.particle_list:
            print(id)
            print(particle.id)
            if(id == str(particle.id)):
                self.ui.particle_tableWidget.clear()
                headers = [ "ID", "Origen X","Origen Y","Destino X",
                    "Destino Y", "Velocidad","Rojo", "Verde", "Azul",
                    "Distancia"]
                self.ui.particle_tableWidget.setHorizontalHeaderLabels(headers)
                self.ui.particle_tableWidget.setRowCount(1)

                id_widget = QTableWidgetItem(str(particle.id))
                origen_x_widget = QTableWidgetItem(str(particle.origen_x))
                origen_y_widget = QTableWidgetItem(str(particle.origen_y))
                destino_x_widget = QTableWidgetItem(str(particle.destino_x))
                destino_y_widget = QTableWidgetItem(str(particle.destino_y))
                velocidad_widget = QTableWidgetItem(str(particle.velocidad))
                red_widget = QTableWidgetItem(str(particle.red))
                green_widget = QTableWidgetItem(str(particle.green))
                blue_widget = QTableWidgetItem(str(particle.blue))
                distance_widget = QTableWidgetItem(str(particle.distancia))

                self.ui.particle_tableWidget.setItem(0, 0, id_widget)
                self.ui.particle_tableWidget.setItem(0, 1, origen_x_widget)
                self.ui.particle_tableWidget.setItem(0, 2, origen_y_widget)
                self.ui.particle_tableWidget.setItem(0, 3, destino_x_widget)
                self.ui.particle_tableWidget.setItem(0, 4, destino_y_widget)
                self.ui.particle_tableWidget.setItem(0, 5, velocidad_widget)
                self.ui.particle_tableWidget.setItem(0, 6, red_widget)
                self.ui.particle_tableWidget.setItem(0, 7, green_widget)
                self.ui.particle_tableWidget.setItem(0, 8, blue_widget)
                self.ui.particle_tableWidget.setItem(0, 9, distance_widget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self, "Atencion",
                'La particula con el id ' + id + ' no fue encontrado...'
            )
    
    @Slot()
    def sort_by_id(self):
        self.particle_list.sort_byId()
        self.click_show()
        self.show_tableParticle()

    @Slot()
    def sort_by_distance(self):
        self.particle_list.sort_byDistance()
        self.click_show()
        self.show_tableParticle()
    
    @Slot()
    def sort_by_speed(self):
        self.particle_list.sort_bySpeed()
        self.click_show()
        self.show_tableParticle()

    @Slot()
    def show_tableParticle(self):
        self.ui.particle_tableWidget.setColumnCount(10)
        headers = [ "ID", "Origen X","Origen Y","Destino X",
            "Destino Y", "Velocidad","Rojo", "Verde", "Azul",
            "Distancia"]
        self.ui.particle_tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.particle_tableWidget.setRowCount(len(self.particle_list))

        row = 0
        for particle in self.particle_list:
            id_widget = QTableWidgetItem(str(particle.id))
            origen_x_widget = QTableWidgetItem(str(particle.origen_x))
            origen_y_widget = QTableWidgetItem(str(particle.origen_y))
            destino_x_widget = QTableWidgetItem(str(particle.destino_x))
            destino_y_widget = QTableWidgetItem(str(particle.destino_y))
            velocidad_widget = QTableWidgetItem(str(particle.velocidad))
            red_widget = QTableWidgetItem(str(particle.red))
            green_widget = QTableWidgetItem(str(particle.green))
            blue_widget = QTableWidgetItem(str(particle.blue))
            distance_widget = QTableWidgetItem(str(particle.distancia))

            self.ui.particle_tableWidget.setItem(row, 0, id_widget)
            self.ui.particle_tableWidget.setItem(row, 1, origen_x_widget)
            self.ui.particle_tableWidget.setItem(row, 2, origen_y_widget)
            self.ui.particle_tableWidget.setItem(row, 3, destino_x_widget)
            self.ui.particle_tableWidget.setItem(row, 4, destino_y_widget)
            self.ui.particle_tableWidget.setItem(row, 5, velocidad_widget)
            self.ui.particle_tableWidget.setItem(row, 6, red_widget)
            self.ui.particle_tableWidget.setItem(row, 7, green_widget)
            self.ui.particle_tableWidget.setItem(row, 8, blue_widget)
            self.ui.particle_tableWidget.setItem(row, 9, distance_widget)

            row += 1
    @Slot()
    def action_abrir(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        ) [0]
        if(self.particle_list.abrir(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo" + ubicacion
            )
    @Slot()
    def action_guardar(self):

        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        ) [0]
        if(self.particle_list.guardar(ubicacion)):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )
    @Slot()
    def click_addStart(self):
        self.particle_list.addFirst(self.make_particle())
        self.reset_spinBoxs()
    @Slot()
    def click_addEnd(self):
        self.particle_list.addToEnd(self.make_particle())
        self.reset_spinBoxs()
    @Slot()
    def click_show(self):
        self.ui.particle_PlainText.clear()
        self.ui.particle_PlainText.insertPlainText(str(self.particle_list))

    def make_particle(self)->Particle:
        id = self.ui.id_lineEdit.text()
        x1 = self.ui.originX_spinBox.value()
        y1 = self.ui.originY_spinBox.value()
        x2 = self.ui.destX_spinBox.value()
        y2 = self.ui.destY_spinBox.value()
        speed = self.ui.speed_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        myParticle = Particle(id, x1, y1, x2, y2, speed, red, green, blue)
        return myParticle

    def reset_spinBoxs(self):
        id = self.ui.id_lineEdit.setText("")
        self.ui.originX_spinBox.setValue(0)
        self.ui.originY_spinBox.setValue(0)
        self.ui.destX_spinBox.setValue(0)
        self.ui.destY_spinBox.setValue(0)
        self.ui.speed_spinBox.setValue(0)
        self.ui.red_spinBox.setValue(0)
        self.ui.green_spinBox.setValue(0)
        self.ui.blue_spinBox.setValue(0)
    @Slot()
    def draw_particle(self):
        self.scene.clear()
        for part in self.particle_list:
            pen = QPen()
            pen.setWidth(2)
            color = QColor(part.red, part.green, part.blue)
            pen.setColor(color)
            self.scene.addEllipse(part.origen_x, part.origen_y, 3, 3, pen)
            self.scene.addEllipse(part.destino_x, part.destino_y, 3, 3, pen)
            self.scene.addLine(part.origen_x +2, part.origen_y+2, part.destino_x+2, part.destino_y+2, pen)

    @Slot()
    def clear_draws(self):
        self.scene.clear()

    @Slot()
    def draw_points(self):
        self.scene.clear()
        for part in self.particle_list:
            pen = QPen()
            pen.setWidth(2)
            color = QColor(part.red, part.green, part.blue)
            pen.setColor(color)
            self.scene.addEllipse(part.origen_x, part.origen_y, 3, 3, pen)
            self.scene.addEllipse(part.destino_x, part.destino_y, 3, 3, pen)


    @Slot()
    def get_points_particles(self):
        self.myPoints.clear()
        for particle in self.particle_list:
            myP = Point(particle.origen_x, particle.origen_y)
            self.myPoints.append(myP)
            myPe = Point(particle.destino_x, particle.destino_y)
            self.myPoints.append(myPe)
        self.get_points()

    def get_points(self):
        count = 0
        close = 0
        less_distance = 99999999999999
        while(len(self.myPoints) > count):
            iter = 0
            while(len(self.myPoints) > iter):
                if(count != iter):
                    actual = euclidean_distance(self.myPoints[count].point_X, self.myPoints[count].point_Y,
                    self.myPoints[iter].point_X, self.myPoints[iter].point_Y)
                    #print("Obtenida: " + actual +"\n")
                    #print("Menor actual: " + less_distance+"\n")
                    if(actual < less_distance):
                        less_distance = actual
                        close = iter
                iter+=1
            
            pen = QPen()
            pen.setWidth(2)
            self.scene.addLine(self.myPoints[count].point_X +2, self.myPoints[count].point_Y+2,
                               self.myPoints[close].point_X +2, self.myPoints[close].point_Y+2, pen)
            less_distance = 99999999999999
            count += 1

   
       
            