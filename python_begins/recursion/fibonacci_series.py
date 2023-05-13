n = int(input("Enter the number of terms in the Fibonacci series: "))

# First two terms of the series
a, b = 0, 1

# If the number of terms is less than or equal to 0, no series is generated
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
# If the number of terms is 1, only the first term of the series is printed
elif n == 1:
    print("Fibonacci series up to", n, "term(s):")
    print(a)
# For more than one term, the series is generated and printed
else:
    print("Fibonacci series up to", n, "term(s):")
    for i in range(n):
        print(a)
        # Update variables to generate next term
        c = a + b
        a = b
        b = c
        print(a)
    print()    
