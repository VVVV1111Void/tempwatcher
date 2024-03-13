import csv
import time
from utils import *
# Initialize the constants
SLEEP_TIME = 0.5  # Time in seconds, the script will wait before updating the CPU temperature
LOG_FILE = 'cpu_temp.csv'  # CSV file to store the temperature data

# Update the temperature array
def update(arr: list):
    temps = get_all_core_temps(4)
    if temps is not None:
        arr.append(temps)
    else:
        print('Invalid temperature value.')

# Save the temperature array into a CSV file
def save_temp(history):
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        for temps in history:
            writer.writerow(temps)
    print('CPU temperature saved into file.')

# Main loop
def main():
    temperature_history = []
    while True:
        update(temperature_history)
        if len(temperature_history) > 50:
            save_temp(temperature_history)
            temperature_history.clear()
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()