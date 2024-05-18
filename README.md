
# Vehicle Factory

## Overview
This project simulates a vehicle factory with the capability to create cars and motorcycles with specific requirements.

## Project Structure

vehicleFactory/
├── .venv/
├── module_name/
│ ├── init.py
│ ├── factory.py
│ ├── motorcycle.py
│ ├── car.py
├── test/
│ ├── init.py
│ ├── test_module_name.py
├── .gitignore
├── README.md


## Classes
- `Factory`: Abstract base class for `Car` and `Motorcycle`.
- `Car`: Represents a car with attributes like model name, fuel type, color, and number of doors.
- `Motorcycle`: Represents a motorcycle with attributes like model name and fuel type.

## Methods
- `change_model_name()`: Change the model name.
- `change_fuel_type()`: Change the fuel type.
- `change_color()`: Change the color of the car.
- `change_number_of_doors()`: Change the number of doors in the car.
- `print_car_count()`: Print the number of cars created.
- `print_motorcycle_count()`: Print the number of motorcycles created.

## Testing
Unit tests are provided in the `test` directory to cover various cases.

## Usage
Instantiate `Car` and `Motorcycle` objects, modify their attributes, and get the count of vehicles created.

## Submission
Submit the pull request by May 19, 2024, at 9:30 AM.
