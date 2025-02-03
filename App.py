import random
from operator import truediv, index

My_List=["Dog","Cat","Mouse"]
Random_element=random.choice(My_List)
print(Random_element)
Guess=0


print("_"*len(Random_element))
value=0
while Guess<=len(Random_element):
 user_input = input("Enter a letter: ")
 if Random_element[value]==user_input:
    print(user_input)
    value=+ 1


 else:
    print("Wrong letter")
Guess=+1
