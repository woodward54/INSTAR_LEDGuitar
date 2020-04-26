import board
import time
import neopixel

pixels = neopixel.NeoPixel(board.D18, 244, brightness =0.1)

pixels.fill((255,0,0))
pixels.show()
time.sleep(5)
