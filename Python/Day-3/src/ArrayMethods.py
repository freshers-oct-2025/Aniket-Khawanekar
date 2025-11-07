from copy import deepcopy
from itertools import zip_longest

# Array (List) Methods Demonstration

# Creating a sample list
numbers = [1, 2, 3, 4, 5]

# Common array methods
def demonstrate_array_methods():
    # 1. Append - adds element at the end
    numbers.append(6)
    print("After append:", numbers)

    # 2. Insert - adds element at specific position
    numbers.insert(0, 0)
    print("After insert:", numbers)

    # 3. Remove - removes first occurrence of value
    numbers.remove(3)
    print("After remove:", numbers)

    # 4. Pop - removes and returns element at given index
    popped = numbers.pop(2)
    print("Popped value:", popped)
    print("After pop:", numbers)

    # 5. Sort - sorts the list
    numbers.sort()
    print("After sort:", numbers)

    # 6. Reverse - reverses the list
    numbers.reverse()
    print("After reverse:", numbers)

    # 7. Length of array
    print("Length:", len(numbers))

    # 8. Count - counts occurrences of value
    print("Count of 5:", numbers.count(5))

    # 9. Index - finds position of value
    print("Index of 5:", numbers.index(5))

if __name__ == "__main__":
    demonstrate_array_methods()
    
    
    
    def demonstrate_multidim_array_methods():

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        print("Original matrix:", matrix)

        # Access element
        print("Element [1][2]:", matrix[1][2])

        # Append a new row
        matrix.append([10, 11, 12])
        print("After append row:", matrix)

        # Append element to a sublist
        matrix[0].append(0)
        print("After append to first row:", matrix)

        # Insert a row
        matrix.insert(1, [100, 101, 102])
        print("After insert row at 1:", matrix)

        # Remove a row (first occurrence)
        matrix.remove([100, 101, 102])
        print("After remove row:", matrix)

        # Pop an element from a sublist
        popped = matrix[2].pop(1)
        print("Popped value from row 2:", popped)
        print("After popping from row 2:", matrix)

        # Dimensions (rows and max columns)
        rows = len(matrix)
        cols = max(len(r) for r in matrix)
        print("Dimensions:", f"{rows} x {cols}")

        # Flatten
        flattened = [x for row in matrix for x in row]
        print("Flattened:", flattened)

        # Transpose (handles non-rectangular via zip_longest)
        transposed = [list(filter(lambda v: v is not None, col)) for col in zip_longest(*matrix)]
        print("Transposed:", transposed)

        # Deep copy example
        copy_matrix = deepcopy(matrix)
        matrix[0][0] = 999
        print("Modified original, copy remains:", copy_matrix)

        # Row sums
        row_sums = [sum(row) for row in matrix]
        print("Row sums:", row_sums)

    demonstrate_multidim_array_methods()