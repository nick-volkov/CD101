composers_data={}
while True:
    name=input("Please enter composer's name: ")
    birth=input("Please eneter composer's birth year: ")
    death=input("Please enter composer's death year: ")
    def minus(x, y):
        z=x-y
        return z
    age = minus(int(death), int(birth))
    composers_data[name] = int(age)

    question=input("One more composer? Press Y if yes or N if no: ")
    if question=="y":
        print("Next composer")
    elif question=="n":
        break

for name, age in composers_data.items():
    print (f"Name: {name}, Age: {age}")

def avg(ages):
    s=0
    for x in ages:
        s=s+x
    a=s/len(composers_data)
    return a
print(f"Average age: {avg(composers_data.values())} years")




