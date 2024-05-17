# Discrete Climate Scenarios

Discrete Climate Scenarios is a Python repository designed to facilitate the download, processing, and bias adjustment of CMIP6 climate scenario data for individual weather station locations. This repository provides tools to streamline the retrieval of climate data and prepare it for further analysis at specific geographic locations.

## Features

- **Data Download**: Automatically fetches CMIP6 climate scenario data from Google Earth Engine for user-specified time periods.
- **Data Processing**: Filters, cleans, and preprocesses the downloaded climate data to ensure consistency and accuracy.
- **Bias Adjustment**: Implements scaled distribution mapping for bias adjustment between observed and modeled climate data.
- **Station-Specific Analysis**: Generates climate scenarios tailored to individual weather station locations, allowing for localized climate analysis and impact assessments.
- **Visualizations**: Creates figures to assess impact and performance of the bias adjustment.

## Installation

To install the Discrete Climate Scenarios package, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/discrete_climate_scenarios.git
    cd discrete_climate_scenarios
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the package:
    ```bash
    pip install .
    ```

## Usage

1. Set up your configuration:
    - Create a `config.ini` file with the following content:
        ```ini
        [settings]
        input_dir = /path/to/your/input_dir
        output_dir = /path/to/your/output_dir
        buffer_radius = 2000
        show = True
        sd_factor = 2
        processes = 30
        download = True
        load_backup = False
        start_region_index = 0
        start_station_index = 0
        ```

2. Prepare your input directory structure:
    - The input directory should contain subdirectories for each region. Each region subdirectory should have two types of `.xlsx` files: precipitation data and temperature data. Each `.xlsx` file should have three time columns (year, month, day) and one column per weather station.
    - Additionally, each region subdirectory should contain a `aws_coords.csv` file with the station coordinates, formatted as follows:
        ```csv
        Name,Latitude,Longitude
        Pskem,41.97372000000,70.45579700000
        Chorvoq,41.61610000000,70.03475800000
        Oygaing,42.15526200000,70.86313900000
        Chimyon,41.52359600000,70.02613100000
        ```

3. Run the main script:
    ```bash
    python main.py
    ```

## Google Earth Engine

This package utilizes the Google Earth Engine and its Python API to download climate data. Ensure you have set up your Google Earth Engine account and authenticated your environment.

## Data Source

The package downloads data from the "NEX-GDDP-CMIP6: NASA Earth Exchange Global Daily Downscaled Climate Projections" dataset. More information can be found [here](https://developers.google.com/earth-engine/datasets/catalog/NASA_GDDP-CMIP6).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is part of the CLIMWATER project funded by the German Ministry for Education and Research (BMBF). It makes use of data from the [CMIP6](https://esgf-node.llnl.gov/projects/cmip6/) (Coupled Model Intercomparison Project Phase 6) archive.

