import random
import csv

Drivers = ['Arya', 'Rishabh', 'Aditya', 'Sai']

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
    'deep_forest': "Deep Forest, Swuzerland",
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
    Records the race results in a CSV file.
    """
    race_results = []
        
    for driver in Drivers:
        lap_time = input(f"Enter lap time for {driver}: ")
        race_results.append([selected_track, driver, car, lap_time])
        
        with open('race_results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Track', 'Driver', 'Car', 'Lap Time'])
            writer.writerows(race_results)
        
        print("Race results recorded successfully.")


def main():

    drivers, track, car = assign_car_driver_track(Drivers, Tracks)
    record_race_results(drivers, track, car)

    

if __name__ == "__main__":
    main()