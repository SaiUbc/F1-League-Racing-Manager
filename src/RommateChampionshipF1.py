import random
import pandas as pd
import os

Drivers = ['Rishabh', 'Sai']

Tracks = {
    'australia': "Melbourne Grand Prix Circuit, Australia",
    'bahrain': "Bahrain International Circuit, Bahrain",
    'azerbaijan': "Baku City Circuit, Azerbaijan",
    'miami': "Miami International Autodrome, USA",
    'imola': "Autodromo Enzo e Dino Ferrari, Italy",
    'qatar': "Losail International Circuit, Qatar",
    'las_vegas': "Las Vegas Street Circuit, USA",
    'china': "Shanghai International Circuit, China",
    'netherlands': "Circuit Zandvoort, Netherlands",
    'spain': "Circuit de Barcelona-Catalunya, Spain",
    'monaco': "Circuit de Monaco, Monaco",
    'azerbaijan': "Baku City Circuit, Azerbaijan",
    'canada': "Circuit Gilles Villeneuve, Canada",
    'france': "Circuit Paul Ricard, France",
    'austria': "Red Bull Ring, Austria",
    'united_kingdom': "Silverstone Circuit, United Kingdom",
    'hungary': "Hungaroring, Hungary",
    'belgium': "Circuit de Spa-Francorchamps, Belgium",
    'netherlands': "Zandvoort Circuit, Netherlands",
    'italy': "Autodromo Nazionale Monza, Italy",
    'singapore': "Marina Bay Street Circuit, Singapore",
    'japan': "Suzuka Circuit, Japan",
    'united_states': "Circuit of the Americas, United States",
    'mexico': "Autodromo Hermanos Rodriguez, Mexico",
    'brazil': "Autodromo Jose Carlos Pace, Brazil",
    'saudi_arabia': "Jeddah Street Circuit, Saudi Arabia",
    'abu_dhabi': "Yas Marina Circuit, Abu Dhabi"
}


Cars = {
    'mercedes': {'Name': "Mercedes", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'red_bull_racing': {'Name': "Red Bull Racing", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'mclaren': {'Name': "McLaren", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'aston_martin': {'Name': "Aston Martin", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'alpine': {'Name': "Alpine", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'ferrari': {'Name': "Ferrari", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'alphatauri': {'Name': "AlphaTauri", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'alfa_romeo': {'Name': "Alfa Romeo", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'haas': {'Name': "Haas", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746},
    'williams': {'Name': "Williams", 'Drivetrain': 'MR', 'Power': 950, 'Weight': 746}
}


# Add column headings as global variables
column_headings = ['Track', 'Driver', 'Car', 'Lap Time', 'Secton 1', 'Section 2', 'Section 3']



def record_race_results(Drivers, selected_track, car):
    """
    Records the race results in a CSV file without duplicating headers.
    """
    file_exists = os.path.isfile('f1_testing.csv')  # Check if file already exists
    race_results = []
    

    for driver in Drivers:
        track_name = Tracks[selected_track]

        lap_time = input(f"Enter lap time for {driver}: ")
        section_1 = input(f"Enter section 1 time for {driver}: ")
        section_2 = input(f"Enter section 2 time for {driver}: ")
        section_3 = input(f"Enter section 3 time for {driver}: ")
        
        race_results.append([track_name, driver, car, lap_time, section_1, section_2, section_3])

    df = pd.DataFrame(race_results, columns=column_headings)
    
    # Append to CSV, write headers only if file doesn't exist
    df.to_csv('f1_testing.csv', mode='a', header=not file_exists, index=False)
    
    print("Race results recorded successfully.")


def main():
       for cars in Cars:
        track = 'japan'
        record_race_results(Drivers, track, Cars[cars]['Name'])
                
if __name__ == "__main__":
    main()
