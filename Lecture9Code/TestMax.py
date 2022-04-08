# Return the max between two numbers 
def max(num1, num2): 
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result # Return result

#def main():
    #i = int(input("Enter first integer: "))
    #j = int(input("Enter second number: "))
    #k = max(i, j) # Call the max function
    #print("The maximum between", i, "and", j, "is", k)

#main() # Call the main function

def nPrintln(mess, n):
    for i in range(0,n):
        print(mess)
