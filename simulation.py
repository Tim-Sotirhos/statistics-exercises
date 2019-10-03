# Simulation Exercises

import pandas as pd
import numpy as np

np.random.seed(3)
# 1.) How likely is it that you roll doubles when rolling two dice?

n_trials = 10000
n_dice_rolled = 2
rolls = np.random.choice([1,2,3,4,5,6], (n_trials, n_dice_rolled))
pairs = pd.DataFrame(rolls)
pairs.apply(lambda x: x[0] == x[1], axis = 1).mean()
# 16.34% of rolling doubles

# Alternative approach
rolls = np.random.randint(1,7, (10000, 2))
(rolls[:, 0] == rolls[:, 1]).mean()

# 2.) If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# Exactly 3 heads
n_trials = 1000
n_coins = 8
eight_flips = np.random.choice([0,1], (n_trials, n_coins))
pairs = pd.DataFrame(eight_flips)
pairs['three_heads'] = pairs.sum(axis = 1) == 3
pairs.three_heads.mean()

# Alternative approach

flips = np.random.choice(["Heads", "Tails"], (10000, 8))
((flips == "Heads").sum(axis=1) == 3).mean()
((flips == "Heads").sum(axis=1) > 3).mean()


# More than 3 heads
n_trials = 10000
n_coins = 8
eight_flips = np.random.choice([0,1], (n_trials, n_coins))
pairs = pd.DataFrame(eight_flips)
pairs['three_heads'] = pairs.sum(axis = 1) > 3
pairs.three_heads.mean()

# Alternative approach

flips = np.random.choice(["Heads", "Tails"], (10000, 8))
((flips == "Heads").sum(axis=1) > 3).mean()

# 3.) There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

probability = .25

ds_students = np.random.random((10000,2)) <= probability
ds_students.sum(axis=1)
yes_billboard = (ds_students.sum(axis = 1) == 2).mean()

# Alternative approach

options = ['Web Dev'] * 3 + ['Data Science']
(((np.random.choice(options, (10_000, 2)) == 'Data Science').sum(axis=1)) == 2).mean()



# 4.) Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

poptarts = np.round(np.random.normal(3, 1.5, (100000, 5)))
poptarts = np.where(poptarts < 0, 0, poptarts)
poptarts = pd.DataFrame(poptarts)
poptarts['count'] = poptarts.sum(axis=1) < 17
poptarts['count'].mean()

# Alternative approach

n = 10_000

pt_consumption = np.round(np.random.normal(3, 1.5, (n, 5)))
pt_consumption = np.where(pt_consumption < 0, 0, pt_consumption)
(pt_consumption.sum(axis=1) < 17).mean()

# 5.) Compare Heights
'''
Men have an average height of 178 cm and standard deviation of 8cm.
Women have a mean of 170, sd = 6cm.
'''

# 5) If a man and woman are chosen at random, P(woman taller than man)?

man = list(np.random.normal(178, 8, (10000,1)))
woman = list(np.random.normal(170, 6, (10000,1)))
man = [m[0] for m in man]
woman = [w[0] for w in woman]
height = pd.DataFrame({'men_height' : man, 'woman_height' : woman})
height['woman_taller'] = height.men_height < height.woman_height
height.woman_taller.mean()

# Alternative approach

n = 10000

male_heights = np.random.normal(178, 8, n)
female_heights = np.random.normal(170, 6, n)

(female_heights > male_heights).mean()

# 6.) When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

# 50 trials

n = 10000

p_corrupt = 1/250

1 - (np.random.random((n, 50)) < p_corrupt).sum(axis=1).mean()

# 100 trials

n = 10000

p_corrupt = 1/250

((np.random.random((n, 100)) < p_corrupt).sum(axis=1) == 0).mean()

# 6.a ) What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# 150 trials

((np.random.random((n, 150)) < p_corrupt).sum(axis=1) > 0).mean()

# 6.b) How likely is it that 450 students all download anaconda without an issue?

((np.random.random((n, 450)) < p_corrupt).sum(axis=1) == 0).mean()

# 7.) There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. 
# How unlikely is this?

n = 10_000
# Food truck arrives
p_food_truck = .7
# Food truck missing
p_no_food_truck = 1 - p_food_truck

lunches = np.random.choice(['Food Truck', 'No Food Truck'], (n, 3), p=[p_food_truck, p_no_food_truck])
lunches == "No Food Truck"
(lunches == "No Food Truck").all(axis = 1).mean()

# Alternative

((np.random.random((n, 3)) < p_food_truck).sum(axis = 1) == 0).mean()

# 7.a) How likely is it that a food truck will show up sometime this week?

lunches = np.random.choice(['Food Truck', 'No Food Truck'], (n, 5), p=[p_food_truck, p_no_food_truck])
(lunches == "Food Truck").any(axis = 1).mean()

# Alternative 

((np.random.random((n, 5)) < p_food_truck).sum(axis=1) > 0).mean()

# 8.) If 23 people are in the same room, 
# what are the odds that two of them share a birthday? 
# What if it's 20 people? 40?

# number of people = 23

birthdays = np.random.randint(1,365, (10000,23))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 23
same_probability = df_birthdays.same_birthdays.mean()

# number of people = 20

birthdays = np.random.randint(1,365, (10000,20))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 20
same_probability = df_birthdays.same_birthdays.mean()

# number of people = 40

birthdays = np.random.randint(1,365, (10000, 40))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 40
same_probability = df_birthdays.same_birthdays.mean()


