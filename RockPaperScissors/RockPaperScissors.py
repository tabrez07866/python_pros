import random

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

# def get_user_choice():
#     choice = input("Choose (rock/paper/scissors): ").lower()
#     while choice not in ["rock", "paper", "scissors"]:
#         choice = input("Invalid input. Please choose rock, paper, or scissors: ").lower()
#     return choice


def determine_winner(user,computer):
    if user==computer:
        return "draw"
    elif(
        (user=="rock" and computer=="scissors") or
        (user=="paper" and computer=="rock") or
        (user=="scissors" and computer=="paper")
    ):
        return "user"
    else:
        return "computer"


def play():
    user_score=0
    computer_score=0

    print("🎮 Rock,Paper,Scissors Game 🎮")
    print("Type 'exit' to quit at any time")

    while True:
        user_choice=input("\n Your move (rock/paper/scissors): ").lower()
        if user_choice=="exit":
            break
        if user_choice not in ["rock","paper","scissors"]:
            print("❌ Invalid choice.Try again.")
            continue

        computer_choice=get_computer_choice()
        print(f"🖥️ Computer choice: {computer_choice}")

        winner=determine_winner(user_choice,computer_choice)

        if winner == "draw":
            print("🤝 It's a draw!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1


        print(f"📊 Score → You: {user_score} | Computer: {computer_score}")

    print("\n🏁 Final Score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 YOU WON!")
    elif user_score < computer_score:
        print("😞 Computer Won!")
    else:
        print("🤝 It's a tie!")

        

if __name__=="__main__":
    play()

