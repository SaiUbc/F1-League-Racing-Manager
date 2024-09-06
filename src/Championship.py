"""
    Represents the F1 League Championship, tracking the standings of drivers and teams.

    Attributes:
        drivers (list of Driver): The list of all drivers in the championship.
        teams (list of Team): The list of all teams in the championship.
"""

from Drivers import Driver

class Championship:
    def __init__(self):
        self.drivers = []
        self.teams = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_team(self, team):
        self.teams.append(team)

    def get_driver_standings(self):
        return sorted(self.drivers, key=lambda driver: driver.points, reverse=True)

    def get_team_standings(self):
        return sorted(self.teams, key=lambda team: team.points, reverse=True)