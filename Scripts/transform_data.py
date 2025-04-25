# %%
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# %%
try:
    logging.info('calculating...')
    def calculate_average_rentals(path):
        # Load the cleaned dataset
        df = pd.read_csv(path)

        # Calculate average rentals per season
        avg_by_season = df.groupby("season")["total_rentals"].mean().reset_index()

        # Rename columns for clarity
        avg_by_season.columns = ["Season", "Average_Rentals"]

        return avg_by_season
    logging.info('calculating done')
except Exception as e:
    logging.error(f'calculation failed: {e}')
# Run this only if the script is executed directly
#if __name__ == "__main__":
   # result = calculate_average_rentals("C:/Work/data engineer/projects/share-bike-demand/output/cleanning-data.csv")
   # result.to_csv("C:/Work/data engineer/projects/share-bike-demand/output/transforming_data.csv", index=False)
   # print("Report generated.")
# %%
