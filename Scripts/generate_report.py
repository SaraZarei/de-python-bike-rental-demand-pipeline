import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
path_base = Path('E:/Git/Data Engineering/output')
# %%
import sys
import os
# Add the script's directory to Python path
sys.path.append(r"E:/Git/Data Engineering/Scripts")

# %%
from transform_data import calculate_average_rentals

if __name__ == "__main__":
    try:
        logging.info('starting...')
        input_path = path_base/'cleaning-data.csv'
        result = calculate_average_rentals(input_path)
        print("📊 Average Rentals by Season:")
        print(result)
    except Exception as e:
        logging.error(f'failed: {e}')
 

# %%
