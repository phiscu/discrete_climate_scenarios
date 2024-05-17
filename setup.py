from setuptools import setup, find_packages

setup(
    name='discrete_climate_scenarios',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.28.2',
        'tqdm==4.65.0',
        'bias_correction==0.4',
        'matplotlib-base==3.7.1',
        'matplotlib-inline==0.1.6',
        'pandas==1.5.3',
        'shapely==2.0.1',
        'pyproj==3.4.1',
        'numpy==1.23.5',
        'geopandas==0.12.2',
        'geopandas-base==0.12.2',
        'geemap==0.19.6',
        'earthengine-api==0.1.346',
        'ee_extra==0.0.15',
        'eerepr==0.0.4',
        'pickleshare==0.7.5',
        'retry==0.9.2',
        'seaborn==0.11.2',
        'probscale==0.2.5'
    ],
    entry_points={
        'console_scripts': [
            'discrete_climate_scenarios=discrete_climate_scenarios.main_script:main',
        ],
    },
    author='Phillip Schuster',
    description='A package for downloading, processing, and bias adjusting CMIP6 climate scenario data for individual weather station locations.',
    url='https://github.com/phiscu/discrete_climate_scenarios',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

