import random
import sys

def generate_matrix(x, y):
    matrix = [[random.choice(['0', 'B', 'H', 'F']) for _ in range(x)] for _ in range(y)]

    # Ensure that I and S are not adjacent horizontally, vertically, or diagonally
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 'B':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (0 <= j+dx < x) and (0 <= i+dy < y) and matrix[i+dy][j+dx] == 'F':
                            matrix[i][j] = '0'
            elif matrix[i][j] == 'F':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (0 <= j+dx < x) and (0 <= i+dy < y) and matrix[i+dy][j+dx] == 'B':
                            matrix[i][j] = '0'

    return matrix

def write_matrix_to_file(x,y,matrix, file_path):
    with open(file_path, 'w') as f:
        f.write('{} {}'.format(x,y) + '\n')
        
        for row in matrix:
            f.write(' '.join(row) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <x> <y> <output_file>")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    output_file = sys.argv[3]

    matrix = generate_matrix(x, y)
    write_matrix_to_file(x,y,matrix, output_file)
    print(f"Matrix of size {x}x{y} has been written to {output_file}.")
