data = input('Введите данные:' ).split("*")
name = data[0]
birth_year = int(data[1].split("-")[0])
death_year = int(data[2].split("-")[0])
age = death_year - birth_year
print(
    f"""
Name: {name}
Age: {age} years
"""
)
