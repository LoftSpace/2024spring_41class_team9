import pandas as pd
import geocoder

def get_system_values():
    # number of logical core
    total_core_num = 22
    core_num = 1

    # Get memory size in GB
    mem_available = 0.6

    # Get carbon intensity for the current location
    g = geocoder.ip('me')
    CI_data = pd.read_csv('./CI_aggregated.csv')
    country = g.country
    CI = float((CI_data.query('index == @country')['in gCO2e/kWh']).values[0])

    # Save values to a file
    return {
        "core_num": core_num,
        "core_power": 150/total_core_num, # TDP
        "mem_num": mem_available,
        "mem_power": 0.3725,
        "PUE": 1.67,
        "CI": CI
    }

#print(get_system_value())
