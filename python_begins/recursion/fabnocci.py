def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


try:
    n = int(input('Enter the Number :'))
    print(f'The Fibonacci of the number {n} is:', fibonacci(n))
except ValueError:
    print('Invalid input. Please enter a valid integer.')
