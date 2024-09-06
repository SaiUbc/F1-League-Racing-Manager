
from Drivers import Driver
from Team import Team

POINTS = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # Points for top 10 finishes in F1
class Race:
    """
    Represents a single race in the F1 League.

    Attributes:
        results (list of Driver): The list of drivers and their finishing positions.
        penalties (dict of Driver to int): A mapping of drivers to the number of positions they lost due to penalties.
        fastest_lap (Driver): The driver who set the fastest
        laps (int): The number of laps
        weather (str): The weather conditions
    """
    def __init__(self):
        self.__results = []
        self.__penalties = {}
        self.__fastest_lap = None
        self.__laps = 0
        self.__weather = ""

    def add_result(self, driver, position):
        if isinstance(driver, Driver):
            driver.set_position(position)
            self.__results.append(driver)

    def apply_penalty(self, driver, positions_lost):
        if isinstance(driver, Driver):
            self.__penalties[driver] = positions_lost

    def finalize_results(self):
        for driver, penalty in self.__penalties.items():
            if penalty > 0 and isinstance(driver, Driver):
                current_position = driver.get_position()
                new_position = min(current_position + penalty, len(self.get_results()))

                for other_driver in self.__results:
                    if isinstance(other_driver, Driver) and current_position < other_driver.get_position() <= new_position:
                        other_driver.get_position() -= 1

                driver.set_position(new_position)

        self.__results.sort(key=lambda x: x.position)

    def award_points(self):
        for i, driver in enumerate(self.get_results()):
            if isinstance(driver, Driver) and isinstance(driver.team, Team) and i < len(self.POINTS):
                #TODO! Fix this implementaion needs to account for private variables
                driver.points += self.POINTS[i]
                driver.team.points += self.POINTS[i]

    def print_race_results(self):
        print("Race Results:")
        for driver in self.get_results():
            if isinstance(driver, Driver) and isinstance(driver.team, Team):
                print(f"{driver.get_name()} ({driver.team.get_name()}) - Position: {driver.get_position()}, Points: {driver.get_points()}")


    # Getters and setters
    def get_results(self):
        return self.__results

    def set_results(self, results):
        self.__results = results

    def get_penalties(self):
        return self.__penalties

    def set_penalties(self, penalties):
        self.__penalties = penalties

    def get_fastest_lap(self):
        return self.__fastest_lap

    def set_fastest_lap(self, fastest_lap):
        self.__fastest_lap = fastest_lap

    def get_laps(self):
        return self.__laps

    def set_laps(self, laps):
        self.__laps = laps

    def get_weather(self):
        return self.__weather

    def set_weather(self, weather):
        self.__weather = weather