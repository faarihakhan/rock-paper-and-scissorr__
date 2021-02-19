import random
def game(comp, you):
    if comp==you:
        return None
    #Check all Possibilities for rock (r)
    elif comp =='r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    
    #check all Possibilities for paper (p)
    elif comp =='p':
        if you == 'r':
            return False
        elif you == 's':
            return True

     #check all Possibilities for scissor (p)
    elif comp =='s':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Computer Turn: Rock(r) Paper(p) or Scissor(s) ? ")
randomNo = random.randint(1,3)
if randomNo == 1:
    comp = 'r'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 's'

you = input("Your Turn: Choose Rock(r) Paper(p) or Scissor(s) ? ")
g = game(comp, you)
print(f"Computer choose {comp}")
print(f"You choose {you}")

if g==None:
    print("The game is Tie!")
elif g:
    print("You win!")
else:
    print("You lose!")