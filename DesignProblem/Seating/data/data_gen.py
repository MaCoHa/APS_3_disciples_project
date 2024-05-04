import random
import sys

def generate_matrix(x, y):
    matrix = [[random.choice(['0', 'I', 'H', 'S']) for _ in range(y)] for _ in range(x)]

    # Ensure that I and S are not adjacent horizontally, vertically, or diagonally
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 'I':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (0 <= i+dx < x) and (0 <= j+dy < y) and matrix[i+dx][j+dy] == 'S':
                            matrix[i][j] = '0'
            elif matrix[i][j] == 'S':
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (0 <= i+dx < x) and (0 <= j+dy < y) and matrix[i+dx][j+dy] == 'I':
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
