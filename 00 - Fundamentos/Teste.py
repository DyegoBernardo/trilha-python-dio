month = input()

try:
    month = int(month)  # Converte a entrada para inteiro
    if month == 1:
        months_dict = "January"
    elif month == 2:
        months_dict = "February"
    elif month == 3:
        months_dict = "March"
    elif month == 4:
        months_dict = "April"
    elif month == 5:
        months_dict = "May"
    elif month == 6:
        months_dict = "June"
    elif month == 7:
        months_dict = "July"
    elif month == 8:
        months_dict = "August"
    elif month == 9:
        months_dict = "September"
    elif month == 10:
        months_dict = "October"
    elif month == 11:
        months_dict = "November"
    elif month == 12:
        months_dict = "December"
    else:
        months_dict = "Mês inválido"
    print(months_dict)
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
