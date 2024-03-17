'''
Linhas: 12
Colunas: 18
Valor total: 1631
Lista:
[28, 17, 4, 13, 0, 0, 7, 561, 9, 2,
8,
8, 2, 2, 4, 6,
7,
99, 3,
91,
1, 9, 5, 7, 0, 461,
127,
3,
2, 7, 0, 6, 9,
9,
5, 8, 4, 83, 6, 5, 0, 3]
'''
# Constants
PATH                = "./map.txt"
DEAD_END            =   "#"
SPACE               =   "+"
VERTICAL_STREET     =   "|"
HORIZONTAL_STREET   =   "-"
CURVE               =   ['\\', '/']
POSITIONAL_ERROR    =   [0,  0]
UPWARDS             =   [-1, 0]
DOWNWARDS           =   [1,  0]
LEFT                =   [0, -1]
RIGHT               =   [0,  1]

PRINT_POSITION      = "@"
# Functions
def get_map_matrix(path:str) -> list:
    return transform_map_to_matrix(get_map(path))

def transform_map_to_matrix(track:str) -> list:
    '''
    Transform the map into a matrix, where each element is a character of the map.
    Also add spaces to the end of each line to make the matrix a rectangle.
    Complexity: O(2n)
    Space Complexity: O(lines * columns)
    '''
    track  = track.split('\n')
    matrix = []
    for line in track:
        matrix.append(list(line))

    max_size = max(len(line) for line in matrix)
    for line in matrix:
        line.extend([SPACE] * (max_size - len(line)))
    return matrix

def get_map(path:str) -> str:
    '''
    Access the file and return the map as a string
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    with open(path, 'r') as file:
        map_file = file.read()

    # Make it usable for matrix iteration
    map_file = map_file.replace(' ', SPACE)
    map_file = map_file[map_file.find('\n') + 1:]

    return map_file

def print_matrix_position(matrix: list, position: list) -> None:
    '''
    print matrix for debugging.
    '''
    for i, row in enumerate(matrix):
        printed_row = row.copy()
        if i == position[0]:
            printed_row[position[1]] = PRINT_POSITION
        print("".join(map(str, printed_row)))


def travel_through_matrix(matrix:list, coordinates:list, direction:list) -> tuple:
    '''
    Travel through the matrix and return the total value of the money and a list with the money in the order they were found
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    # Travel through the matrix
    money_list = []
    x, y = coordinates
    try:
        while matrix[x][y] not in CURVE:
            print(f"{matrix[x][y]} - Posição atual: {[x,y]}, Direção atual: {direction}")
            if matrix[x][y].isdigit():
                print("Dígito Encontrado!")
                money, [x,y] = verify_value(matrix, matrix[x][y], direction)
                money_list.append(money)

            # Update the current position to the next position
            x += direction[0]
            y += direction[1]
    except:
        print("Erro! A execução não foi finalizada corretamente.")
    return (money_list, [x,y], direction)

def change_direction(matrix:list, position:list, direction:list=POSITIONAL_ERROR) -> list:
    '''
    Verify the direction to follow in the matrix using the current position and the current direction
    Time Complexity: O(1)
    Space Complexity: O(1)
    '''
    try:
        x = position[0]
        y = position[1]

        end_border = (x == len(matrix)-1 or y == len(matrix[0])-1)

        if direction[1] != 0:    # CURRENT DIRECTION IS HORIZONTAL
            if (end_border) or (matrix[x+1][y] is VERTICAL_STREET) or (matrix[x+1][y].isdigit()):
                return DOWNWARDS
            return UPWARDS
        if direction[0] != 0:   # CURRENT DIRECTION IS VERTICAL
            if (end_border) or (matrix[x][y-1] is HORIZONTAL_STREET) or (matrix[x][y-1].isdigit()):
                return LEFT
            return RIGHT
    except:
        print(f"Erro! Não foi possível definir direção a partir da posição {position}.")
        return POSITIONAL_ERROR

def verify_value(matrix:list, current_position:list, direction:list=POSITIONAL_ERROR) -> tuple: # money list, next position
    '''
    Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    if not matrix[current_position].isdigit():
        return (False, 0, [])
    digits =  str(matrix[current_position[0]][current_position[1]])

    i = current_position[0] + direction[0]
    j = current_position[1] + direction[1]

    while matrix[i][j].isdigit():
        i += direction[0]
        j += direction[1]
        digits += str(matrix[i][j]) # add the next digit to the current number

    return (int(digits), [i,j])

def define_initial_direction(position:str):
    if position.isdigit():
        print("Erro! Primeira posição deve definir direção!")
        return POSITIONAL_ERROR
    if position == HORIZONTAL_STREET:
        return RIGHT
    return DOWNWARDS

def main():
    x,y = POSITIONAL_ERROR
    money_map = get_map_matrix(PATH)
    direction = define_initial_direction(money_map[y][x])
    sorted_list = []

    while (money_map[y][x] != DEAD_END):
        money_list, [y,x], direction = travel_through_matrix(money_map, [y,x], direction)
        direction = change_direction(money_map, [y,x], direction)
        sorted_list.append(money_list)

    print(f"Valor total do dinheiro derrubado: {sum(sorted_list)}")
    print(f"Lista ordenada de dinheiro derrubado: \n{sorted_list}")


if __name__ == "__main__":
    print(f"Iniciando Execução!")
    main()
    print("Execução Finalizada!")
