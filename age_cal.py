user_data = input ("please enter your name, surname, birth year separated by space: ").split(" ")
curr_year = 2021
age = curr_year - int (user_data [2])

# ['Nick', 'Volkov', '1988']
print (f"You are: {user_data [0]} {user_data [1]}, {age} years old")
