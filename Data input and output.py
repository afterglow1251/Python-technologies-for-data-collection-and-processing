#1
name = input("What is your name? ")
age = input("How old are you? ")
location = input("Where are you live? ")

print("This is", name)
print("It is", age)
print("(S)he lives in", location)

#2
expression = "4 * 100 - 54"
result = eval(expression)  # Використовуємо функцію eval() для обчислення виразу
user_answer = int(input(f"Solve the expression {expression}: "))
print("Correct answer:", result)
print("Your answer:", user_answer)

#3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum1 = num1 + num2
sum2 = float(input("Enter the third number: ")) + float(input("Enter the fourth number: "))

result = round(sum1 / sum2, 2)
print("Result:", result)
