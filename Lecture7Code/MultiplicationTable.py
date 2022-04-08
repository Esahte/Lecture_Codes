print("          Multiplication Table")
# Display the number title
print("   ", end='')
for j in range(1, 10):
    print("  ", j, end='')
print()  # Jump to the new line
print("-----------------------------------------")

# Display table body
for x in range(1, 10):
    print(x, "|", end='')
    for j in range(1, 12):
        # Display the product and align properly
        print(format(x * j, '4d'), end='')
    print()  # Jump to the new line
