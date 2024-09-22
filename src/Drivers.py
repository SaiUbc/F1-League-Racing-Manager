class Driver:
    """
    Represents a driver participating in the F1 League.

    Attributes:
        name (str): The name of the driver.
        team (Team): The team that the driver belongs to.
        points (int): The points the driver has accumulated.
        position (int): The finishing position of the driver in a race.
        fastest_lap (bool): Whether the driver has set the
    """
    def __init__(self, name, team):
        self.__name = name
        self.__team = team
        self.__points = 0
        self.__position = 0
        self.fastest_lap = False

    def __repr__(self) -> str:
        return f"{self.get_name()} ({self.get_team().get_name()})s  - {self.get_points()} points"
    

    # getters and setters
    def get_name(self):
        return self.__name
    
    def get_team(self):
        return self.__team
    
    def get_points(self):
        return self.__points
    
    def get_position(self):
        return self.__position
    
    def has_fastest_lap(self):
        return self.fastest_lap
    
    def set_name(self, name):
        self.__name = name
    
    def set_team(self, team):
        self.__team = team
    
    def set_points(self, points):
        self.__points = points
    
    def set_position(self, position):
        self.__position = position
    
    def set_fastest_lap(self, fastest_lap):
        self.fastest_lap = fastest_lap