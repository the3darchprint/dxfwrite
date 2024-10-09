import csv
import easygui

global pointlist
global original_name


points_from_original_csv=[]
points_from_csv=[]
pointlist = points_from_csv

#file = easygui.fileopenbox(filetypes=["*.csv"])
f = open("C48CPT_1.CSV", mode="r", encoding="utf-8")


#original_name = str(file)

reader = csv.reader(f, delimiter=";")
for i in range(171):
    next(reader)

data = list(reader)
start_index = None
end_index = None

for i, row in enumerate(data):
    if "m;MPa" in row:
        start_index = i

for i, row in enumerate(data):
    if "[CLASSIFICATION]" in row:
        end_index = i
        break
ezleszajolista = data[start_index:end_index]


for row in iter(ezleszajolista):
    deep=row[0]
    deepstr=str(deep)
    deepsomething="valami"+deepstr
    deepb=deepsomething.strip("valami")

    qc=row[1]
    strqc=str(qc)
    strqcomething="valami"+strqc
    value_qc=strqcomething.strip("valami")

    rf=row[8]
    strrf=str(rf)
    strqcomething="valami"+strrf
    value_rf=strqcomething.strip("valami")

    points_from_original_csv.append([deepb,value_qc, value_rf])

print(type(points_from_original_csv[0]))

points_from_csv_work = points_from_original_csv[:-1]


for i in iter(points_from_csv_work):

    deep=float(i[0])
    deepy=deep*-10

    value_qc=float(i[1])

    value=float(i[2])
    value_rf=value*5

    points_from_csv.append([deepy, value_qc, value_rf])

print(pointlist)








