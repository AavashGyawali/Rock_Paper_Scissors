import random
enter="t"
while enter!='q':
    possible_action= ['rock','paper','scissors']
    user_action1= input("Enter 'rock','paper'or'scissors' ")
    user_action= user_action1.lower()
    if user_action1 not in possible_action:
        print ("you did not typed correctly")
        continue
    computer_action =random.choice(possible_action)
    print(f"You choice is {user_action} and computer's choice is {computer_action}")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    enter = input("Enter q to exit else enter anything to continue \n")

