
if __name__ == "__main__":
    import sys
    sys.path.append("..")

from lib.core import *

class Interval:
    def __init__(self, min : float = infinity, max : float = infinity): # Default interval is empty
        self.min = min
        self.max = max

    def contains(self, x : float) -> bool:
        return self.min <= x <= self.max

    def surrounds(self, x : float) -> bool:
        return self.min < x and x < self.max

    def clamp(self, x : float) -> float:
        return (self.min if x < self.min 
                else self.max if x > self.max 
                else x)

    def __str__(self):
        return f"min: {self.min}, max: {self.max}"
    
    def __eq__(self, other):
        return self.min == other.min and self.max == other.max
    

# Test
if __name__ == "__main__":
    i = Interval(1, 2)
    print(f"Test 1:		{i}")
    print(f"Test 2:		{i.contains(0)}")
    print(f"Test 3:		{i.contains(1)}")
    print(f"Test 4:		{i.contains(2)}")
    print(f"Test 5:		{i.contains(3)}")
    print(f"Test 6:		{i.surrounds(0)}")
    print(f"Test 7:		{i.surrounds(1)}")
    print(f"Test 8:		{i.surrounds(2)}")
    print(f"Test 9:		{i.surrounds(3)}")
    print(f"Test 10:	{Interval()}")
    print(f"Test 11:	{Interval(1)}")
    print(f"Test 12:	{Interval(1, 2)}")
    print(f"Test 13:	{Interval(1, 2) == Interval(1, 2)}")
    print(f"Test 14:	{Interval(1, 2) == Interval(1, 3)}")
    print(f"Test 15:	{Interval(1, 2) == Interval(3, 2)}")
