import sys
from random import randint
MEASUREMENTS=['humedad', 'temperatura', 'uv']
VALUES=['%', 'Cº', 'μmol']
FILEPATH = "iot_garden_dataset.log"
DB_TIMESTAMP=1556496000
DATASET_NUMBER = 20000000

# display progress bar
def display_progress(ratio):
    bar_length = 40
    block = int(round(bar_length * ratio))
    text = "\rGenerating data: [{0}] {1:.2f}%".format( "#" * block + "-" * (bar_length - block), ratio * 100)
    sys.stdout.write(text)
    sys.stdout.flush()


#first we need to open the filepath to create the file where we will create our dataset. 
f = open(FILEPATH, "w")

#We create a database in which we will insert data. 
f.write("# DDL\n\nCREATE DATABASE iot_garden_dataset\n\n# DML\n\n# CONTEXT-DATABASE: iot_garden_dataset\n\n")


for i in range(20000000):
   f.write(MEASUREMENTS[0]+","+ "sensor=TH0F-133"+","+"marca=Antiam"+","+"unidades="+VALUES[0]+" valor="+str(randint(0, 90))+" "+str(DB_TIMESTAMP+i)+"\n")
   f.write(MEASUREMENTS[1]+","+ "sensor=TT0F-32"+","+"marca=Sobinar"+","+"unidades="+VALUES[1]+" valor="+str(randint(-10, 40))+" "+str(DB_TIMESTAMP+i)+"\n")
   f.write(MEASUREMENTS[2]+","+ "sensor=TUV0F-41"+","+"marca=Sobinar"+","+"unidades="+VALUES[2]+" valor="+str(randint(0, 15))+" "+str(DB_TIMESTAMP+i)+"\n")
   display_progress(float(i) / float(DATASET_NUMBER))    # for displaying progress