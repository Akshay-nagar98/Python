import random


#print(random.randint(1000,9999)
#print(random.choice([10,20,1,2,"tops","Python","java",Ture]))


num=random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 to 20 : "))
    if guess==num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed A Higher Number")
    elif guess<num:
        print("You Guessed A Smaller Number")
