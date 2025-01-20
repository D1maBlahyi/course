
print('I love Python  ' * 42)

#2
age_in_month = 22 * 12
print(age_in_month)

#3
age_in_years = age_in_month // 12
print(age_in_years)

#4
my_age = f"My name is Dima, I'm {age_in_years} years old"
print(my_age)

#5
value = 1
print(value > 0, value > 2, value == 1, value is type(int), value < -7, sep='\n')
print(type(value))

#6
a, b, c = 2, 5, 6
d = str(a) + str(b) + str(c)
print(d)  