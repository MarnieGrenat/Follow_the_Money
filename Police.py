from Map import Map
from MoneyBag import MoneyBag as Bag

POSITIONAL_ERROR    =   [0,  0]
UPWARDS             =   [-1, 0]
DOWNWARDS           =   [1,  0]
LEFT                =   [0, -1]
RIGHT               =   [0,  1]

class Police:
    '''
    Police class. It's responsible for the police movement and the money collection.
    '''
    def __init__(self, map: Map) -> None:
        self.map = map
        self.position = map.start
        self.direction = list(self.map.get_initial_direction())
        self.money_bag = Bag()
        self.end_or_wall = [self.DEAD_END, self.WALL]


    def change_direction(self) -> list:
        '''
        Verify the direction to follow in the map using the current position and the current direction
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        try:
            x = self.position[0]
            y = self.position[1]

            map_border = (x == len(self.map)-1 or y == len(self.map[0])-1)

            if self.irection[1] != 0:    # CURRENT DIRECTION IS HORIZONTAL
                if (map_border) or (self.map[x+1][y] is map.VERTICAL_STREET) or (self.map[x+1][y].isdigit()):
                    print(f"[VERBOSE] New Direction: DOWNWARDS")
                    return DOWNWARDS
                print(f"[VERBOSE] New Direction: UPWARDS")
                return UPWARDS
            if self.direction[0] != 0:   # CURRENT DIRECTION IS VERTICAL
                if (map_border) or (map[x][y-1] is map.HORIZONTAL_STREET) or (self.map[x][y-1].isdigit()):
                    print(f"[VERBOSE] New Direction: LEFT")
                    return LEFT
                print(f"[VERBOSE] New Direction: RIGHT")
                return RIGHT
        except:
            print(f"[ERROR] Não foi possível definir direção a partir da posição {self.position}.")
            return POSITIONAL_ERROR


    def collect_money(self, verbose:bool=False) -> list: # next position
        '''
        Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        i = self.position[0]
        j = self.position[1]
        # print(f"[VERBOSE] Checking Value: {self.map[i][j]} at position {[i,j]}")
        while self.map[i][j].isdigit():
            self.money_bag.collect(self.map[i][j], verbose)
            self.map.set_as_visited(i,j)

            i += self.direction[0]
            j += self.direction[1]

        return [i,j]


    def travel_until_curve(self) -> None:
        '''
        Travel through the self.map and return the total value of the money and a list with the money in the order they were found
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        # Travel through the self.map
        money_list = []
        x, y = self.direction
        while (self.map[x][y] not in map.CURVE) and self.map[x][y] not in [map.DEAD_END, map.WALL]:
            # print(f"| Current Element: {self.map[x][y]} | Current Position: {[x,y]} | Current Direction: {direction}|")
            if self.map[x][y].isdigit():
                print("[VERBOSE] DIGIT FOUND!")
                money, [x,y] = self.collect_money()
                money_list.append(money)
                continue

            # Update the current position to the next position
            x += self.direction[0]
            y += self.direction[1]

    def change_direction(self) -> None:
        '''
        Verify the direction to follow in the self.map using the current position and the current direction
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        try:
            x, y = self.position
            map_border = (x == len(self.map)-1 or y == len(self.map[0])-1)

            # CURRENT DIRECTION IS HORIZONTAL
            if self.direction[1] != 0:
                if (map_border) or (self.map[x+1][y] is map.VERTICAL_STREET) or (self.map[x+1][y].isdigit()):
                    print(f"[VERBOSE] New Direction: DOWNWARDS")
                    return DOWNWARDS
                print(f"[VERBOSE] New Direction: UPWARDS")
                return UPWARDS


            # CURRENT DIRECTION IS VERTICAL
            if self.direction[0] != 0:
                if (map_border) or (self.map[x][y-1] is map.HORIZONTAL_STREET) or (self.map[x][y-1].isdigit()):
                    print(f"[VERBOSE] New Direction: LEFT")
                    return LEFT
                print(f"[VERBOSE] New Direction: RIGHT")
                return RIGHT
        except:
            print(f"[ERROR] Não foi possível definir direção a partir da posição {self.position}.")
            return POSITIONAL_ERROR