composers = [1, 2, 3, 4, 5]
composers_data = []

print ("Please enter info on any 5 deceased composers")

for n in composers:
    first_name = input ("Please enter composer's first name: ")
    composers_data.append(first_name)
    last_name = input ("Please enter composer's last name: ")
    composers_data.append(last_name)
    b_year = input ("Please enter composers's year of birth: ")
    composers_data.append(b_year)
    d_year = input ("Please enter composer's year of death: ")
    composers_data.append (d_year)

age1 = int (composers_data [3]) - int (composers_data [2])
age2 = int (composers_data [7]) - int (composers_data [6])
age3 = int (composers_data [11]) - int (composers_data [10])
age4 = int (composers_data [15]) - int (composers_data [14])
age5 = int (composers_data [19]) - int (composers_data [18])

print (f"First Name: {composers_data [0]}, Last Name: {composers_data [1]}, Age: {age1}")
print (f"First Name: {composers_data [4]}, Last Name: {composers_data [5]}, Age: {age2}")
print (f"First Name: {composers_data [8]}, Last Name: {composers_data [9]}, Age: {age3}")
print (f"First Name: {composers_data [12]}, Last Name: {composers_data [13]}, Age: {age4}")
print (f"First Name: {composers_data [16]}, Last Name: {composers_data [17]}, Age: {age1}")

age_sum = (age1 + age2 + age3 + age4 + age5)
average_age = (age_sum / 5)
print ("Average age: " + str(average_age))

    

