import os
import sys

from lib.color import Color

width = 256
height = 256

print(f"P3\n{width} {height}\n255\n")

for j in range(height):
  print(f"\rScanlines remaining: {height - j}", file=sys.stderr, end="\n")
  for i in range(width):
    c = Color(i / (width - 1), j / (height - 1), 0)
    print(f"{c}")

print(f"\nDone", file=sys.stderr, end="\n")