import random
import time

def func(seconds):
    while seconds>0:
        print("Loading......")
        print("Please Wait")
        time.sleep(2)
        seconds=seconds-1
        break
func(5)

while True:
    A=input("Select (Rock/Papper/Scissors)=")
    print(f"User Selected {A}")
    if A=="Rock" or A=="Papper" or A=="Scissors":
        break
    else:
        continue


a=["Rock","Papper","Scissors"]

b=random.choice(a)
print(f"CPU selected {b}")
if A==b:
    print("Draw")
elif (A=="Rock" and b=="Scissors") or (A=="Papper" and b=="Rock") or (A=="Scissors" and b=="Papper"):
    print("User Won")
elif (b=="Rock" and A=="Scissors") or (b=="Papper" and A=="Rock") or (b=="Scissors" and A=="Papper"):
    print("CPU Won")