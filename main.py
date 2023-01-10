import csv
import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf import zoom

import os

pointsqc=[]

pointsrf=[]

RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")

inputqc = os.path.join(RESOURCES_PATH, "qc.dxf")
inputrf = os.path.join(RESOURCES_PATH, "rf.dxf")
csvname = "input.csv"
inputfile = os.path.join(RESOURCES_PATH, csvname)

def DrawQC(file):
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in iter(reader):
            deep=float(row[0])
            deepy=deep*-10
            value_qc=float(row[1])
            pointsqc.append([value_qc, deepy])

    dwg = ezdxf.readfile(inputqc)
    msp = dwg.modelspace()
    msp.add_lwpolyline(pointsqc)
    msp.add_text(csvname, height=2).set_placement((0, 25), align=TextEntityAlignment.MIDDLE_CENTER )
    msp.add_text("magassag", height=2).set_placement((5, 5), align=TextEntityAlignment.LEFT )
    msp.add_lwpolyline([(0, 0), (0, 20)])
    msp.add_circle((0, 25), radius=5)    
    dwg.saveas("cptQC.dxf")
    

def DrawRF(file):
 
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in iter(reader):
            deep=float(row[0])
            deepy=deep*-10
            value=float(row[7])
            value_rf=value*5
            pointsrf.append([value_rf, deepy])

    dwg = ezdxf.readfile(inputrf)
    msp = dwg.modelspace()
    msp.add_lwpolyline(pointsrf)
    msp.add_text(csvname, height=2).set_placement((0, 25), align=TextEntityAlignment.CENTER )
    msp.add_text("magassag", height=2).set_placement((5, 5), align=TextEntityAlignment.LEFT )
    msp.add_lwpolyline([(0, 0), (0, 20)])
    msp.add_circle((0, 25), radius=5)
    dwg.saveas("cptRF.dxf")

DrawQC(inputfile)
DrawRF(inputfile)
    



