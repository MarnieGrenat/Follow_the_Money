import sys
import os

current_dir = os.path.dirname(__file__)
script_dir = os.path.join(current_dir, '..')
sys.path.append(script_dir)

from Olympus.Pandora import Pandora
from Olympus.Atlas import Atlas
class Hermes:
    '''
    Hermes class. It's responsible for the movement and the money collection.
    '''
    def __init__(self, path:str, repeat_value:bool=False, debug:bool=False) -> None:
        self._dirs = {
            "U":     [-1, 0],
            "D":     [1, 0],
            "L":     [0, -1],
            "R":     [0, 1],
            "ERROR": [0, 0]
        }
        self.atlas = Atlas(path, debug)
        self.pandora = Pandora()
        self.mapping = self.atlas.map
        self.position = self.atlas.start
        self.direction = self._dirs["R"]

        self.repeat = repeat_value
        self.debug = debug

    # Setters
    def should_repeat_value(self, value:bool) -> None:
        self.repeat = value
        self.log(f"Setting visited value to {self.repeat}.")

    def is_at_dead_end(self) -> bool:
        try:
            i, j = self.position
            return (self.mapping[i][j] == self.atlas._DEAD_END)
        except:
            print(f"Error at position {self.position}.")
            self.atlas.debug_save(self.direction)
            sys.exit(1)

    def is_not_at_wall(self) -> bool:
        try:
            i, j = self.position
            return self.mapping[i][j] == self.atlas._WALL
        except:
            print(f"Error at position {self.position}.")
            self.atlas.debug_save(self.direction)
            sys.exit(1)


    def get_money_amount(self) -> int:
        return self.pandora.get_amount()

    def get_money_list(self) -> list:
        return self.pandora.get_money_list()

    # Other Methods
    def change_curve_direction(self) -> int:
        '''
        Verify the direction to follow in the map using the current position and the current direction
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        try:
            self.log(f"Checking a Curve! Current Direction: {self.direction}.")
            self.log_position()

            # CURRENT DIRECTION IS VERTICAL
            if self.direction == self._dirs['U']:
                if self.mapping[self.position[0]][self.position[1]] == '/':
                    self.update_position_and_direction(self._dirs['R'])
                elif self.mapping[self.position[0]][self.position[1]] == '\\':
                    self.update_position_and_direction(self._dirs['L'])
            elif self.direction == self._dirs['D']:
                if self.mapping[self.position[0]][self.position[1]] == '/':
                    self.update_position_and_direction(self._dirs['L'])
                elif self.mapping[self.position[0]][self.position[1]] == '\\':
                    self.update_position_and_direction(self._dirs['R'])


            # CURRENT DIRECTION IS HORIZONTAL
            elif self.direction == self._dirs['L']:
                if self.mapping[self.position[0]][self.position[1]] == '/':
                    self.update_position_and_direction(self._dirs['D'])
                elif self.mapping[self.position[0]][self.position[1]] == '\\':
                    self.update_position_and_direction(self._dirs['U'])
            elif self.direction == self._dirs['R']:
                if self.mapping[self.position[0]][self.position[1]] == '/':
                    self.update_position_and_direction(self._dirs['U'])
                elif self.mapping[self.position[0]][self.position[1]] == '\\':
                    self.update_position_and_direction(self._dirs['D'])
            return 1
            

            # if self.direction[1] == 0:
            #     # If it's a border, or left street exists
            #     if (self.position[1] > 0 and self.mapping[self.position[0]][self.position[1] - 1] == self.atlas._HORIZONTAL_STREET):
            #         self.update_position_and_direction(self._dirs['L'])
            #         return
            #     self.update_position_and_direction(self._dirs['R'])
            # # CURRENT DIRECTION IS HORIZONTAL
            # elif self.direction[0] == 0:
            #     # If it's a border, or downwards street exists
            #     if (self.position[0] > 0 and self.mapping[self.position[0] - 1][self.position[1]] == self.atlas._VERTICAL_STREET):
            #         self.update_position_and_direction(self._dirs['U'])
            #         return
            #     self.update_position_and_direction(self._dirs['D'])

        except:
            self.log(f"Não foi possível definir direção a partir da posição {self.position}.")
            self.atlas.debug_save(self.direction)
            # sys.exit(1)

    def travel_until_curve(self) -> int:
        '''
        Travel through the self.atlas and return the total value of the money and a list with the money in the order they were found
        Time Complexity: O(n)
        '''
        # try:
        op = 0
        while (self.mapping[self.position[0]][self.position[1]] not in self.atlas._CURVE) and (not self.is_at_dead_end()):
            op += 1
            self.atlas.debug_control(self.position)
            self.log_informations()

            if self.mapping[self.position[0]][self.position[1]].isdigit():
                self.log("FOUND MONEY!")
                self.collect_money() # returns current coordinates after collecting money
                continue    # Don't update coordinates manually

            self.update_position()
        return op
        # except:
        #     self.atlas.debug_save(self.direction)
        #     sys.exit(1)

    def collect_money(self) -> int:
        '''
        Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
        Time Complexity: O(n)
        '''
        op = 0
        self.log(f"Starting money collection at position {self.position}.")
        value = ''
        while self.mapping[self.position[0]][self.position[1]].isdigit():
            op += 1
            value += str(self.mapping[self.position[0]][self.position[1]])
            if not self.repeat:
                self.atlas.set_as_visited(self.position)
            self.update_position()

        self.pandora.collect(int(value), self.debug)
        self.log(f"Finished money collection: {self.get_money_amount()} at Position {self.position}.")
        return op

    def update_position_and_direction(self, direction : dict) -> None:
        self.direction = direction
        self.log(f"Updating direction to {self.direction}.")
        self.update_position()

    def update_position(self) -> None:
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]
        self.log(f"Updating position to {self.position}.")

    '''        debug METHODS        '''
    def log(self, message:str) -> None:
        if self.debug:
            print(f"[LOG] {message}")

    def log_position(self) -> None:
        if self.debug:
            print(f"[LOG] Current Position: {self.position}")

    def log_direction(self) -> None:
        if self.debug:
            print(f"[LOG] Current Direction: {self.direction}")

    def log_informations(self) -> None:
        if self.debug:
           print(f"| Element={self.mapping[self.position[0]][self.position[1]]} : Position={self.position} : Direction={self.direction} : Money={self.mapping[self.position[0]][self.position[1]].isdigit()} |")