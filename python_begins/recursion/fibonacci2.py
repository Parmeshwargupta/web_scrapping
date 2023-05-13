def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


try:
    n = int(input('Enter the number of terms in the Fibonacci series: '))
    if n <= 0:
        print('Invalid input. Please enter a positive integer.')
    else:
        print(f'The Fibonacci series up to {n} terms is:')
        for i in range(n):
            print(fibonacci(i))
except ValueError:
    print('Invalid input. Please enter a valid integer.')
