import base64
import os
import time
from sys import exit
 
path_name = "GeometryDash.exe"

if os.path.exists(path_name):
  print('Client-Creator v0.1')
else:
  print("Error: "+(path_name)+(" does not exist \nSolution: Make sure that "+(path_name)+" is located with the program."))
  time.sleep(3)
  exit()

original = 'http://www.boomlings.com/database'
address = input('Your server address: ')

if len(address) != 33 :
    print('Error: Number of characters does not match the original address. \nSolution: Your address must be 33 characters long.')
    time.sleep(3)
    exit()

name = input('Executable name: ')

file = open('GeometryDash.exe', 'r+b')
filedata = file.read()

original = bytes(original, "utf-8")
address = bytes(address, "utf-8")
filedata = filedata.replace(original, address)

b64_o = base64.b64encode(original)
b64_a = base64.b64encode(address)
filedata = filedata.replace(b64_o, b64_a)

with open(name + '.exe', 'w+b') as out:
    out.write(filedata)
print('Success!')
time.sleep(3)