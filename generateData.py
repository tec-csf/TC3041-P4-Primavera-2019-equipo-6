#!/usr/bin/env python
MEASUREMENTS=['humedad', 'temperatura', 'uv']
VALUES=['%', 'Cº', 'μmol']
FILEPATH = "iot_garden_dataset.log"
DATASET_NUMBER = 20000000

import sys
import random
import json

# display progress bar
def display_progress(ratio):
    bar_length = 40
    block = int(round(bar_length * ratio))
    text = "\rGenerating data: [{0}] {1:.2f}%".format( "#" * block + "-" * (bar_length - block), ratio * 100)
    sys.stdout.write(text)
    sys.stdout.flush()

#Generate data and write
with open(FILEPATH, 'w') as file:
    for point in range(DATASET_NUMBER):
        data = {}
        data['points'] = []
        data['points'].append({  
        'name': MEASUREMENTS[0],
        'tags': {
            'sensor': 'TH0F-133',
            'marca': 'Antiam'
        },
        'timestamp': str(1556496000+point),
        'fields': {
            'valor': random.randint(0,50)
        }})

        data['points'].append({  
        'name': MEASUREMENTS[1],
        'tags': {
            'sensor': 'TT0F-32',
            'marca': 'Sobinar'
        },
        'timestamp': str(1556496000+point),
        'fields': {
            'valor': random.randint(0,40)
        }})
        data['points'].append({  
        'name': MEASUREMENTS[2],
        'tags': {
            'sensor': 'TUV0F-41',
            'marca': 'Sobinar'
        },
        'timestamp': str(1556496000+point),
        'fields': {
            'valor': random.randint(0,11)
        }})
        json.dump(data, file)
        file.write('\n')
        display_progress(float(point) / float(DATASET_NUMBER))    # for displaying progress

sys.stdout.write("\rDone!\r")