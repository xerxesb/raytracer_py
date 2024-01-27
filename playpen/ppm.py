import os
import sys

width = 256
height = 256

print(f"P3\n{width} {height}\n255\n")

for j in range(height):
  print(f"\rScanlines remaining: {height - j}", file=sys.stderr, end="")

  for i in range(width):
    r = i / (width - 1)
    g = j / (height - 1)
    b = 0

    print(f"{int(255.999 * r)} {int(255.999 * g)} {int(255.999 * b)}")

print(f"\rDone", file=sys.stderr, end="")