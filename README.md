# Zomato restaurant data analysis

With the given datasets, I focused on extracting restaurant details, event information, and determining rating thresholds.

## Prerequisites

- Python 3.8 or higher
- Pandas library
- Openpyxl library

## Installation

1. Clone the repository:

```
git clone https://github.com/rencongchia/DE-CC4-assessment.git
```

2. Navigate to the project directory:

```
cd DE-CC4-assessment
```

3. Install the required Python packages:

```
pip install pandas openpyxl
```

## Run scripts

Task 1 Part 1 - To extract restaurant data, run:
```
cd task_1_part_1
```
```
python extract_restaurants.py
```

Task 1 Part 2 - To extract restaurant events, run:
```
cd task_1_part_2
```
```
python extract_restaurant_events.py
```

Task 1 Part 3 - To determine rating thresholds, run:
```
cd task_1_part_3
```
```
python rating_threshold_aggregator.py
```

## Architecture Decisions
- The project is structured into separate scripts for each task to maintain modularity.
- Pandas is used for data manipulation as given dataset is in tabular form.
