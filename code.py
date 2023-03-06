import RPi.GPIO as G
import time


leds = [24,25,7,8,12,16,20,21]
aux = [2,3,14,15,18,27,23,22]

G.setmode(G.BCM)

G.setup(leds, G.OUT)
G.setup(aux, G.IN)

G.output(leds,1)
time.sleep(2)

while True:
    for i in range(8):
        G.output(leds[i], G.input(aux[i]))
        time.sleep(0.1)



    
