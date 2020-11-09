secret = "game"
guess = ""
guess_count = 0
guess_limit = 5

i = 1

while i <= 60:
    print("x" * i)
    i += 1
print("""
                Guessing 
                 game""")
print("""
    Type help for help
        """)
while guess_count < guess_limit:
    guess = input("> ").lower()
    guess_count += 1
    if guess == secret:
        print("Correct")
        break
    elif guess_count == guess_limit:
        print("Out of guess")
    elif guess == '':
        print('Enter guess')
    elif guess == "help":
        print("""
        Type your guess
        You have Just 5 guesses
        """)
    elif guess != secret and guess_count < 5:
        print("incorrect guess")
