import random
import pandas as pd
import os

Drivers = ['Arya', 'Rishabh', 'Sai']

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


Cars_2023 = {
    'mercedes': {'Name': "Mercedes", 'Weight': 796, 'Drag': 0.77674999, 'Aero': 0.0788, 'Aero Front': 0.0461, 'Aero Rear': 0.0327, 'Weight Distro': 0.250},
    'ferrari': {'Name': "Ferrari", 'Weight': 796, 'Drag': 0.775, 'Aero': 0.0796, 'Aero Front': 0.0457, 'Aero Rear': 0.0339, 'Weight Distro': 0.264},
    'red_bull_racing': {'Name': "Red Bull Racing", 'Weight': 796, 'Drag': 0.76865025, 'Aero': 0.0849, 'Aero Front': 0.0492, 'Aero Rear': 0.0357, 'Weight Distro': 0.264},
    'mclaren': {'Name': "McLaren", 'Weight': 800, 'Drag': 0.775, 'Aero': 0.0808, 'Aero Front': 0.0465, 'Aero Rear': 0.0342, 'Weight Distro': 0.2405},
    'aston_martin': {'Name': "Aston Martin", 'Weight': 805, 'Drag': 0.773249986, 'Aero': 0.0803, 'Aero Front': 0.0463, 'Aero Rear': 0.034, 'Weight Distro': 0.2305},
    'alpine': {'Name': "Alpine", 'Weight': 802, 'Drag': 0.7785, 'Aero': 0.0772, 'Aero Front': 0.0445, 'Aero Rear': 0.0327, 'Weight Distro': 0.236},
    'alphatauri': {'Name': "AlphaTauri", 'Weight': 805, 'Drag': 0.78875033, 'Aero': 0.0716, 'Aero Front': 0.041, 'Aero Rear': 0.0306, 'Weight Distro': 0.2405},
    'alfa_romeo': {'Name': "Alfa Romeo", 'Weight': 803, 'Drag': 0.784749997, 'Aero': 0.0727, 'Aero Front': 0.042, 'Aero Rear': 0.0309, 'Weight Distro': 0.264},
    'haas': {'Name': "Haas", 'Weight': 807, 'Drag': 0.778, 'Aero': 0.0763, 'Aero Front': 0.0439, 'Aero Rear': 0.0324, 'Weight Distro': 0.245},
    'williams': {'Name': "Williams", 'Weight': 809, 'Drag': 0.7709999, 'Aero': 0.0749, 'Aero Front': 0.0428, 'Aero Rear': 0.0321, 'Weight Distro': 0.235}
}


# Add column headings as global variables
column_headings = ['Track', 'Driver', 'Car', 'Lap Time', 'Sector 1', 'Sector 2', 'Sector 3']



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
    track = 'australia'
    for car in reversed(Cars_2023):
        record_race_results(Drivers, track, Cars_2023[car]['Name'])
                
if __name__ == "__main__":
    main()
