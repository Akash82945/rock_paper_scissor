import random

input_map = {
    '0':'rock','r':'rock','R':'rock','rock':'rock','Rock':'rock',
    '1':'paper','p':'paper','P':'paper','paper':'paper','Paper':'paper',
    '2':'scissor','s':'scissor','S':'scissor','scissor':'scissor','Scissor':'scissor'
}

emoji_map  = {
    'rock':'🗻 rock',
    'paper':'📄 paper',
    'scissor':'✂ scissor'
}

def get_user_choice():
    print("Choice- [0/r/R/rock/Rock] 🗻Rock|  [1/p/P/paper/Paper] 📄Paper|    [2/s/S/scissor/Scissor] ✂Scissor")
    choice = input("enter your choice: ")
    while choice not in input_map:
        print("❌Invalid Choice, Choice again..")
        choice = input("enter your choice |[0/r/R/rock/Rock] 🗻Rock|  [1/p/P/paper/Paper] 📄Paper|    [2/s/S/scissor/Scissor] ✂Scissor")
    return input_map[choice]

def get_computer_choice():
    return random.choice(['rock','paper','scissor'])

def determine_winner(user,computer):
    if user == computer:
        print("🤝it's draw.")
    elif (user == 'rock' and computer == 'scissor') or\
        (user == 'scissor' and computer == 'paper') or\
        (user == 'paper' and computer == 'rock'):
            print("🙎You win.🎉")
    else:
        print("🤖Computer win.🎉")
        
def play():
    print("🎮 -- Welcome Rock Paper Scissor Game. -- 🎮")
    while True:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        
        print(f"👉You choice:{emoji_map[user_choice]}")
        print(f"💻Computer choice:{emoji_map[computer_choice]}")
        
        result = determine_winner(user_choice,computer_choice)
        print(f"\n{result}")
        
        
        play_again = input(f"🔁Do you want to play again? (y/n):").lower
        if play_again not in ['y','yes']:
            print("👋 Thanks for playing. Good bye! Meet again. 👋")
            break
        
if __name__=="__main__":
    play()
    
