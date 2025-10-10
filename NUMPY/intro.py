import numpy as np
print("SHLOK KUMAR");

temperature = [33.5, 22.5, 37, 45.6, 23.5];

total = 0

for temp in temperature:
    total += temp
avg = total / len(temperature)

print("Average Temperature is : ", avg)