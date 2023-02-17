from calculator.evaluation import evaluate
from convertor import conv_1


print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

print("5. base 10")
print("6. base 02")
print("7. base 12")
print("8. base 16")

try:
    z = int(input('Enter operation from 1 to 4'))
    k = int(input("Enter number systems from 5 to 8"))
except ValueError:
    z == 0
    print("Dont print zero")
 
try:
    x = int(input('Enter fisrt number:'))
    y = int(input('Enter second number:'))
    
except ValueError:
    print("Enter only integer please")

j = None
bs_3 = None




print(evaluate(x,y,z))