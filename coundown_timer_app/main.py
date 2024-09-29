# Exercise 1

### Countdown Timer With ChatGPT

import time

my_time = int(input("Enter the time in seconds: "))
print(f"{my_time} seconds countdown starting...")

while my_time > 0:
    print(f"{my_time} seconds left")
    my_time -= 1
    time.sleep(1)

print("Countdown completed!")

# Exercise 2

### Countdown Timer With Bro Code

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0, -1):
    seconds = x % 60
    minitues = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minitues:02}:{seconds:02}")
    time.sleep(1)

print("Time is UP.")
