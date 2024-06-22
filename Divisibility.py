def check_divisibility(number):
    results = {}

    # Check divisibility by 5
    results['divisible_by_5'] = (number % 5 == 0)

    # Check divisibility by 7
    results['divisible_by_7'] = (number % 7 == 0)

    # Check divisibility by 11
    results['divisible_by_11'] = (number % 11 == 0)

    # Check if the number is even
    results['is_even'] = (number % 2 == 0)

    return results

# Input number
number = int(input("Enter a number: "))

# Check the number
results = check_divisibility(number)

# Print the results
if results['divisible_by_5']:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")

if results['divisible_by_7']:
    print(f"{number} is divisible by 7.")
else:
    print(f"{number} is not divisible by 7.")

if results['divisible_by_11']:
    print(f"{number} is divisible by 11.")
else:
    print(f"{number} is not divisible by 11.")

if results['is_even']:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
