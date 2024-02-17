def generate_multiplication_table(number, num_terms):
    multiplication_table = []
    for i in range(1, num_terms + 1):
        multiplication_table.append(number * i)
    return multiplication_table

# Example usage:
number = int(input("Enter the number for multiplication table: "))
num_terms = int(input("Enter the number of terms in the table: "))

table = generate_multiplication_table(number, num_terms)
print(f"The multiplication table of {number} until {num_terms} term(s) is:")
print(table)

