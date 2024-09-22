from Drivers import Driver
from Team import Team

POINTS = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # Points for top 10 finishes in F1
RIDE_5 = [25, 20, 15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

class Race:    
    """
    Represents a single race in the F1 League.

    Attributes:
        results (list of Driver): The list of drivers and their finishing positions.
        penalties (dict of Driver to int): A mapping of drivers to the number of positions they lost due to penalties.
        fastest_lap (Driver): The driver who set the fastest lap.
        laps (int): The number of laps.
        weather (str): The weather conditions.
    """
    def __init__(self):
        self.__results = []
        self.__penalties = {}
        self.__fastest_lap = None
        self.__laps = 0
        self.__weather = ""

    def add_result(self, driver, position):
        """
        Add a driver and their finishing position.

        Args:
            driver (Driver): The driver object.
            position (int): The finishing position of the driver.
        """
        if isinstance(driver, Driver):
            driver.set_position(position)
            self.__results.append(driver)

    def apply_penalty(self, driver, positions_lost):
        """
        Apply a penalty to a driver.

        Args:
            driver (Driver): The driver object.
            positions_lost (int): The number of positions the driver lost due to penalties.
        """
        if isinstance(driver, Driver):
            self.__penalties[driver] = positions_lost

    def finalize_results(self):
        """Finalize the results of the race"""
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
        """Award points to drivers and teams based on their finishing position"""
        for i, driver in enumerate(self.get_results()):
            if isinstance(driver, Driver) and isinstance(driver.team, Team) and i < len(self.POINTS):
                driver.points += self.POINTS[i]
                driver.team.points += self.POINTS[i]

    def print_race_results(self):
        """Print the results of the Race"""
        print("Race Results:")
        for driver in self.get_results():
            if isinstance(driver, Driver) and isinstance(driver.team, Team):
                print(f"{driver.get_name()} ({driver.team.get_name()}) - Position: {driver.get_position()}, Points: {driver.get_points()}")

    # Getters and setters
    def get_results(self):
        """
        Get the results of the race.

        Returns:
            list of Driver: The list of drivers and their finishing positions.
        """
        return self.__results

    def set_results(self, results):
        """
        Set the results of the race.

        Args:
            results (list of Driver): The list of drivers and their finishing positions.
        """
        self.__results = results

    def get_penalties(self):
        """
        Get the penalties applied to drivers.

        Returns:
            dict of Driver to int: A mapping of drivers to the number of positions they lost due to penalties.
        """
        return self.__penalties

    def set_penalties(self, penalties):
        """
        Set the penalties applied to drivers.

        Args:
            penalties (dict of Driver to int): A mapping of drivers to the number of positions they lost due to penalties.
        """
        self.__penalties = penalties

    def get_fastest_lap(self):
        """
        Get the driver who set the fastest lap.

        Returns:
            Driver: The driver who set the fastest lap.
        """
        return self.__fastest_lap

    def set_fastest_lap(self, fastest_lap):
        """
        Set the driver who set the fastest lap.

        Args:
            fastest_lap (Driver): The driver who set the fastest lap.
        """
        self.__fastest_lap = fastest_lap

    def get_laps(self):
        """
        Get the number of laps in the race.

        Returns:
            int: The number of laps.
        """
        return self.__laps

    def set_laps(self, laps):
        """
        Set the number of laps in the race.

        Args:
            laps (int): The number of laps.
        """
        self.__laps = laps

    def get_weather(self):
        """
        Get the weather conditions of the race.

        Returns:
            str: The weather conditions.
        """
        return self.__weather

    def set_weather(self, weather):
        """
        Set the weather conditions of the race.

        Args:
            weather (str): The weather conditions.
        """
        self.__weather = weather