from calculator.evaluation import evaluate


print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

z = int(input('Enter operation from 1 to 4'))
x = int(input('Enter fisrt number:'))
y = int(input('Enter second number:'))


print(evaluate(x,y,z))