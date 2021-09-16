def fib(n):
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return (fib(n-1) + fib(n-2))

n=int(input('Enter the number of terms to obtain fibonacci sequence :'))

if n <= 0:
    print('invalid input')

else:
    print('Fibonacci sequence :')
    for i in range(n):
        print(fib(i))
    

