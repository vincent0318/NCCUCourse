import os, json

from fetchClass import fetchClass
from fetchTeacherId import fetchTeacherId

dir_path = os.path.dirname(os.path.realpath(__file__))

def useOldClasses():
  with open(os.path.join(dir_path, "_data", "classes.json"), "r") as f:
    return json.loads(f.read())

if not os.path.exists(os.path.join(dir_path, "_data")):
  os.makedirs(os.path.join(dir_path, "_data"))

classes = fetchClass()
TeacherId = fetchTeacherId(classes)
print(TeacherId)