#Calculate Factorial using a function
'''

def factorial(n):
    if n==0:
        return 1
    else:
        res = 1
        for i in range(1, n+1):
            res*=i
    return res

num = int(input('Enter a number: '))
result = factorial(num)
print("Factorial of {} is {}".format(num, result))

'''
# Factorial of a number using while loop
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        current_num = n
        while(current_num>=1):
            result*=current_num
            current_num-=1
        return result

num = int(input('Enter a number: '))
result = factorial(num)
print("Factorial of {} is {}".format(num, result))
