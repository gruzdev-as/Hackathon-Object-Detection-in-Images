import cv2
import numpy as np
import os
import pandas as pd

def get_base_task_solution(image_path):
    """
    Calculates the sum of points on black dice with white dots.

    Args:
        image_path (str): Path to the image.

    Returns:
        int: The sum of points on all dice.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Contour Detection
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_points = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Adjust this threshold based on your image data
            # This is likely a dice, now find dots inside
            x, y, w, h = cv2.boundingRect(contour)
            dice_roi = gray[y:y+h, x:x+w]
            
            # Threshold the dice ROI
            _, dice_thresh = cv2.threshold(dice_roi, 127, 255, cv2.THRESH_BINARY_INV)
            
            # Find contours of the dots
            dot_contours, _ = cv2.findContours(dice_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            num_dots = 0
            for dot_contour in dot_contours:
                dot_area = cv2.contourArea(dot_contour)
                if dot_area > 20:  # Adjust this threshold based on your image data
                    num_dots += 1
            
            total_points += num_dots

    return total_points

if __name__ == "__main__":
    # Example usage
    image_folder = 'data_train/basic'
    results = []

    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, filename)
            total_points = get_base_task_solution(image_path)
            results.append({'image': filename, 'total_points': total_points})

    # Save results to CSV
    df = pd.DataFrame(results)
    df.to_csv('base_predictions.csv', index=False)
    print("Base predictions saved to base_predictions.csv")