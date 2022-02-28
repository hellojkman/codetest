import sys
A, B, C, D, E = map(int,sys.stdin.readline().split())
print((A**2 + B**2 + C**2 + D**2 + E**2) % 10)