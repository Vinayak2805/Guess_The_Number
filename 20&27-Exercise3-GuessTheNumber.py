# Version 2.0
# guess the number game
import random
random_num = random.randint(0, 100)
inp_num = int(input("Enter the number:\n"))
chances = 5

while chances>1:
    chances = chances-1
    if inp_num == random_num:
        print("Congratulaions, You guessed it correct in", (5-chances), "guesses")
        break
    elif inp_num>random_num:
        print("It's less than", inp_num, "\nNo. of chances left:", chances)
        inp_num = int(input("Enter the number:\n"))
        
    elif inp_num<random_num:
        print("It's greater than", inp_num, "\nNo. of chances left:", chances)
        inp_num = int(input("Enter the number:\n"))

if chances==1 and inp_num==random_num:
    print("Congratulaions, You guessed it correct in 5 guesses")
elif chances==1 and inp_num!=random_num:
    print("Game Over, the number was", random_num)

#Version 1.0
"""n = 18
n1 = int(input("Guess the number:"))
print((type(n1) == 'int'))
g=5
while(g>1):
    g = g-1
    print("Number of guesses left: ", g)
    if n1<18:
        print("It's greater than ", n1)
        n1 = int(input("Guess the number:"))
    elif n1>18:
        print("It's less than ", n1)
        n1 = int(input("Guess the number:"))
    else:
        print("Congratulation! You guessed the number")
        break

if g==1 and n1==18:
    print("Congratulation! You guessed the number")
else:
    print("Game Over")"""
