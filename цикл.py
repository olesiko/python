

# if age1>age2:
#     print("age1 больше age2")
# else:
#     print("age2 больше age1")
# if age3>age2 and age3>age2:
#     print("age3 больше age1 и age2")
# age1 = int(input("кошелек"))
# if age1>100:
#     print("хватит денег")
# else:
#     print("не хватит денег")
колбаса = 112
молоко = 100
сыр = 110
йогурт = 25
age1 = int(input("сколько у вас денег"))
if age1>0 and age1<26:
    print("можешь купить йогурт")
if age1>26 and age1<101:
    print("можешь купить йогурт и молоко")
if age1>101 and age1<111:
    print("можешь купить все кроме колбасы")
if age1>111:
    print("можешь купить все")
else:
    print("у тебя не хватает денег")


