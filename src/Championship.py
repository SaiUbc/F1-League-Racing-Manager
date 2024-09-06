
from Drivers import Driver
from Team import Team

class Championship:
    """
    Represents the F1 League Championship, tracking the standings of drivers and teams.

    Attributes:
        drivers (list of Driver): The list of all drivers in the championship.
        teams (list of Team): The list of all teams in the championship.
    """
    def __init__(self):
        self.drivers = []
        self.teams = []

    def add_driver(self, driver):
        if isinstance(driver, Driver):
            self.drivers.append(driver)

    def add_team(self, team):
        if isinstance(team, Team):
            self.teams.append(team)

    def get_drivers_championship(self):
        drivers_championship = sorted([driver for driver in self.drivers if isinstance(driver, Driver)], key=lambda driver: driver.get_points(), reverse=True)
        return drivers_championship
    
    def get_constructors_championship(self):
        constructors_championship = sorted([team for team in self.teams if isinstance(team, Team)], key=lambda team: team.get_points(), reverse=True)
        return constructors_championship