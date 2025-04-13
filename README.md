# Hackathon: Object Detection in Images
My description are in the end

### Difficulty Levels
1. **Basic Level**
- **Objects**: Black dice with white dots
- **Task**: Calculate the sum of points on all dice
- **Output**: Single number (sum)

Examples: 
<p float="center">
<img src="data_train/basic/1.jpg" width="40%" height="40%"/>
<img src="data_train/basic/15.jpg" width="40%" height="40%"/>
</p>

## Data
- **Format**: Images in `.jpg`
- **Resolution**: 3472x4624 px
- **Background**: uniform light and uniform black
- **Training data** is given to the participants and is located in the folder [data_train/basic](data_train/basic) and [data_train/advanced](data_train/advanced). Labels are in [labels_basic.json](data_train\labels_basic.json) and [labels_advanced.json](data_train\labels_advanced.json)
- **Test data** is not given to the participants. The solution will be tested on a combination of training and testing sets.

## Rules
✅ **Allowed**:
- **Any computer vision libraries** (OpenCV, scikit-image etc)
- **Classical** image processing algorithms (Filters, Thresholding, Affine Transformations and so on)

Attention please!!!
1. Execute your `solution_pipeline.py` file as follows: `python solution_pipeline.py --dir data_train`;!!!dir data_train!!!,please note `python solution_pipeline.py --dir data_train`!!!
Only use this code can exeute my `solution_pipeline.py` successfully!!!
2. Get one file: `base_predictions.csv`

## Solution Description
1. **Read the Image**: Read the image in grayscale mode to reduce the complexity of subsequent processing.
2. **Preprocess the Image**: Use simple threshold processing to convert the image into a binary image, separating the dice from the background.
3. **Detect the Dice**: Detect the dice in the image by finding contours, and simply filter out small contours.
4. **Count the Points**: Create a mask for each detected die, and count the number of white pixels within the mask as the number of points.
5. **Calculate the Total**: Add up the points of all the dice to obtain the final result.