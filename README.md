# F1 League Management System

## Overview
Welcome to the F1 League Management System! This project is designed to simplify the management of points, standings, and penalties in a Formula 1-style esports racing league. If you've been struggling with keeping track of race results, adjusting for post-race penalties, and calculating driver and constructor standings, this tool is here to help.

## Features
- **Driver & Team Management**: Track drivers and their respective teams, including their points and positions.
- **Race Results**: Automatically update race results and standings after each race.
- **Penalty Management**: Apply penalties to drivers and adjust their positions accordingly, with the system automatically updating the standings.
- **Points Calculation**: The system follows a standard F1 points distribution model for the top 10 finishes.
- **Standings Export**: Export driver and team standings to Excel files for easy sharing and record-keeping.
- **Future Enhancements**: Planned features include a web interface for easier management and real-time leaderboard updates.

## Installation
To run this project locally, you need Python and some additional libraries. Follow these steps to get started:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/f1-league-manager.git
    ```
2. Navigate to the project directory:
    ```bash
    cd f1-league-manager
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main script:
    ```bash
    python main.py
    ```


# Usage
To use this F1 League Management System, follow these steps:
1. Add Drivers and Teams: Define the drivers and their respective teams in the script.
2. Input Race Results: Enter the finishing order after each race.
3. Apply Penalties: If any post-race penalties are needed, apply them and finalize the results.
4. View Standings: After each race, view and export the updated driver and team standings.

```python
# Create Teams and Drivers
alpine = Team("Alpine")
psilegends = Driver("PSILegends", alpine)
chipscheema = Driver("Chipscheema", alpine)

ferrari = Team("Ferrari")
vifix = Driver("Vifix", ferrari)
yash = Driver("Yash", ferrari)

# Initialize Championship
championship = Championship()
championship.add_team(alpine)
championship.add_team(ferrari)
championship.add_driver(psilegends)
championship.add_driver(chipscheema)
championship.add_driver(vifix)
championship.add_driver(yash)

# Australian GP Results
australia_gp = Race()
australia_gp.add_result(psilegends, 1)
australia_gp.add_result(chipscheema, 2)
australia_gp.add_result(vifix, 3)
australia_gp.add_result(yash, 4)

# Apply Penalties
australia_gp.apply_penalty(psilegends, 2)
australia_gp.finalize_results()
australia_gp.award_points()

# View and Export Standings
driver_standings = championship.get_driver_standings()
team_standings = championship.get_team_standings()

# Export to Excel
australia_gp.export_standings_to_excel(driver_standings, team_standings)
```

## Roadmap
- Implement a user-friendly web interface for race result entry and leaderboard display.
- Enable real-time updates and automatic notifications after races.
- Consider integration with popular racing simulation games for automatic result imports.

## Contributing
Contributions are welcome! If you find a bug or have an idea for an improvement, feel free to open an issue or submit a pull request.

## LICENSE
This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or suggestions, feel free to reach out via GitHub issues or contact me directly.
