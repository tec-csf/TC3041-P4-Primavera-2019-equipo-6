#!/usr/bin/env python
FILEPATH        = 'iot_garden_dataset.log'
DATABASE        = 'iot_garden_database'
HOST            = 'localhost'
PORT            = 8086
USER            = 'root'
PASSWORD        = 'root'

import sys
import json
from influxdb import InfluxDBClient

# display progress bar

def display_progress(ratio):
    bar_length = 20
    block = int(round(bar_length * ratio))
    text = "\rInserting data points: [{0}] {1:.2f}%".format( "#" * block + "-" * (bar_length - block), ratio * 100)
    sys.stdout.write(text)
    sys.stdout.flush()


# create a client instance

client = InfluxDBClient(host=HOST, port=PORT, username=USER, password=PASSWORD, database=DATABASE)
client.create_database(DATABASE)


# reading and inserting the data points

with open(FILEPATH, 'r') as file:
        lines = file.readlines()
        line_count  = len(lines)     # for displaying progress
        line_number = 0              # for displaying progress   
        for line in lines:
                JSONified_line = json.loads(line)
                points = JSONified_line["points"]
                for point in points:
                        point['measurement'] = point.pop('name')
                client.write_points(points)
                line_number += 1     # for displaying progress
                display_progress(float(line_number) / float(line_count))    # for displaying progress
                
client.close()

sys.stdout.write("\rDone!\r")