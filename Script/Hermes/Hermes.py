import sys
import os

current_dir = os.path.dirname(__file__)
script_dir = os.path.join(current_dir, '..')
sys.path.append(script_dir)

from Pandora.Pandora import Pandora
from Atlas.Atlas import Atlas

class Hermes:
    '''
    Hermes class. It's responsible for the movement and the money collection.
    '''
    _POSITIONAL_ERROR    =   [0,  0]
    _UPWARDS             =   [-1, 0]
    _DOWNWARDS           =   [1,  0]
    _LEFT                =   [0, -1]
    _RIGHT               =   [0,  1]
    def __init__(self, path:str) -> None:
        self.map = Atlas(path)
        self.position = self.map.start
        self.direction = self._RIGHT
        self.money_bag = Pandora()

    def change_direction(self) -> list:
        '''
        Verify the direction to follow in the map using the current position and the current direction
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        try:
            x, y = self.position
            map_border = (x == len(self.map)-1 or y == len(self.map[0])-1)

            # CURRENT DIRECTION IS HORIZONTAL
            if self.irection[1] != 0:
                # If it's a border, or downwards street exists
                if (map_border) or (self.map[x+1][y] is self.map.VERTICAL_STREET):
                    print(f"[VERBOSE] New Direction: _DOWNWARDS")
                    return self._DOWNWARDS
                print(f"[VERBOSE] New Direction: _UPWARDS")
                return self._UPWARDS

            # CURRENT DIRECTION IS VERTICAL
            if self.direction[0] != 0:
                # If it's a border, or left street exists
                if (map_border) or (map[x][y-1] is self.map.HORIZONTAL_STREET):
                    print(f"[VERBOSE] New Direction: _LEFT")
                    return self._LEFT
                print(f"[VERBOSE] New Direction: _RIGHT")
                return self._RIGHT
        except:
            print(f"[ERROR] Não foi possível definir direção a partir da posição {self.position}.")
            return self._POSITIONAL_ERROR

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
        x, y = self.direction
        while (self.map[x][y] not in self.map._CURVE) and (self.map[x][y] != self.map._DEAD_END):
            print(f"| Current Element={self.map[x][y]} : Current Position={[x,y]} : Current Direction={self.direction}|")
            if self.map[x][y].isdigit():
                print("[VERBOSE] DIGIT FOUND!")
                [x,y] = self.collect_money()
                continue

            x += self.direction[0]
            y += self.direction[1]

    # def change_direction(self) -> None:
    #     '''
    #     Verify the direction to follow in the self.map using the current position and the current direction
    #     Time Complexity: O(1)
    #     Space Complexity: O(1)
    #     '''
    #     try:
    #         x, y = self.position
    #         map_border = (x == len(self.map)-1 or y == len(self.map[0])-1)

    #         # CURRENT DIRECTION IS HORIZONTAL
    #         if self.direction[1] != 0:
    #             if (map_border) or (self.map[x+1][y] is self.map._VERTICAL_STREET) or (self.map[x+1][y].isdigit()):
    #                 print(f"[VERBOSE] New Direction: _DOWNWARDS")
    #                 return self._DOWNWARDS
    #             print(f"[VERBOSE] New Direction: _UPWARDS")
    #             return self._UPWARDS


    #         # CURRENT DIRECTION IS VERTICAL
    #         if self.direction[0] != 0:
    #             if (map_border) or (self.map[x][y-1] is self.map._HORIZONTAL_STREET) or (self.map[x][y-1].isdigit()):
    #                 print(f"[VERBOSE] New Direction: _LEFT")
    #                 return self._LEFT
    #             print(f"[VERBOSE] New Direction: _RIGHT")
    #             return self._RIGHT
    #     except:
    #         print(f"[ERROR] Não foi possível definir direção a partir da posição {self.position}.")
    #         return self._POSITIONAL_ERROR