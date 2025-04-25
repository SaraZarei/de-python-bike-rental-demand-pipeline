# %% 
import pandas as pd 
# %% 
from pathlib import Path
# %%
import logging
# %%
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# %%
# Create a Path object for a folder
base_path = Path('E:/Git/Data Engineering')
# %%
try:
    logging.info('cleaning data')
    def cleaning_dataset(input_path, output_path):
        df = pd.read_csv(input_path)
        # convert date to 3 columns
        if not pd.api.types.is_datetime64_any_dtype(df['dteday']):
            try:
                df['dteday'] = pd.to_datetime(df['dteday'])
                df['year']= df['dteday'].dt.year
                df['month'] = df['dteday'].dt.month
                df['day'] = df['dteday'].dt.day
            except Exception as e:
                print('Failed to convert "dteaday" to datetime')
                print('error detail:', e)
        
        # convert season to readable text
        df['season']= df['season'].map({1:'spring', 2:'summer', 3:'autumn', 4:'winter'})
        
        # Rename columns
        df.rename(columns = {'cnt': 'total_rentals'}, inplace= True)
        df.to_csv(output_path, index = False)

        logging.info('cleaning done')

except Exception as e:
    logging.error(f'cleaning failed: {e}')

# Usage
if __name__ == '__main__':

    input_path = base_path /"input"/"day.csv"
    clean_input_path = base_path/"output"/"cleaning-data.csv"
    cleaning_dataset(input_path, clean_input_path)

# %%
