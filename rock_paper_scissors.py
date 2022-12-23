import random
enter=True
score_user =0
score_computer =0
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
            score_user = score_user + 1
        else:
            print("Paper covers rock! You lose.")
            score_computer=score_computer + 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            score_user = score_user + 1
        else:
            print("Scissors cuts paper! You lose.")
            score_computer=score_computer + 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            score_user=score_user + 1
        else:
            print("Rock smashes scissors! You lose.")
            score_computer=score_computer + 1
    enter = input("Enter q to exit else enter anything to continue \n")

print(f"Your score is {score_user} \n Computer's score is {score_computer} ")

