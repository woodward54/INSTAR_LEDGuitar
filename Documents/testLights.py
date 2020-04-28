import board
import neopixel
import time
import signal
import sys
#from matrixData import * 
import importlib

import sys
if len(sys.argv) != 3:
  print("error on args")
  exit
else:
  speed = int(sys.argv[2])
  module = str(sys.argv[1])
  try:
    m1 = importlib.import_module(module)
  except ImportError as err:
    print("ERROR ON IMPORT")
    exit

NUM_ROWS = 7
NUM_COLS = 16

#define a list of valid pixels (note this is longer but it is required to be addressable)
pixels = neopixel.NeoPixel(board.D18, 244, brightness =0.1, auto_write = False)

#matrix of actual addressable pixels 
maskMatrix = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 
[-1,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16],
[-1,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45],
[-1,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46],
[-1,-1,61,62,63,64,65,66,67,68,69,70,71,72,73,-1],
[-1,-1,85,84,83,82,81,80,79,78,77,76,75,74,-1,-1],
[-1,-1,86,87,88,89,90,91,92,93,94,95,96,97,-1,-1]]

#start all off
#print("test")
#pixels.fill((0,255,0))

frames = len(m1.ledarray)/7

while True:
  for frame in range(0,int(frames)):
    for led_pos in range(0, 112):
      row = int(led_pos / NUM_COLS)
      col = int(led_pos % NUM_COLS)

      if maskMatrix[row][col] != -1:
        idx = maskMatrix[row][col]

        colorHex = m1.ledarray[row+(7*frame)][col]

        b = colorHex % 256
        g = int( ((colorHex-b)/256) % 256 )      # always an integer
        r = int( ((colorHex-b)/256**2) - g/256 ) # ditto

        pixels[idx] = (r,g,b)
    pixels.show()
    time.sleep(1/speed)
    print ("TEST")

