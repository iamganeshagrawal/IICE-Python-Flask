from time import time

sT = time()
loops = 0

while time() - sT < 10:
	loops += 1

print(loops)
