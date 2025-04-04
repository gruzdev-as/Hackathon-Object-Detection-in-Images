# Hackathon: Object Detection in Images

## Task Description
You need to solve two tasks of object detection in images with their properties extraction **without using machine learning models**:

### Difficulty Levels
1. **Basic Level**
- **Objects**: Black dice with white dots
- **Task**: Calculate the sum of points on all dice
- **Output**: Single number (sum)

2. **Advanced Level**
- **Objects**: Colored dice with numbers (the style is the same for all test images)
- **Task**: Calculate the sum of numbers on all dice
- **Output**: Single number (sum)

## Data
- **Format**: Images in `.jpg`
- **Features**:
- **Resolution**: 3472x4624 px
- **Background**: uniform light (5 photos) and uniform black (5 photos)
- **Training data** is given to the participants and is located in the folder [data_train/basic](data_train/basic) and [data_train/advanced](data_train/advanced)
- **Test data** is not given to the participants. The solution will be tested on a combination of training and testing sets

## Rules
✅ **Allowed**:
- **Any computer vision libraries** (OpenCV, scikit-image)
- **Classical** image processing algorithms

❌ **Prohibited**:
- **Neural networks** and **ML models** (including pre-trained)
- **Manual labeling** of test data

## Solution requirements
1. **Format**:
- Implement your own implementations of the `get_base_task_solution()` and `get_advanced_task_solution()` methods in the [solution_pipeline.py](solution_pipeline.py) file. DO NOT TOUCH other contents of the file (argparse, etc.)! You can break the project structure to any level of branching and imports, but I will test your solution as follows:

1. Call your `solution_pipeline.py` file as follows: `python solution_pipeline.py --dir data`;
2. Get two files: `base_predictions.csv`, `advanced_predictions.csv`;
3. Measure metrics for the basic and advanced tasks (more on this later).

- Checkout a git repository: attach a `requirements.txt` file so I can install the necessary libraries and checkout a `README.MD` file: describe your solution.

2. **Submission**:
- Send a link to your git repository to [mail](gruzdev-as@yandex.ru) before **April 27, 2025, 23:59 Moscow time** (don't forget to open the repository)

## Evaluation
**Metric**:
- `MAE` (mean absolute error between the predicted and true sum)
- If MAE is tied: the solution with **shorter execution time** wins

## Determining the winners:

**The winners will be selected based on the following principles:**
- **Top 3 solutions** by metric on the "Basic Level" task
- **Top 3 solutions** by metric on the "Advanced Level" task

If a participant got into both tops, then he is taken into account only in one top (the one in which he took the best place). If he took first place in both tops, then only his place in the "Advanced Level" top is taken into account.

If no working solution is received for the "Advanced Level" problem, the top 5 participants of the "Basic Level" will become the winners. The solution is considered working if `MAE < naive_prediction` (average for the test set)

## Prizes for the winners

**The winners receive:**
- **In case of top-3**: +25, +20, +15 points for the count, respectively;
- **In case of top-5**: +25, +20, +15, +10, +10 points for the count, respectively;

Winners will also be invited to a 🍕🍕 **pizza afterparty** 🍕🍕 (pizza on me)

**Participants who don't make it to the top will receive:**

- First quartile (top 25%) +7 points to the score
- Second and third quartiles (top 25% - top 75%) +5 points to the score
- Fourth quartile (bottom 25%) +3 points to the score