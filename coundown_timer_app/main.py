import time

my_time = int(input("Enter the time in seconds: "))
print(f"{my_time} seconds countdown starting...")

while my_time > 0:
    print(f"{my_time} seconds left")
    my_time -= 1
    time.sleep(1)

print("Countdown completed!")
