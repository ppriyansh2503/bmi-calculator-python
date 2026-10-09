# BMI Calculator (Python)

A beginner-friendly command-line BMI Calculator built with Python.

## Features

- Takes weight in kilograms and height in metres.
- Calculates BMI using `weight / (height * height)`.
- Displays the result rounded to two decimal places.
- Classifies the result as Underweight, Normal, Overweight, or Obese.
- Handles non-numeric, zero, and negative inputs.

## Requirements

- Python 3.9 or newer
- No external libraries required

## How to Run

1. Install Python if it is not already installed: https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python bmi_calculator.py
   ```

   On some systems, use `python3 bmi_calculator.py`.

## Example

For weight `65` kg and height `1.70` m, the BMI is approximately `22.49`, classified as `Normal`.

## BMI Categories

| BMI | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 to below 25 | Normal |
| 25 to below 30 | Overweight |
| 30 or above | Obese |

These are general screening ranges, not a medical diagnosis.

## Learning Reference

- Python Tutorial: https://docs.python.org/3/tutorial/
