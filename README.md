# Project Name: LAParkingCitations05

> Course: Big Data (44-517)

> Project Number: Group 5 

Developers:
- Zachary Haider
- Saivarun Illendula
- Samuel Gedwillo
- Aawaj Joshi

> Link to the repository: (https://github.com/Saivarun2185/MapReduceProject05.git)


> Link to the Issue Tracker: (https://github.com/Saivarun2185/MapReduceProject05/issues)

## Introduction:

This is our MapReduce Project which involves processing data from the city of Los Angeles parking citations database.  


## Data Source:
This data source contains information about the records of all the parking citations issued to people in the city of Los Angeles. This data source has been hosted by the city of Los Angeles.The data source is about 233MB and contains information from January, 2010 to November, 2018. The dataset we have chosen has structured data. 

>Link to the Data Source: [Los Angeles Parking Citations](https://www.kaggle.com/cityofLA/los-angeles-parking-citations)

## Challenges of the Data Source (The V's of Big Data):

The dataset we have chosen has a huge volume of data which keeps updateing daily signifying its velocity. The dataset is maintained by Kaggle and hosted by the city of Los Angeles which makes it trustworthy. The dataset has a wide variety of different field inputs like text and numerical data. This data is valuable as it helps in keeping track of parking violations in the city of Los Angeles from 2010 to now.  
 

## The Big Data Question:
- Saivarun Illendula: What is the total amount of fines collected for the violation of "NO STOP/STAND AM" from 2010 to 2018 in the city of LA ?


## Big Data Solutions:

1. Mapper Input:

- Saivarun Illendula: 

    | Ticket number | Issue Date          | Issue time | Meter Id | Marked Time | RP State Plate | Plate Expiry Date | VIN | Make | Body Style | Color | Location        | Route | Agency | Violation code | Violation Description | Fine amount | Latitude |
    |---------------|---------------------|------------|----------|-------------|----------------|-------------------|-----|------|------------|-------|-----------------|-------|--------|----------------|-----------------------|-------------|----------|
    | 1103341116    | 2015-12-21T00:00:00 | 1251       |          |             | CA             | 200304            |     | HOND | PA         | GY    | 13147 WELBY WAY | 1521  | 1      | 4000A1         | NO EVIDENCE OF REG    | 50          | 99999    |


2. Mapper Output:

- Saivarun Illendula: 

3. Reducer Output:

- Saivarun Illendula: 

4. Language:

- Saivarun Illendula: I  will use Python for performing the MapReduce Jobs.

5. Chart: 

- Saivarun Illendula: We will be using Bar Chart to represent our MapReduce outputs.





