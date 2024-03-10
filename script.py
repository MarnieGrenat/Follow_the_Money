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
VERTICAL_STREET     = "|"
HORIZONTAL_STREET   = "-"
INITIAL_POSITION    =   [0,  0]
UPWARDS             =   [-1, 0]
DOWNWARDS           =   [1,  0]
LEFT                =   [0, -1]
RIGHT               =   [0,  1]

# Functions
def get_map_matrix(path:str) -> list:
    return transform_map_to_matrix(get_map(path))

def transform_map_to_matrix(_map:str) -> list:
    '''
    Transform the map into a matrix, where each element is a character of the map
    Complexity: O(n)
    Space Complexity: O(lines * columns)
    '''
    _map = _map.split('\n')
    matrix = []
    for line in _map:
        matrix.append(list(line))

    # pegar tamanho da maior linha da matriz
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
        track = file.read()
    track = track.replace(' ', SPACE)
    track = track[track.find('\n') + 1:]
    print(track)
    return track

def print_matrix_position(matrix: list, position: list) -> None:
    for i, row in enumerate(matrix):
        printed_row = row.copy()
        if i == position[0]:
            printed_row[position[1]] = "X"
        print("".join(map(str, printed_row)))


def travel_through_matrix(matrix: list) -> list:
    '''
    Travel through the matrix and return the total value of the money and a list with the money in the order they were found
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    # Verify first direction
    direction = INITIAL_POSITION
    if matrix[0][0] == HORIZONTAL_STREET or matrix[0][0].isdigit():
        print("Direção inicial: direita")
        direction = RIGHT
    elif matrix[0][0] == VERTICAL_STREET or matrix[0][0].isdigit():
        print("Direção inicial: esquerda")
        direction = DOWNWARDS

    # Travel through the matrix
    list_money = []
    current_position = INITIAL_POSITION
    try:
        while matrix[current_position[0]][current_position[1]] != DEAD_END:
            # If the current position is a corner, then change the direction
            if matrix[current_position[0]][current_position[1]] in ['\\', '/']:
                direction = change_direction(matrix, current_position, direction)
            # print(f"Posição atual: {current_position}, Direção atual: {direction}")

            # Update the current position to the next position
            current_position[0] += direction[0]
            current_position[1] += direction[1]
    except:
        print("Erro! A execução não foi finalizada corretamente.")
    return list_money

def change_direction(matrix:list, position:list, direction:list=INITIAL_POSITION) -> list:
    '''
    Verify the direction to follow in the matrix using the current position and the current direction
    Time Complexity: O(1)
    Space Complexity: O(1)
    '''

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

    print(f"Erro! Não foi possível definir direção a partir da posição {position}.")
    return INITIAL_POSITION

def verify_value(matrix:list, current_position:list, current_direction:list=INITIAL_POSITION) -> tuple: # (bool, int, tuple)
    '''
    Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    if not matrix[current_position].isdigit():
        return (False, 0, [])

    digits = str(matrix[current_position])
    while matrix[current_position + current_direction].isdigit():   # While the next element is a number
        current_position += current_direction                       # Move to the next position that will be a digit
        digits += str(matrix[current_position])                     # Add the number to the digits
    return (True, int(digits), current_position)

def main():
    print("Iniciando execução do script...")
    money_map = get_map_matrix(PATH)

    sorted_list = travel_through_matrix(money_map)
    total_value = sum(sorted_list)
    print("Execução finalizada!")
    print(f"Valor total do dinheiro derrubado: {total_value}")
    print(f"Lista ordenada de dinheiro derrubado: /n{sorted_list}")

if __name__ == "__main__":
    main()
    pass
