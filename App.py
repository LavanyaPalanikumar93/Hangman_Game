import random

My_List=["Dog","Cat","Mouse"]
Random_element=random.choice(My_List)
print(Random_element)

while len(Random_element)>0:
 user_input = input("Enter a letter: ")
 used_letters=set(user_input)
 print("You used this letters: "," ".join(used_letters))

 word_list=[]
 for letter in Random_element:
     if letter in used_letters:
         word_list.append(letter)
     else:
         word_list.append("-")



