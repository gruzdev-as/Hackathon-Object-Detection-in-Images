import argparse
import os

from typing import List
from pathlib import Path, PosixPath

import numpy as np 
import pandas as pd

import cv2

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

    # get folders for the base task
    dir_path = Path(image_dir)
    if not dir_path.exists():
        print(f"Error: path '{image_dir}' does not exist.")
        return
    if not dir_path.is_dir():
        print(f"Error: path '{image_dir}' is not a dir.")
        return
    
    base_img_path_list = os.listdir(dir_path / 'basic')

    base_predictions = get_base_task_solution(path=base_img_path_list)
    base_predictions.to_csv('base_predictions.csv')
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
    predictions = []
    for img_path in path:
        try:
            img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
            _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            total_points = 0
            for cnt in contours:
                if cv2.contourArea(cnt) > 100:  # Simple filtering of small contours
                    mask = np.zeros_like(thresh)
                    cv2.drawContours(mask, [cnt], -1, 255, -1)
                    points = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
                    total_points += points

            predictions.append(total_points)
        except Exception as e:
            print(f"An error occurred while processing {img_path}.: {e}")
            predictions.append(0)
    
    # DO NOT CHANGE THE OUTPUT FORMAT
    df_answer = pd.DataFrame({
        'img': path,
        'prediction': predictions
    })

    return df_answer


if __name__ == "__main__":
    main()
