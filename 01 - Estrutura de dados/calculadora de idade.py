"""birth_year = input("Digite seu ano de nascimento: ")
age = 2023 - int(birth_year)
print("Você tem", age, "anos de idade.")"""

"""course = 'Python for Beginners'
print(course.find ('y'))"""

"""temperature = int(input("Qual a temperatura agora?"))
if temperature >= 30:
    print('It´s a hot day!')
    print("You should drink a lot of water.")
elif temperature <= 20:
    print("It´s a nice day. ")"""

weight = int(input("Weight: "))
unit = input("(K)g" or "(L)bs:")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + converted)
else:
    converted = weight* 0.45
    print = weight("Weight in Kgs: " + str (converted))    
