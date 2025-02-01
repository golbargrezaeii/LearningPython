myname ="golbarg"
for character in myname:
    print(character)
print("________________________________________")
mynumber = [23,3,67,4,34]
for number in mynumber:
    print(number)
print("________________________________________")
mynumber = [23,3,67,4,34]
for number in mynumber:
    print(number*2)
print("________________________________________")
for number in range(1,20):
    print("*"*number)
    print("________________________________________")
for number in range(1,20):
    if number%2==1:
        print("*" * number)
    else:
        for stars in range(20,0,-1):
            print("*" * stars)
            print("________________________________________")