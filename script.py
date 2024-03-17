
# Constants
PATH                = "./map.txt"
VISITED             =   "X"
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
    print matrix. Debugging porpuses
    '''
    for i, row in enumerate(matrix):
        printed_row = row.copy()
        if i == position[0]:
            printed_row[position[1]] = VISITED
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
    while (matrix[x][y] not in CURVE):
        # print(f"| Current Element: {matrix[x][y]} | Current Position: {[x,y]} | Current Direction: {direction}|")
        if matrix[x][y].isdigit():
            print("[VERBOSE] DIGIT FOUND!")
            money, [x,y] = verify_value(matrix, [x, y], direction)
            money_list.append(money)
            continue

        # Update the current position to the next position
        x += direction[0]
        y += direction[1]

        # If error or deadend
        if(matrix[x][y] in [DEAD_END, SPACE]):
            print(f"[VERBOSE] Dead End or SPACE Found! {matrix[x][y]}")
            break
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
                print(f"[VERBOSE] New Direction: DOWNWARDS")
                return DOWNWARDS
            print(f"[VERBOSE] New Direction: UPWARDS")
            return UPWARDS
        if direction[0] != 0:   # CURRENT DIRECTION IS VERTICAL
            if (end_border) or (matrix[x][y-1] is HORIZONTAL_STREET) or (matrix[x][y-1].isdigit()):
                print(f"[VERBOSE] New Direction: LEFT")
                return LEFT
            print(f"[VERBOSE] New Direction: RIGHT")
            return RIGHT
    except:
        print(f"[ERROR] Não foi possível definir direção a partir da posição {position}.")
        return POSITIONAL_ERROR

def verify_value(matrix:list, current_position:list, direction:list=POSITIONAL_ERROR) -> tuple: # money list, next position
    '''
    Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    i = current_position[0]
    j = current_position[1]
    digits = ""
    # print(f"[VERBOSE] Checking Value: {matrix[i][j]} at position {[i,j]}")
    while matrix[i][j].isdigit():
        digits += str(matrix[i][j]) # add the next digit to the current number
        matrix[i][j] = VISITED
        i += direction[0]
        j += direction[1]

    print(f"[VERBOSE] Money value: {digits}")
    return (int(digits), [i,j])

def define_initial_direction(position:str) -> list:
    '''
    Define the initial direction to follow in the matrix.
    If the first position is a digit, return an error.
    '''
    if position.isdigit():
        print("[ERROR] First position should define direction!")
        return POSITIONAL_ERROR
    if position == HORIZONTAL_STREET:
        return RIGHT
    return DOWNWARDS

def main():
    x,y = POSITIONAL_ERROR
    money_map = get_map_matrix(PATH)
    direction = define_initial_direction(money_map[y][x])
    sorted_list = []
    append_list = []

    while (money_map[y][x] != DEAD_END):
        money_list, [y,x], direction = travel_through_matrix(money_map, [y,x], direction)

        append_list.append(money_list)  # append the list of money dropped in the current street
        sorted_list += money_list       # append all the  money dropped in the current street
        if (money_map[y][x] in [SPACE, DEAD_END]):
            break

        # print("[VERBOSE] Curve detected! Changing direction!")
        direction = change_direction(money_map, [y ,x], direction)
        y += direction[0]
        x += direction[1]

    print(f"[LOG] Lista ordenada de dinheiro derrubado: \n{sorted_list}\n")
    print(f"[LOG] Lista ordenada de dinheiro derrubado: \n{append_list}\n")
    print(f"[LOG] Valor total do dinheiro derrubado: {sum(sorted_list)}")


if __name__ == "__main__":
    print(f"[VERBOSE] Initiating Executed!")
    main()
    print("[VERBOSE] Execution Finished Successfully!")