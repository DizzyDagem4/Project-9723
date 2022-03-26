import random
print("Number guessing game! Guess the right number and you win! (1-9)")
number = random.randint(1,9)
chances = 0 
print("Guess a number between 1-9")
while chances < 5 : 
    guess = int(input("Enter your guess:"))
    if(guess == number):
        print("Congrats you won!!")
        break
    elif(guess > number):
        print("Your guess was too high try a number lower than",guess)
    else :   
        print("Your number was too low try a number higher than",guess) 
    chances += 1 
if(not chances < 5): 
    print("You lost :(, the number was",number)   