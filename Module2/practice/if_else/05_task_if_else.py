# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
month = int(input("Номер месяца:"))
if month < 1 and month > 12:
	print("Ошибка")	
elif month <= 2 or month == 12:
	print("зима")	
elif month >= 3 and month <= 5:
	print("Весна")	
elif month >= 6 and month <= 8:
	print("Лето")
elif month >= 9 and month <=11:
	print("Осень")	
