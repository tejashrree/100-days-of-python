import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
names = ['Rock', 'Paper', 'Scissors']
player_score = 0
computer_score = 0

print("🎮 Welcome to Rock Paper Scissors Game!")

while True:
    print("\nWhat do you choose?")
    print("0 - Rock\n1 - Paper\n2 - Scissors\nq - Quit")

    user_input = input("Enter your choice: ")

    if user_input.lower() == 'q':
        print(f"\n👋 Final Score:\nYou: {player_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_input not in ['0', '1', '2']:
        print("⚠️ Invalid input! Try again.")
        continue

    user_choice = int(user_input)
    comp_choice = random.randint(0, 2)

    print("\nYou chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[comp_choice])

    if user_choice == comp_choice:
        print("😐 It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

    print(f"📊 Score -> You: {player_score} | Computer: {computer_score}")
