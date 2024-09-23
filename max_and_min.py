# Angelo Andrade
# 09/21/24
# max_and_min.py
from multiprocessing.managers import Value

# Write another program that prompts for a list of numbers as above and at the end prints out
# both the maximum and minimum of the numbers instead of the average.

# Create num
# Initializes num stores numeric values from users input.
nums = []
while True:
    # Prompt for user
    user_input = input("Enter a number or `DONE` to finish: ")

    # Check if the user entered 'done' to break the loop
    if user_input == 'done':
        break

    try:
        # Try to convert the input to a float and add it to the list
        num = float(user_input)
        nums.append(num)
    except ValueError:
        # If conversion fails, notify the user and continue the loop
        print("Invalid input. Please enter a numeric value or `done` to finish")

    # Check if the list is not empty before calculating min and max
    if nums:
        print("Maximum:", max(nums))
        print("Minimum:", min(nums))
    else:
        print("No numbers were entered.")