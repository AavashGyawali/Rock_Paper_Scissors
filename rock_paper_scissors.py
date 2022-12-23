import random
enter=True
# initializing the score
score_user =0
score_computer =0
# running the loop until the user enters 'q'
while enter!='q':
    # possible inputs
    possible_action= ['rock','paper','scissors']
    # input to the user
    user_action1= input("Enter 'rock','paper'or'scissors' ")
    user_action= user_action1.lower()
    # condition if user gives incorrect input
    if user_action not in possible_action:
        print ("you did not typed correctly")
        continue
    # generating random input by computer
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
    
# Final score
print(f"Your score is {score_user} \n Computer's score is {score_computer} ")

