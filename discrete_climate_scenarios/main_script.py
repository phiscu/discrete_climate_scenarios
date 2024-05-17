# -*- coding: UTF-8 -*-

import os
import time
import warnings
import sys
import configparser
import matilda_functions as mf

warnings.filterwarnings("ignore")

def main():
    # Read configuration settings from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    settings = config['settings']

    # Extract settings from the configuration file
    input_dir = settings.get('input_dir')
    output_dir = settings.get('output_dir')
    buffer_radius = settings.getint('buffer_radius')
    show = settings.getboolean('show')
    sd_factor = settings.getint('sd_factor')
    processes = settings.getint('processes')
    download = settings.getboolean('download')
    load_backup = settings.getboolean('load_backup')
    start_region_index = settings.getint('start_region_index')
    start_station_index = settings.getint('start_station_index')

    # Preprocessing
    print('Initiating preprocessing routine')
    preprocessor = mf.StationPreprocessor(input_dir=input_dir, output_dir=output_dir, buffer_radius=buffer_radius,
                                          show=show, sd_factor=sd_factor)
    preprocessor.full_preprocessing()
    print('Set up preprocessing routine for target directory!')

    # Main loop
    start_total_time = time.time()
    total = mf.count_dataframes(preprocessor.region_data)

    for region_index, region in enumerate(preprocessor.region_data.keys()):
        if start_region_index is not None and region_index < start_region_index:
            continue

        for station_index, (station, data) in enumerate(preprocessor.region_data[region].items()):
            if start_station_index is not None and station_index < start_station_index:
                continue

            start_process_time = time.time()
            if region_index == 0:
                print(f'\n** Starting processing of Station {station_index+1} of {total}: "{station}"\n')
            else:
                print(f'\n** Starting processing of Station {station_index+6} of {total}: "{station}"\n')

            try:
                instance = mf.ClimateScenarios(output=f'{preprocessor.output_dir}{region}/{station}/',
                                               region_data=preprocessor.region_data, station=station, download=download,
                                               load_backup=load_backup, show=show, buffer_file=preprocessor.gis_file,
                                               processes=processes)
                instance.complete_workflow()
            except Exception as e:
                print(f"Error occurred for station {station}: {e}")
                continue  # Skip to the next station

            end_process_time = time.time()
            process_elapsed_time = end_process_time - start_process_time
            print(f'Processing time for station {station}: {round(process_elapsed_time/60, 2)} minutes')

        # Update the start_station_index after processing all stations in the current region
        start_station_index = None

        # If start_region_index is not set, update it to proceed to the next region
        if start_region_index is None:
            start_region_index = region_index

    # Reset the start_region_index after completing the loop
    start_region_index = None

    end_total_time = time.time()
    total_elapsed_time = end_total_time - start_total_time
    print('**************************************\n** COMPLETED **')
    print(f'Total processing time: {round(total_elapsed_time/60, 2)} minutes')

if __name__ == "__main__":
    main()

