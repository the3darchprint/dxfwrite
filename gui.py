# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import csv
import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf import zoom
import easygui

RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")

inputpic = os.path.join(RESOURCES_PATH, "picture.jpg")
inputqc = os.path.join(RESOURCES_PATH, "qc.dxf")
inputrf = os.path.join(RESOURCES_PATH, "rf.dxf")

pointlist=[]

original_name = "placeholder"


class Ui_CPT_CSV_TO_DXF(object):
    def setupUi(self, CPT_CSV_TO_DXF):

                # create message window
        self.message_box = QMessageBox()
        self.message_box.setIcon(QMessageBox.Critical)
        self.message_box.setWindowTitle("Error")


        CPT_CSV_TO_DXF.setObjectName("CPT_CSV_TO_DXF")
        CPT_CSV_TO_DXF.resize(722, 827)
        self.horizontalLayout = QtWidgets.QHBoxLayout(CPT_CSV_TO_DXF)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.import_csv_bttn = QtWidgets.QPushButton(CPT_CSV_TO_DXF)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.import_csv_bttn.setFont(font)
        self.import_csv_bttn.setObjectName("import_csv_bttn")

        self.import_csv_bttn.clicked.connect(self.import_csv)

        self.verticalLayout.addWidget(self.import_csv_bttn)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.name_label = QtWidgets.QLabel(CPT_CSV_TO_DXF)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_4.addWidget(self.name_label)
        self.name_field_lineedit = QtWidgets.QLineEdit(CPT_CSV_TO_DXF)
        self.name_field_lineedit.setObjectName("name_field_lineedit")

        self.horizontalLayout_4.addWidget(self.name_field_lineedit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.height_label = QtWidgets.QLabel(CPT_CSV_TO_DXF)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.height_label.setFont(font)
        self.height_label.setObjectName("height_label")
        self.horizontalLayout_5.addWidget(self.height_label)
        self.height_field_lineedit = QtWidgets.QLineEdit(CPT_CSV_TO_DXF)
        self.height_field_lineedit.setObjectName("height_field_lineedit")

        self.horizontalLayout_5.addWidget(self.height_field_lineedit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.frame_3 = QtWidgets.QFrame(CPT_CSV_TO_DXF)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.export_qc_bttn = QtWidgets.QPushButton(CPT_CSV_TO_DXF)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.export_qc_bttn.setFont(font)
        self.export_qc_bttn.setObjectName("export_qc_bttn")

        self.export_qc_bttn.clicked.connect(self.export_qc)

        self.verticalLayout.addWidget(self.export_qc_bttn)
        self.frame_2 = QtWidgets.QFrame(CPT_CSV_TO_DXF)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.export_rf_bttn = QtWidgets.QPushButton(CPT_CSV_TO_DXF)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.export_rf_bttn.setFont(font)
        self.export_rf_bttn.setObjectName("export_rf_bttn")

        self.export_rf_bttn.clicked.connect(self.export_rf)

        self.verticalLayout.addWidget(self.export_rf_bttn)
        self.frame_4 = QtWidgets.QFrame(CPT_CSV_TO_DXF)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.Picture_label = QtWidgets.QLabel(CPT_CSV_TO_DXF)
        self.Picture_label.setText("")
        self.Picture_label.setPixmap(QtGui.QPixmap(inputpic))
        self.Picture_label.setObjectName("Picture_label")
        self.horizontalLayout_2.addWidget(self.Picture_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(CPT_CSV_TO_DXF)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CPT_CSV_TO_DXF)
        QtCore.QMetaObject.connectSlotsByName(CPT_CSV_TO_DXF)

    def retranslateUi(self, CPT_CSV_TO_DXF):
        _translate = QtCore.QCoreApplication.translate
        CPT_CSV_TO_DXF.setWindowTitle(_translate("CPT_CSV_TO_DXF", "Dialog"))
        self.import_csv_bttn.setText(_translate("CPT_CSV_TO_DXF", "CSV file beolvasása"))
        self.name_label.setText(_translate("CPT_CSV_TO_DXF", "Feltárás neve:"))
        self.height_label.setText(_translate("CPT_CSV_TO_DXF", "Feltárás magassága:"))
        self.export_qc_bttn.setText(_translate("CPT_CSV_TO_DXF", "qc görbe rajzolása"))
        self.export_rf_bttn.setText(_translate("CPT_CSV_TO_DXF", "Rf görbe rajzolása"))

    

    def import_csv(self):
        global pointlist
        global original_name


        points_from_csv=[]

        pointlist = points_from_csv

        file = easygui.fileopenbox(filetypes=["*.csv"])
        f = open(file, mode="r")
        original_name = str(file)
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in iter(reader):
            deep=float(row[0])
            deepy=deep*-10
            value=float(row[7])
            value_rf=value*5
            value_qc=float(row[1])
            points_from_csv.append([deepy, value_rf, value_qc])


        self.name_field_lineedit.setText("nev")
        

    def export_qc(self):


        name=self.name_field_lineedit.text()
        if not self.height_field_lineedit.text():
            name = original_name    
    
        filename= (str(name))+"_Qc"+".dxf"
                      
        heightm=self.height_field_lineedit.text()

        if not self.height_field_lineedit.text():
            heightm = "-- m"
     
        fileoutput = easygui.filesavebox(default=filename)
        
        pointsqc=[]
        
        for i in pointlist:
            deepy=i[0]
            value_qc=i[2]
            pointsqc.append([value_qc, deepy])


        dwg = ezdxf.readfile(inputqc)
        msp = dwg.modelspace()
        msp.add_lwpolyline(pointsqc)
        msp.add_text(name, height=2).set_placement((0, 25), align=TextEntityAlignment.MIDDLE_CENTER )
        msp.add_text(heightm, height=2).set_placement((5, 5), align=TextEntityAlignment.LEFT )
        msp.add_lwpolyline([(0, 0), (0, 20)])
        msp.add_circle((0, 25), radius=5)    
        dwg.saveas(fileoutput)


    def export_rf(self):
 

        name=self.name_field_lineedit.text()
        if not self.height_field_lineedit.text():
            name = original_name    
    
        filename= (str(name))+"_Rf"+".dxf"
                      
        heightm=self.height_field_lineedit.text()

        if not self.height_field_lineedit.text():
            heightm = "-- m"
     
        fileoutput = easygui.filesavebox(default=filename)       


        pointsrf=[]
        
        for i in pointlist:
            deepy=i[0]
            value_rf=i[1]
            pointsrf.append([value_rf, deepy])



        dwg = ezdxf.readfile(inputrf)
        msp = dwg.modelspace()
        msp.add_lwpolyline(pointsrf)
        msp.add_text(name, height=2).set_placement((0, 25), align=TextEntityAlignment.MIDDLE_CENTER )
        msp.add_text(heightm, height=2).set_placement((5, 5), align=TextEntityAlignment.LEFT )
        msp.add_lwpolyline([(0, 0), (0, 20)])
        msp.add_circle((0, 25), radius=5)    
        dwg.saveas(fileoutput)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CPT_CSV_TO_DXF = QtWidgets.QDialog()
    ui = Ui_CPT_CSV_TO_DXF()
    ui.setupUi(CPT_CSV_TO_DXF)
    CPT_CSV_TO_DXF.show()
    sys.exit(app.exec_())
