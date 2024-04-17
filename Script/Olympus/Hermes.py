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

    Attributes:
        _dirs (dict): Dictionary containing direction vectors for movement.
        atlas (Atlas): Instance of the Atlas class representing the map.
        pandora (Pandora): Instance of the Pandora class representing the bag.
        mapping (list): Representation of the map as a matrix.
        position (list): Current position of Hermes in the map.
        direction (list): Current direction vector of movement.
        repeat (bool): Flag indicating whether to repeat visited locations.
        debug (bool): Flag indicating whether to enable debugging.

    Methods:
        __init__(self, path:str, repeat_value:bool=False, debug:bool=False) -> None: Initializes a Hermes object.
        should_repeat_value(self, value:bool) -> None: Sets the repeat flag to the specified value.
        is_at_dead_end(self) -> bool: Checks if Hermes is at a dead end in the map.
        is_not_at_wall(self) -> bool: Checks if Hermes is not at a wall in the map.
        get_money_amount(self) -> int: Returns the total amount of money collected.
        get_money_list(self) -> list: Returns the list of money values collected.
        change_curve_direction(self) -> int: Updates direction based on current position and direction at curves.
        travel_until_curve(self) -> int: Travels until encountering a curve or dead end, collecting money along the way.
        collect_money(self) -> int: Collects money at current position and updates bag accordingly.
        update_position_and_direction(self, direction : dict) -> None: Updates direction and position based on input direction.
        update_position(self) -> None: Updates position based on current direction vector.
        log(self, message:str) -> None: Logs a message if debugging is enabled.
        log_position(self) -> None: Logs current position if debugging is enabled.
        log_direction(self) -> None: Logs current direction if debugging is enabled.
        log_informations(self) -> None: Logs current map element, position, direction, and money presence if debugging is enabled.
    '''

    def __init__(self, path:str, repeat_value:bool=False, debug:bool=False) -> None:
        '''
        Initializes a Hermes object.

        Args:
            path (str): The path to the map file.
            repeat_value (bool, optional): Whether to repeat the value at visited positions. Defaults to False.
            debug (bool, optional): Whether to enable debug mode. Defaults to False.
        '''
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
        Verify the direction to follow in the map using the current position and the current direction.

        Returns:
            int: 1
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
            sys.exit(1)

    def travel_until_curve(self) -> int:
        '''
        Travel through the map until reaching a curve or a dead end.
        Time Complexity: O(n)

        Returns:
            int: Number of operations performed during the travel.
        '''
        try:
            op = 0
            while (self.mapping[self.position[0]][self.position[1]] not in self.atlas._CURVE) and (not self.is_at_dead_end()):
                op += 1
                self.atlas.debug_control(self.position)
                self.log_informations()

                if self.mapping[self.position[0]][self.position[1]].isdigit():
                    self.log("FOUND MONEY!")
                    op += self.collect_money() # returns current coordinates after collecting money
                    continue    # Don't update coordinates manually

                self.update_position()
            return op
        except:
            self.atlas.debug_save(self.direction)
            sys.exit(1)

    def collect_money(self) -> int:
        '''
        Verify if the current position has a value, if so, capture that value and ends returning the value and the next position
        Time Complexity: O(n)
        '''
        op = 0
        self.log(f"Starting money collection at position {self.position}.")
        value = ''
        while self.mapping[self.position[0]][self.position[1]].isdigit():
            op += 2 # Duas operações abaixo
            value += str(self.mapping[self.position[0]][self.position[1]])
            if not self.repeat:
                op += 1
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