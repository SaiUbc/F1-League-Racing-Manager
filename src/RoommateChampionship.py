import random
import pandas as pd
import os

Drivers = ['Rishabh', 'Sai']

Tracks = {
    'lake_louise': "Lake Louise, USA",
    'blue_moon': "Blue Moon Bay, USA",
    'laguna_seca': "Laguna Seca, USA",
    'grand-valley': "Grand Valley, USA",
    'trial_mountain': "Trial Mountain, USA",
    'willow_springs': "Willow Springs, USA",
    'colorado_springs': "Colorado Springs, USA",
    'northern_isle': "Northern Isle, USA",
    'raceway_road_atlanta': "Raceway Road Atlanta, USA",
    'daytona': "Daytona, USA",
    'watkins_glen': "Watkins Glen, USA",
    'fishermans_ranch': "Fisherman's Ranch, USA",
    'special_stage_route_x': "Special Stage Route X, USA",
    'interlagos': "Interlagos, Brazil",
    'brands_hatch': "Brands Hatch, UK",
    'goodwood': "Goodwood, UK",
    'circuit_de_spa': "Circuit de Spa, Belgium",
    'nurbugring_gp': "Nurbugring, Germany",
    'nordshleife': "Nordschleife, Germany",
    'alsace': "Alsace, France",
    'eiger_nordwand': "Eiger Nordwand, Switzerland",
    'autodrome_lago_maggiore': "Autodrome Lago Maggiore, Italy",
    'deep_forest': "Deep Forest, Switzerland",
    'monza': "Monza, Italy",
    'red_bull_ring': "Red Bull Ring, Austria",
    'circuit_de_Sainte-Croix': "Circuit de Sainte-Croix, France",
    'dragon_trail': "Dragon Trail, Croatia",
    'sardegna': "Sardegna, Italy",
    'sardegna_windmills': "Sardegna Windmills, Italy",
    'circuit_de_barcelona': "Circuit de Barcelona, Spain",
    'autopolis': "Autopolis, Japan",
    'kyoto_driving_park': "Kyoto Driving Park, Japan",
    'broad_ben_raceway': "Broad Ben Raceway, Japan",
    'tokyo_expressway': "Tokyo Expressway, Japan",
    'suzuka': "Suzuka, Japan",
    'fuji_speedway': "Fuji Speedway, Japan",
    'mount_panorama': "Mount Panorama, Australia",
    'high_speed_ring': "High Speed Ring, Japan"
}


Cars = {
    'sf19_super_formula': {'Name': "SF19 Super Formula", 'Drivetrain': 'MR', 'Power': 633, 'Weight': 1455},
    'mercedes_amg_gt3_2020': {'Name': "Mercedes-AMG GT3 '20", 'Drivetrain': 'FR', 'Power': 613, 'Weight': 2833},
    'vgt_f1_1_gr_3': {'Name': "FT-1 VGT (Gr.3)", 'Drivetrain': 'FR', 'Power': 544, 'Weight': 2822},
    'f_type_gr_3': {'Name': "F-type Gr.3", 'Drivetrain': 'FR', 'Power': 552, 'Weight': 2756},
    '911_rsr_2017': {'Name': "911 RSR (991) '17", 'Drivetrain': 'MR', 'Power': 509, 'Weight': 2740},
    'sls_amg_gr_4': {'Name': "SLS AMG Gr.4", 'Drivetrain': 'FR', 'Power': 514, 'Weight': 3120},
    'sport_quattro_s1_pikes_peak_1987': {'Name': "Sport quattro S1 Pikes Peak '87", 'Drivetrain': '4WD', 'Power': 588, 'Weight': 2205},
    'mercedes_amg_gt_black_series_2020': {'Name': "Mercedes-AMG GT Black Series '20", 'Drivetrain': 'FR', 'Power': 719, 'Weight': 3395},
    'ford_gt_2006': {'Name': "Ford GT '06", 'Drivetrain': 'MR', 'Power': 549, 'Weight': 3199},
    'sls_amg_10': {'Name': "SLS AMG 10", 'Drivetrain': 'FR', 'Power': 570, 'Weight': 3571},
    'gr_supra_race_car_2019': {'Name': "GR Supra Race Car '19", 'Drivetrain': 'FR', 'Power': 394, 'Weight': 3042},
    '205_turbo_15_evolution_2_1986': {'Name': "205 Turbo 15 Evolution 2 '86", 'Drivetrain': '4WD', 'Power': 448, 'Weight': 2006},
    'focus_gr_b_rally_car': {'Name': "Focus Gr.B Rally Car", 'Drivetrain': '4WD', 'Power': 538, 'Weight': 2778},
    'taycan_turbo_s_2019': {'Name': "Taycan Turbo S '19", 'Drivetrain': '4WD', 'Power': 751, 'Weight': 5060},
    'diablo_gt_2000': {'Name': "Diablo GT '00", 'Drivetrain': 'MR', 'Power': 571, 'Weight': 3285},
    'camaro_zl1_1le_package_18': {'Name': "Camaro ZL1 1LE Package 18", 'Drivetrain': 'FR', 'Power': 649, 'Weight': 3818}
}


# Add column headings as global variables
column_headings = ['Track', 'Driver', 'Car', 'Lap Time']


def assign_car_driver_track(Drivers, Tracks) -> tuple:
    """
    Assigns a car to each driver and a track to race on.
    """
    random.shuffle(Drivers)
    selected_track = random.choice(list(Tracks.keys()))
    car = random.randint(1, 82) 
    
    print(f"Drivers: {Drivers}")
    print(f"Selected Track: {Tracks[selected_track]}")
    print(f"Selected Car: {car}")

    return Drivers, selected_track, car


def record_race_results(Drivers, selected_track, car):
    """
    Records the race results in a CSV file without duplicating headers.
    """
    file_exists = os.path.isfile('race_results.csv')  # Check if file already exists

    race_results = []
    
    # Collect results for each driver
    for driver in Drivers:
        lap_time = input(f"Enter lap time for {driver}: ")
        race_results.append([selected_track, driver, car, lap_time])
    
    # Create DataFrame
    df = pd.DataFrame(race_results, columns=column_headings)
    
    # Append to CSV, write headers only if file doesn't exist
    df.to_csv('race_results.csv', mode='a', header=not file_exists, index=False)
    
    print("Race results recorded successfully.")


def main():
    for i in range(8):
        drivers, track, car = assign_car_driver_track(Drivers, Tracks)
        record_race_results(drivers, track, car)


if __name__ == "__main__":
    main()
