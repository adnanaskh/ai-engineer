"""def generator():
    for i in range(20):
        yield i

gen = generator()


for i in gen:
    print(next(gen))
"""


import time
import random

def live_sensor_feed():
    while True:
        temperature = random.uniform(20.0, 35.0)
        yield round(temperature, 2)
        time.sleep(1)  

sensor = live_sensor_feed()

for _ in range(3):
    print(f"Current Temp: {next(sensor)}°C")
