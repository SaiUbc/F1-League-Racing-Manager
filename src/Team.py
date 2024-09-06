
from Drivers import Driver

class Team:
    """
    Represents a racing team.

    Attributes:
        name (str): The name of the team.
        drivers (list): A list of drivers in the team.
        points (int): The total points earned by the team.

    Methods:
        add_driver(driver): Adds a driver to the team.
        - Adds a driver to the team.

        Parameters:
            driver (Driver): The driver to be added to the team.
    """
    def __init__(self, name):
        self.__name = name
        self.__drivers = []
        self.__points = 0

    def add_driver(self, driver):
        if isinstance(driver, Driver):
            self.__drivers.append(driver)
        else:
            print("The driver is not a valid Driver object.")

    def __repr__(self):
        return f"{self.get_drivers()} - {self.get_points()} points"
    
    
    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for drivers
    def get_drivers(self):
        return self.__drivers

    # Setter for drivers
    def set_drivers(self, drivers):
        self.__drivers = drivers

    # Getter for points
    def get_points(self):
        return self.__points

    # Setter for points
    def set_points(self, points):
        self.__points = points