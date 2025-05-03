num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
result = num1*num2
print(f"{num1}*{num2}={result}")

my_list=[]
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(2,15)
print(my_list)

numbers=[50,60,70]
my_list.extend(numbers)
print(my_list)

del my_list[-1]
print(my_list)

my_list.sort()
print(my_list)  

index_30 = my_list.index(30)
print("Index of 30:", index_30)


