# Railway Ticket Sales & Performance Analytics Dashboard
## 1. Executive Summary
This project is focused on data analytics for the National Rail in the UK, concentrating on ticket sales and train performance from January to April 2024. The key objective was to understand the passenger demand, determine the time frames for peak travel, and revenue share on it, and diagnose on the time performance.
The dataset for the ticket sales was taken from the Maven Rail Challenge. The mock dataset as part of the National Rail ticket sales had 18 columns and was increased to 25 columns through Exploratory Data Analysis (EDA) and feature engineering by adding important attributes like Hour, DayOfWeek, DelayMinutes, and HourBin. These changes enabled better understanding of the travel and performance data.
The performance and ticket sales forecaster dashboard were powered by Python, Pandas, NumPy, Plotly, and Streamlit to allow data users to engage in the structure by providing filters for specific routes and days of the week, and the ability to visualize real-time and historical performance data on key metrics. The analysis enables identification of the most popular routes, weekday peak hours for travel, class and type on tickets sold, and reasons to time delays and cancellations.
## 2. Problem Statement
National Rail requires a business intelligence tool that enables decision makers to:
•	Identify the most popular and high demand routes.

•	Identify peak travel periods within the week and across differing time slots.

•	Break down revenue by category of tickets and by classes.

•	Assess punctuality and determine the reasons and sources of delays and cancellations.

Without these insights, it would not be possible to allocate resources optimally, schedule effectively, and enhance the experience of the passengers.
## 3. Goals
The goals of the project will be:

•	Establish the top-selling train routes.

•	Identify the peak travel periods by the day and time.

•	Assess ticket revenue by type and class.

•	Evaluate punctuality and identify the delays and cancellations.
## 4. Dataset
•	Source: Dataset pulled from the Maven Rail Challenge (mock datasets simulating ticket sales for the National Rail for the period January to April 2024).
•	Initial Size:18 columns containing information on ticket sales and journeys.
•	Expanded Size: The size was increased to 25 columns after cleaning the data and feature engineering, which included creating new variables such as:

Hour: from journey duration.

DayOfWeek: from journey start dates.

DelayMinutes: the difference between scheduled and actual minutes of arrival.

HourBin: defined time periods for peak time assessments.

This more comprehensive dataset better addresses the business questions, matching the challenge’s expectations.
## 5. Methodology  
The methodology consists of the following steps:  
a)	Data Cleaning & Preparation: Removing duplicates and standardizing categorical fields while addressing issues for missing values.  

b)	 Feature Engineering: Forming new variables (Hour, DayOfWeek, DelayMinutes, HourBin) to facilitate further analysis.  

c)	Exploratory Data Analysis (EDA): Describing and visually formatting statistics to identify the meaning of the data through patterns or anomalies in it and more.  

d)	 Dashboard Development:  
•	Using Python Pandas NumPy Plotly and Streamlit modules.  
•	Total journeys (KPI): Delayed journeys, cancelled journeys, and average delay.  
•	Top routes (bar chart), journey status (pie chart), time & day stacked bar (revenue), bar (reasons for delay/cancellation) and heatmap of journeys.  
## 6. Expected Deliverables  
•	Streamlit interactive: BI Dashboard.  

•	Project Report: containing methodology, analysis and findings.  

•	Presentation & Demo: covering insights and dashboard functionality.  

•	Data enabled: Business Recommendations (route scheduling, optimize delay) for further analysis.  
## 7. Expected Outcomes  
The project aims to supply decision makers with:  

•	Identification of routes with high demand periods.

•	Contribution of ticket types and classes to overall revenue.  

•	Analysis of the main causes of delays and cancellations.  

•	Suggestions to improve service and operational efficiency as well as passenger satisfaction.

## 8. Acknowledgements
First and foremost, we appreciate the invaluable guidance from our instructor and the diverse contributions from each team member while preparing this proposal. This project aims to use open-source software tools and the Maven Rail Challenge Dataset to demonstrate practical applications for Business Intelligence.


