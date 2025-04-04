import argparse
import os

from typing import List
from pathlib import Path, PosixPath

import numpy as np 
import pandas as pd

parser = argparse.ArgumentParser(
    description="Solution Template",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "-dir", "--directory", 
    help="image directory path",
    type=str
)

args = parser.parse_args()
image_dir = args.directory

def main():

    # get folders for the base and advance task 
    dir_path = Path(image_dir)
    if not dir_path.exists():
        print(f"Error: path '{image_dir}' does not exist.")
        return
    if not dir_path.is_dir():
        print(f"Error: path '{image_dir}' is not a dir.")
        return
    
    base_img_path_list = os.listdir(dir_path / 'basic')
    advance_img_path_list = os.listdir(dir_path / 'advanced')

    base_predictions = get_base_task_solution(path=base_img_path_list)
    advanced_predictions = get_advanced_task_solution(path=advance_img_path_list)

    base_predictions.to_csv('base_predictions.csv')
    advanced_predictions.to_csv('advanced_predictions.csv')
    print('Predictions Generated Successfully!')

def get_base_task_solution(path: List[PosixPath]) -> pd.DataFrame:
    """ This function should return a pandas DataFrame with 
        predictions for the base task

    Args:
        path (List[PosixPath]): List of paths of base task images

    Returns:
        pd.DataFrame: Pandas Dataframe with two columns: 
            "img": path, 
            "prediction": prediction (int) for each image,  
    """
    # MAKE SURE TO IMPLEMENT YOUR OWN LOGIC 
    predict_array = np.random.randint(0, 50, size=len(path))
    
    # DO NOT CHANGE THE OUTPUT FORMAT
    df_answer = pd.DataFrame({
        'img': path,
        'prediction': predict_array
    })

    return df_answer

def get_advanced_task_solution(path: List[PosixPath]) -> pd.DataFrame:
    """ This function should return a pandas DataFrame with 
        predictions for the base task

    Args:
        path (List[PosixPath]): List of paths of base task images

    Returns:
        pd.DataFrame: Pandas Dataframe with two columns: 
            "img": path, 
            "prediction": prediction (int) for each image,  
    """
    
    # MAKE SURE TO IMPLEMENT YOUR OWN LOGIC 
    predict_array = np.random.randint(0, 50, size=len(path))
    
    # DO NOT CHANGE THE OUTPUT FORMAT
    df_answer = pd.DataFrame({
        'img': path,
        'prediction': predict_array
    })

    return df_answer

if __name__ == "__main__":
    main()