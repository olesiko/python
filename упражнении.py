# a = int(input("введите возраст собаки"))

# if a<=21:
#     print(a/10.5)
# else:
#     print((a-21)/4+2)

age_pet = int(input("введите сколько лет прожила собака"))
if age_pet<= 2:
    age_pet *= 10.5
else:
    age_pet = (age_pet-2)*4+21
    print(f"по человеческим меркам собаки {age_pet} лет")