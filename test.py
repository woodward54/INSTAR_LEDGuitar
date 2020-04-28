import board
import time
import neopixel

# was 244
print("Setting")
pixels = neopixel.NeoPixel(board.D18, 10, brightness=0.4)

print("filling...")

while (1):
    pixels.fill((255,0,0))
    print("show")
    pixels.show()
    time.sleep(1)

print("sleep")
time.sleep(5)
