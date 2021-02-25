#lst = [24, 33, 42, 21, 125, -11, 0]
# even = []
# uneven = []
# for val in lst:
#     if val % 2==0:
#         even.append(val)
#     else: 
#          uneven.append(val)  
# print (even)
# print (uneven)

    
# x = 10

# # >, <, >=, <=, ==, and, or, not 
# if x % 2 == 0:
#     print("x is even")
#     print("yet another line")
# else:
#     print("x is not even")


# for val in lst:
#     if val % 2 !=0:
#         print(f"First odd element: {val}")
#         #break -остановиться после нахождения первого нечетного

names = []
ages = [] 

while True:
    data = input ("Please enter your name separated by space: ").split(" ")
    names.append(data [0])
    data = input ("Please enter age: ")
    ages.append(int (data [0]))
    
    status = input ("Would you like to enter one more? Press Y if continue. Otherwise N")
    if status == "N":
        break

for idx, val in enumerate(names):
    print(f"User {idx}: {val}, {ages[idx]}")


sum_age = 0
for x in ages:
    sum_age = sum_age + x
average = (sum_age / len(ages))    
print(average)




