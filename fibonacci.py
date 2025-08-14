
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

while True:
    try:
        num_str = input("Enter a single-digit number: ")
        if len(num_str) == 1 and num_str.isdigit():
            num = int(num_str)
            fibonacci_series(num)
            break
        else:
            print("Invalid input. Please enter a single-digit number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
