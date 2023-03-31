import random
import matplotlib.pyplot as plt
import numpy as np


array = []
random_number = []

# here i am just creating some random number in between 0 and 100.
# and then putting all numbers in an array named array.

for i in range(101):
    x = random.randrange(0,101)
    array.append(x)

count = 0
for i in range(101):
    c = array.count(i)
    random_number.append(c)

xpoints = np.array(0,99)
ypoints = np.array(random_number)

plt.plot(xpoints, ypoints)
plt.show()