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
print("rock,peaper,scissors")
player1=input("player1,make your movement:")
player2=input("player2,make your movement:")

if player1==player2:
    print("that's a tie...")
    
elif player1=="rock":
    if player2=="scissors":
        print("player1 wins")
    if player2=="peaper":
        print("player2 wins")
elif player1=="peaper":
    if player2=="scissors":
        print("player2 wins")
    if player2=="rock":
        print("player1 wins")
elif player1=="scissors":
    if player2=="peaper":
        print("player1 wins")
    if player2=="rock":
        print("player2 wins")
else:
    print("smth went wrong...")
ROCK,PEAPER,SCISSORS
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