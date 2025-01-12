#ROCK,PEAPER,SCISSORS
print("rock...")
print("peaper...")
print("scissors...")
player1=input("enter your movement:")
player2=input("enter your movement:")
if player1=="rock" and player2=="peaper":
    print("player2 wins")
if player1=="rock" and player2=="scissors":
    print("player1 wins")
if player1=="peaper" and player2=="scissors":
    print("player2 wins")
if player1=="peaper" and player2=="rock":
    print("player1 wins")
if player1=="scissors" and player2=="rock":
    print("player2 wins")
if player1=="scissors" and player2=="peaper":
    print("player1 wins") 
elif player1==player2:
    print("that's a tie...")