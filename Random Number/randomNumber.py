import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        guess = int(input("Guess the random number: "))
        if(guess < random_number):
            print("Sorry Guess Again. Too low")
        elif(guess > random_number):
            print("Sorry guess again. Too high")
    print(f"You have guessed the correct random number: {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low != high):
            guess = random.randint(low, high)
        else:
            guess = low 
        
        feedback = input(f'Is {guess} too High(H), too Low(L) or Correct(C): ').lower()
        if(feedback == 'h'):
            high = guess - 1
        elif(feedback == 'l'):
            low = guess + 1
    
    print(f"Yay, you have guessed the correct Number: {guess}")

computer_guess(100)

# guess(10)