# IoT Sensor Data Analysis

## Overview
This Python project demonstrates basic data handling and analysis of IoT sensor readings. It covers operations on integers, strings, booleans, lists, arrays, and dictionaries. The goal is to illustrate how sensor data can be processed, analyzed, and reported programmatically.

---

## Features

1. **Integers**
   - Computes total, average, minimum, and maximum of sensor readings.
   - Example output:
     ```
     Total: 532
     Average: 59.11
     Minimum: 23
     Maximum: 90
     ```

2. **Strings**
   - Generates a formatted report summarizing sensor data.
   - Example report:
     ```
     IoT Sensor Report:
     Total = 532, Average = 59.11
     Min = 23, Max = 90
     ```

3. **Booleans**
   - Evaluates sensor performance against a threshold.
   - Determines if the average exceeds the standard and if the maximum reading is high.
   - Example:
     ```
     Status: Below Standard
     Compound Status Condition Met: True
     ```

4. **Lists**
   - Demonstrates adding, removing, and sorting sensor readings.
   - Example output:
     ```
     Original List: [45, 67, 89, 34, 56, 78, 90, 23, 50]
     Modified & Sorted List: [34, 45, 50, 56, 67, 72, 78, 89, 90]
     ```

5. **Arrays**
   - Uses the `array` module for integer arrays.
   - Compares sums of array elements vs list elements.
   - Example output:
     ```
     Array Elements: [45, 67, 89, 34, 56, 78, 90, 23, 50]
     Array Sum: 532
     Comparison (Array vs List): True
     ```

6. **Dictionaries**
   - Stores detailed sensor records in dictionaries.
   - Supports updating, deleting, and adding records.
   - Computes the total values across all records.
   - Example:
     ```
     Updated Records:
     {'id': 2, 'name': 'Sensor-B', 'value': 75}
     {'id': 3, 'name': 'Sensor-C', 'value': 89}
     {'id': 4, 'name': 'Sensor-D', 'value': 55}

     Total Values Across Records: 219
     ```

---

## How to Run

1. Ensure Python 3.x is installed on your system.
2. Save the code in a file named `iot_sensor_analysis.py`.
3. Run the file using:
   ```bash
   python iot_sensor_analysis.py
