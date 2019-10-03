# Probability Distribution
import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as plt
import viz
import pandas as pd

# 1.) A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. 
# Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

def cars_at_bank_at_noon():
    x = range(8)
    y = stats.poisson(2).pmf(x)

    plt.figure(figsize=(9, 6))
    plt.bar(x, y, edgecolor='black', color='white', width=1)
    plt.xticks(x)
    plt.ylabel('P(X = x)')
    plt.xlabel('Average cars at drive_up window')
print(cars_at_bank_at_noon())

# 1.a) What is the probability that no cars drive up in the noon hour?

stats.poisson(2).pmf(0)

# 1.b) What is the probability that 3 or more cars come through the drive through?

stats.poisson(2).sf(3)

# 1.c) How likely is it that the drive through gets at least 1 car?

stats.poisson(2).pmf(1)

# 2.) Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:

# 2.a) What grade point average is required to be in the top 5% of the graduating class?

stats.norm(3, .3).isf(.05)

# 2.b) What GPA constitutes the bottom 15% of the class?

stats.norm(3, .3).ppf(.15)

# 2.c) An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. 
# Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

stats.norm(3, .3).ppf(.3)
stats.norm(3, .3).ppf(.2)

# 2.d) If I have a GPA of 3.5, what percentile am I in?

stats.norm(3, .3).isf(.045)

# 3.) A marketing website has an average click-through rate of 2%. 
# One day they observe 4326 visitors and 97 click-throughs. 
# How likely is it that this many people or more click through?

stats.poisson().pdf(.02)
stats.binom(4326, .02).sf(97)

# 4.) You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.

# 4.a) What is the probability that at least one of your first 60 answers is correct?

stats.binom(60,.01).pmf(1)

# 5.) The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. How likely is it that the break area gets cleaned up each day? How likely is it that it goes two days without getting cleaned up? All week?
n_students = round(.9*66)

# cleanded every day
stats.binom(n_students, .03).sf(0)
# not cleaned two day
stats.binom(n_students, .03).pmf(2)
# not cleaned all week
stats.binom(n_students, .03).pmf(5)

# 6.) You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, 
# you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

mean = 15
std= 3
time_to_order = 2
lunch_hour = 60
eat_time = 15
prep_time = 10
wait_time = lunch_hour - mean * time_to_order - prep_time - eat_time
people = round((lunch_hour - eat_time - prep_time) // time_to_order)


lunch_line = stats.norm(15, 3).cdf(people)
lunch_line

# 7.) Connect to the employees database and find the average salary of current employees, along with the standard deviation. 
# Model the distribution of employees salaries with a normal distribution and answer the following questions:

def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

import env

from env import host, user, password

url = get_db_url(user,password, host, "employees")

url

# Read the salaries tables into a dataframes

salaries_query = "SELECT * FROM salaries WHERE to_date like '9999%%'"
salaries = pd.read_sql(salaries_query, url) 
(salaries.tail(25))

average_salary = salaries.salary.mean()

std_salary = salaries.salary.std()

salary_distribution = stats.norm(average_salary, std_salary)

# 7.a) What percent of employees earn less than 60,000?

percent_under_60k = salary_distribution.cdf(60000)

# 7.b) What percent of employees earn more than 95,000?

percent_above_95k = salary_distribution.sf(95000)

# 7.c) What percent of employees earn between 65,000 and 80,000?

percent_above_65k = salary_distribution.sf(65000)
percent_below_80k = salary_distribution.cdf(80000)

percent_between_65k_and_80k = percent_below_80k - percent_above_65k

# 7.d) What do the top 5% of employees make?

top_5%_salary = salary_distribution.isf(.05)