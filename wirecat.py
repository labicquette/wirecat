from parser import *
import time 
timer = time.process_time()
file = "tramedns.txt"

Bytes = parser(file)

print(Bytes)
print(time.process_time()- timer)