# Project Name: LAParkingCitations05

> Course: Big Data (44-517)

> Project Number: Group 5 

### Developers:
- Zachary Haider
- Saivarun Illendula
- Samuel Gedwillo
- Aawaj Joshi

> Link to the repository: (https://github.com/Saivarun2185/MapReduceProject05.git)

> Link to the Issue Tracker: (https://github.com/Saivarun2185/MapReduceProject05/issues)

## Introduction:

This is our MapReduce Project which involves processing data from the city of Los Angeles parking citations database.We will use the data set linked here to answer 4 difrent quietions about the answer.


## Data Source:
This data source is a csv file containing information about the records of all the parking citations issued to people in the city of Los Angeles. This data source has been hosted by the city of Los Angeles.The data source is about 233MB and contains information from January, 2010 to November, 2018. The dataset we have chosen has structured data. 

>Link to the Data Source: (https://www.kaggle.com/cityofLA/los-angeles-parking-citations)

## Challenges of the Data Source (The V's of Big Data):

The dataset we have chosen has a huge volume of data which keeps updateing daily signifying its velocity. The dataset is maintained by Kaggle and hosted by the city of Los Angeles which makes it trustworthy. The dataset has a wide variety of different field inputs like text and numerical data. This data is valuable as it helps in keeping track of parking violations in the city of Los Angeles from 2010 to now.
 
## The Big Data Question:

- Zachary Haider: 
How does the color of car correspond to the number of cars that let the meter expire?

- Saivarun Illendula:
For each year from 2010 to 2018 what is the total number of fines for the violation of "NO STOP/STAND AM" in the city of LA ?

- Samuel Gedwillo:
What hour of the day has the most parking violations?

- Aawaj Joshi:
What was the average fine amount for black colored vehicles between the years 2010 and 2015?

## Big Data Solutions:

### 1. Mapper Input:

- Everyone is useing the same dataset and therefor will have the same Mapper Input: 

    | Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude |
    |---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|
    | 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    |


### 2. Mapper Output:

- Zachary Haider:
    GY, 1 

- Saivarun Illendula:
    2015, 50

- Samuel Gedwillo:
    1200, 1

- Aawaj Joshi:
    BK, 1

### 3. Reducer Output:

- Zachary Haider:
    GY, 2023

- Saivarun Illendula: 
    2015, 1500

- Samuel Gedwillo:
    1200, 300

- Aawaj Joshi:
    BK, 68
    
### 4. Language:

- Zachary Haider: 
I will use Python for performing the MapReduce Jobs.

- Saivarun Illendula: 
I also will use Python for performing the MapReduce Jobs.

- Samuel Gedwillo:
I am planning on using Python to execute my MapReduce job.

- Aawaj Joshi:
I will be using Python to run my MapReduce jobs. 

### 5. Chart: 

- Zachary Haider:
 I will be useing a pie chart for my data.

- Saivarun Illendula: 
I will be using Bar Chart to represent our MapReduce outputs.

- Samuel Gedwillo:
I am planning on using a Bar Chart create a story for my data.

- Aawaj Joshi: 
I will visualize my MapReduce outputs using a Bar Chart.





