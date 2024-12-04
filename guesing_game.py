import random
jackpot = random.randint(1, 100)
guess = int(input("Chal guess kar:- "))
count = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("guess lower")
    guess = int(input("Chal guess kar:- "))
    count = count + 1


print("sahi jawab")
print("your attempt is", count)

   
##############Using For looping-----------------------------
# for guess in range(jackpot):
#     guess = int(input("Enter number:= "))
#     if guess == jackpot:
#         print('sahi jawab')
#         break
#     elif guess < jackpot:
#         print("enter higher;==")
#     else:
#         print("Enter lower")

