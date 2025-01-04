def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * length + width  # Bug: Should be (2 * (length + width))

def get_positive_number(prompt):
    value = input(prompt)
    if value < 0:  # Bug: input() returns a string; needs conversion and proper comparison
        print("Please enter a positive number.")
        return get_positive_number(prompt)
    return value

# Example usage
length = get_positive_number("Enter the length of the rectangle: ")
width = get_positive_number("Enter the width of the rectangle: ")
print("Area of the rectangle:", calculate_rectangle_area(length, width))
print("Perimeter of the rectangle:", calculate_rectangle_perimeter(length, width))

