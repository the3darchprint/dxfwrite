import csv
import ezdxf
import os

points=[]
RESOURCES_PATH = os.path.dirname(__file__)

with open(f'{RESOURCES_PATH}//input.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in iter(reader):
        deep=float(row[0])
        deepy=deep*-10
        value=float(row[1])
        points.append([value, deepy])

dwg = ezdxf.readfile(f'{RESOURCES_PATH}//qc.dxf')
msp = dwg.modelspace()
msp.add_lwpolyline(points)
dwg.saveas("cpt.dxf")