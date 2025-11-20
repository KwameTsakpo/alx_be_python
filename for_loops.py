# Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
# Initialize a variable total to 0, which will store the running sum.
# Use a for loop to iterate over the numbers list.
# Inside the loop, add the current number (use the loop variable) to the total variable.
# After the loop, print the final total value, which represents the sum of all the numbers in the list.

numbers = [1,5,3,9]

total = 0

for number in numbers:
    total += number

print(f'Sum of all numbers is :{total}')