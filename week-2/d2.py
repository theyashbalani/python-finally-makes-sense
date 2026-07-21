###
import math
print(math.sqrt(49))

from math import ceil
print(ceil(4.2))


####
from math import pi
print(round(pi, 4))

###
import json

data = json.loads('{"hostname":"web-1","cpu":81}')
print(data["hostname"])

###
from pathlib import Path

config = Path("config.py")

###
from datetime import datetime
print(datetime.now())

###
from time import sleep
sleep(2)
print("Deployment Complete")

###
from os import getcwd
print(getcwd())

###
from health import cpu_ok
status = cpu_ok(80)
print(status)
print(type(status))

###
from automation import aws


###
import json

def load_server(json_text):
    data = json.loads(json_text)
    return data

print(load_server('{"hostname":"web-1","cpu":81}'))
