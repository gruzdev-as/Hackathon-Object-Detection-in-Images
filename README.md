# Hackathon: Object Detection in Images

## Problem Definition
You need to solve two tasks of object detection in images with their properties extraction **without using machine learning models**:

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

2. **Advanced Level**
- **Objects**: Colored dice with numbers (the style is the same for all test images)
- **Task**: Calculate the sum of numbers on all dice
- **Output**: Single number (sum)

Examples: 
<p float="center">
<img src="data_train/advanced/1.jpg" width="40%" height="40%"/>
<img src="data_train/advanced/15.jpg" width="40%" height="40%"/>
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

❌ **Prohibited**:
- **Neural networks** and **ML models** (including pre-trained)
- **Manual if else solution** for train data

## Solution requirements
1. **Format**:
- Implement your own implementations of the `get_base_task_solution()` and `get_advanced_task_solution()` methods in the [solution_pipeline.py](solution_pipeline.py) file.**DO NOT TOUCH** other contents of the file (argparse, etc.)! You can break the project structure to any level of branching and imports, but I will test your solution as follows:

1. Execute your `solution_pipeline.py` file as follows: `python solution_pipeline.py --dir data`;
2. Get two files: `base_predictions.csv`, `advanced_predictions.csv`;
3. Measure metrics for the basic and advanced tasks (more on this later).

- Properly design a git repository: attach a `requirements.txt` file so I can install the necessary libraries and include a `README.MD` file with the description of your solution.

2. **Submission**:
- Send a link to your git repository to [mail](gruzdev-as@yandex.ru) before **April 27, 2025, 23:59 Moscow time** (don't forget to open the repository. It's better to open it just before the deadline. Commits after the deadline won't be taken into account)

## Evaluation
**Metric**:
- `MAE` (mean absolute error between the predicted and true sum)
- If MAE is tied: the **faster** solution wins

## Determining the winners:

**The winners will be selected based on the following principles:**
- **Top 3 solutions** by metric on the "Basic Level" task
- **Top 3 solutions** by metric on the "Advanced Level" task

If a participant would get into both tops, then they will be taken into account only in one top (the one in which they would take the best place). If they would take first place in both tops, then only their place in the "Advanced Level" top is taken into account.

If no working solutions would be received for the "Advanced Level" problem, the top 5 participants of the "Basic Level" will become the winners. 

The solution is considered working if `MAE < naive_prediction` (average for the test set)

## Prizes for the winners

**The winners receive:**
- **In case of top-3**: +30, +25, +20 credit points, respectively;
- **In case of top-5**: +30, +25, +20, +15, +15 credit points, respectively;

Winners will also be invited to a 🍕🍕 **PIZZA AFTERPARTY** 🍕🍕 (pizza on me)

**Participants who don't make it to the top will receive:**

- First quartile (top 25%) +10 credit points
- Second and third quartiles (top 25% - top 75%) +7 credit points
- Fourth quartile (bottom 25%) +5 credit points