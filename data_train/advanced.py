import cv2
import numpy as np
import os
import pandas as pd
import json

def get_advanced_task_solution(image_path, training_data):
    """
    Calculates the sum of numbers on colored dice.

    Args:
        image_path (str): Path to the image.
        training_data (dict): Dictionary containing training data (e.g., number templates).

    Returns:
        int: The sum of numbers on all dice.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding to get a binary image
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the dice
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_numbers = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Adjust this threshold based on your image data
            # Get the bounding box for the contour
            x, y, w, h = cv2.boundingRect(contour)
            roi = image[y:y+h, x:x+w]

            # Use template matching to recognize the number on the dice
            recognized_number = recognize_number(roi, training_data)
            total_numbers += recognized_number

    return total_numbers

def recognize_number(roi, training_data):
    """
    Recognizes the number on the dice using template matching.

    Args:
        roi (numpy.ndarray): Region of interest containing the dice.
        training_data (dict): Dictionary containing number templates.

    Returns:
        int: Recognized number.
    """
    # Convert ROI to grayscale
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi_thresh = cv2.threshold(roi_gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Initialize variables to store the best match
    best_match = -1
    best_score = 0

    # Loop through each template in the training data
    for number, template in training_data.items():
        # Resize template to match the ROI size
        template_resized = cv2.resize(template, (roi.shape[1], roi.shape[0]))

        # Match the template
        result = cv2.matchTemplate(roi_thresh, template_resized, cv2.TM_CCOEFF_NORMED)
        _, score, _, _ = cv2.minMaxLoc(result)

        # Update best match if the score is better
        if score > best_score:
            best_score = score
            best_match = number

    return best_match if best_match != -1 else 0  # Return 0 if no match found

if __name__ == "__main__":
    # Example usage
    image_folder = 'data_train/advanced'
    results = []

    # Load training data for number templates
    with open('labels_advanced.json', 'r') as f:
        training_data = json.load(f)

    # Convert training data templates to numpy arrays
    for key in training_data.keys():
        training_data[key] = cv2.imread(training_data[key], cv2.IMREAD_GRAYSCALE)

    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, filename)
            total_numbers = get_advanced_task_solution(image_path, training_data)
            results.append({'image': filename, 'total_numbers': total_numbers})

    # Save results to CSV
    df = pd.DataFrame(results)
    df.to_csv('advanced_predictions.csv', index=False)
    print("Advanced predictions saved to advanced_predictions.csv")