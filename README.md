# Project Name: LAParkingCitations05

> Course: Big Data (44-517)

> Project Number: Group 5 

## About our dataset 

Our data, hosted by the city of Los Angeles (LA), concerns parking citations issued in LA from 2015 - present. For each citation record, the citation number, issue date and time, meter id and marked time (if applicable), the registration state, plate expiry date, VIN, make, body style, and color of the vehicle, location of violation, route, violation code and description, and fine amount have been recorded. 

## Link to our dataset 

We obtained our dataset on [Kaggle](https://www.kaggle.com/). Here is the link to the raw dataset. 

https://www.kaggle.com/cityofLA/los-angeles-parking-citations

## Overview of our project

In this project, we create and compile our individual Mappers and Reducers to generate the output needed to answer our Big Data questions pertaining to the dataset. To summarize in a simple term, we run processes to generate mathematical computations such as count, maximum, and average.

## Implimentation:
Each of the sections has its own mapper.py and reducer.py ( and some have sorter.py). To run the code for each you need to have python 3.0 or higher. 

For each section start with its mapper.py by typeing the following commands into your commandline or terminal:
 
> python mapper.py
 
Then if it has a sorter.py run it with 

> python sorter.py

Finaly run the reducer.py with:

> python reducer.py

The results should be generated accordingly.


  

## Challenges of the Data Source (The V's of Big Data):

The dataset that we picked has a huge volume of data which is updated daily signifying a swift velocity. The dataset is maintained by Kaggle and hosted by the city of Los Angeles which makes it trustworthy. The dataset has a wide variety of different field inputs like text and numerical data. This data is valuable as it helps in keeping track of parking violations in the city of Los Angeles from 2010 to now.
 
## The Big Data Question:

- Zachary Haider: 
For each  car that let the meter expire how many cars of each color were there?

- Saivarun Illendula:
For each year from 2010 to 2018 what is the total number of fines for the violation of "NO STOP/STAND AM" in the city of LA ?

- Samuel Gedwillo:
What hour of the day has the most parking violations?

- Aawaj Joshi:
What was the average fine amount for black colored vehicles that received parking citations in LA? 

## Big Data Solutions:

### Zachary Haider:
##### 1. Mapper Input:
 

| Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude | Longitude |
|---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|-----------|
| 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    | 99999     |
##### 2. Mapper Output:
* GY, 1 

##### 3. Reducer Output:
-    GY, 2023

##### 4. Language:
I will use Python for performing the MapReduce Jobs.

##### 5. Chart: 
 I will be useing a bar chart for my data.
 
 ![chart](https://github.com/Saivarun2185/LAParkingCitations05/blob/master/Zachary%20Haider/chart.png?raw=true)
      


### Saivarun Illendula:

##### 1. Mapper Input:

| Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude | Longitude |
|---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|-----------|
| 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    | 99999     |

##### 2. Mapper Output:
* 2015, 50

##### 3. Reducer Output:
* 2015, 1500

##### 4. Language:
I also will use Python for performing the MapReduce Jobs.

##### 5. Chart: 
I will be using Bar Chart to represent our MapReduce outputs.

![barchart](https://user-images.githubusercontent.com/31701961/49250810-758c7600-f3e5-11e8-9f07-59791dd2e232.PNG)


### Samuel Gedwillo

#### 1. Mapper Input:

| Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude | Longitude |
|---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|-----------|
| 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    | 99999     |
##### 2. Mapper Output:
-  1200, 1

##### 3. Reducer Output:
- 1200, 300

##### 4. Language:

I am planning on using Python to execute my MapReduce job.

##### 5. Chart: 

I am planning on using a Bar Chart create a story for my data.

![barchart](https://github.com/Saivarun2185/LAParkingCitations05/tree/master/Samuel%20Gedwillo/chart.png?raw=true)


### Awaj Joshi:

#### 1. Mapper Input:

| Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude | Longitude |
|---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|-----------|
| 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    | 99999     |


##### 2. Mapper Output:
*  BK, 1

##### 3. Reducer Output:
* BK, 68
##### 4. Language:
I will be using Python to run my MapReduce jobs. 

##### 5. Chart: 
I will visualize my MapReduce outputs using a Bar Chart.

![barchart](https://github.com/Saivarun2185/LAParkingCitations05/blob/master/Aawaj%20Joshi/chart.png?raw=true)

## Authors 

**Zachary Haider**  
**Saivarun Illendula**  
**Samuel Gedwillo**  
**Aawaj Joshi**



