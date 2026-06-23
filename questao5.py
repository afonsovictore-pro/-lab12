import random
import time

N = random.randint(2, 10)

print("Prepare-se...")

time.sleep(N)

print("AGORA!")

tempo0 = time.time()

input()

tempo1 = time.time()

print("Você levou", tempo1 - tempo0, "segundos para responder.")