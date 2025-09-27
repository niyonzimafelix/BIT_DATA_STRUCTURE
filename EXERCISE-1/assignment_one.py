import array as arr   # For Arrays
# 1. INTEGERS
sensor_readings = [45, 67, 89, 34, 56, 78, 90, 23, 50]

total = sum(sensor_readings)
average = total / len(sensor_readings)
minimum = min(sensor_readings)
maximum = max(sensor_readings)

print(" INTEGERS")
print("Total:", total) 
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
# 2. STRINGS
report = f"IoT Sensor Report:\nTotal = {total}, Average = {average:.2f}\nMin = {minimum}, Max = {maximum}"
print("\n STRINGS ")
print(report)
# 3. BOOLEANS
threshold = 60
status = "Above Standard" if average > threshold else "Below Standard"
compound_status = average > threshold and maximum > 80

print("\nBOOLEANS ")
print("Status:", status)
print("Compound Status Condition Met:", compound_status)
# 4. LISTS
print("\nLISTS ")
print("Original List:", sensor_readings)
# Add new reading
sensor_readings.append(72)
# Remove readings below 30
sensor_readings = [x for x in sensor_readings if x >= 30]
# Sort readings
sensor_readings.sort()
print("Modified & Sorted List:", sensor_readings)
# 5. ARRAYS
sensor_array = arr.array('i', [45, 67, 89, 34, 56, 78, 90, 23, 50])
array_sum = sum(sensor_array)

print("\nARRAYS ")
print("Array Elements:", sensor_array.tolist())
print("Array Sum:", array_sum)
print("List Sum:", total)
print("Comparison (Array vs List):", array_sum == total)
# 6. DICTIONARIES
sensor_records = [
    {"id": 1, "name": "Sensor-A", "value": 45},
    {"id": 2, "name": "Sensor-B", "value": 67},
    {"id": 3, "name": "Sensor-C", "value": 89},
]
print("\nDICTIONARIES ")
print("Original Records:")
for record in sensor_records:
    print(record)

# Update one record
sensor_records[1]["value"] = 75   # Update Sensor-B
# Delete another record
del sensor_records[0]  # Remove Sensor-A

# Add a new record
sensor_records.append({"id": 4, "name": "Sensor-D", "value": 55})

# Compute total value across all records
total_values = sum(record["value"] for record in sensor_records)

print("\nUpdated Records:")
for record in sensor_records:
    print(record)

print("\nTotal Values Across Records:", total_values)