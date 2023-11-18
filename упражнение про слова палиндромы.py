word = "наворуван"

left = 0
right = 8
  
while left!=right:
    if (word[0]==word[8]):
        print(f"буквы равны")
        left +=1
        right -=1
    else:
        print("слово", word, "не палиндром")

