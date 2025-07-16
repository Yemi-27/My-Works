import pandas as pd

df = pd.read_csv(r"C:\Users\HP Elite\Documents\adult.data.csv")

print(df.head()) # Viewed a part of the data
print(df.info()) # Viewed the structure of the data
print(df.columns) # Looked at the columns
print(df.describe()) # Viewed the statistical properties of the data
print(df.shape) # Checked the count of rows and columns

# Removing white spaces from columns
columns_to_trim = ["Education", "Gender", "Work Class", "Race", "Marital status", 
"Occupation", "Relationship", "Native-Country" , "Salary"]

# Applied strip to each column
df[columns_to_trim] = df[columns_to_trim].apply(lambda x: x.str.strip()) # lambda is a shortcut for writing simple, on- line function

# Question 1 - How many people of each race are represented in this dataset?
race_count = df["Race"].value_counts()
print("Race count:", race_count)

#Question 2- What is the average age of men?
average_age_of_men = df[df["Gender"] == "Male"]["Age"].mean()
print(f"Average age of men: {average_age_of_men:.1f}")

#Question 3- What is the percentage of the people who have a Bachelor's Degree
bachelors_degree_count = df[df["Education"] == "Bachelors"].shape[0]
total_count = df.shape[0]
bachelors_percentage = (bachelors_degree_count/total_count) * 100
print(f"percentage with Bachelor's degree: {bachelors_percentage:.1f}")

# Question 4- What percentage of people with advanced education ( Bachelors, Masters or Doctorate make more than 50K)
advanced_education = df[df["Education"].isin(["Bachelors", "Masters", "Doctorate"])]
advanced_education_high_salary = advanced_education[advanced_education["Salary"] == ">50K"]
percentage_of_advanced_education_high_salary = advanced_education_high_salary.shape[0] / advanced_education.shape[0] * 100
print(f"percentage of advanced education earning >50K: {percentage_of_advanced_education_high_salary:.1f}%")

# Question 5- What percentage of people without advanced education make more than 50K?
without_advanced_education = df[~df["Education"].isin(["Bachelors", "Masters", "Doctorate"])]
without_advanced_education_high_salary = without_advanced_education[without_advanced_education["Salary"]== ">50K"]
percentage_of_without_advanced_education_high_salary = without_advanced_education_high_salary.shape[0] / without_advanced_education.shape[0] * 100
print(f"percentage of without advanced education earning 50K: {percentage_of_without_advanced_education_high_salary:.1f}%")

# Question 6- What is the minimum number of hours a person works per week?
min_hour = df["Hours-per-week"].min()
print("minimum number of hours:", min_hour)

# Question 7- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_of_people = df[df["Hours-per-week"] == min_hour]
min_hours_of_people_high_salary = min_hours_of_people[min_hours_of_people["Salary"] == ">50K"]
percentage_of_minimum_hours_of_people_high_salary = min_hours_of_people_high_salary.shape[0]/ min_hours_of_people.shape[0] * 100
print(f"percentage of people who work the min number of hours earning above 50K: {percentage_of_minimum_hours_of_people_high_salary:.1f}%")

# Question 8- What country has the highest percentage of people that earn >50K and what is the percentage?
country_high_salary = df[df["Salary"] == ">50k"].groupby("Native-Country").size()/ df.groupby("Native-Country").size() * 100
# print(country_high_salary) # This shows the percentage of people in each country earning above 50K
# Identifies the country with the highest oercentage of people earning 50K
country_with_highest_percentage = country_high_salary.idxmax()
highest_percentage = country_high_salary.max()
print(f"country with the highest percentage of people that earn above 50K: {country_with_highest_percentage} {highest_percentage:.1f}%")

# Qustion 9- Identify the most popular occupation for those who earn >50K in India?
india_high_salary = df[(df["Native-Country"] == "India") & (df["Salary"] == ">50K")]
most_popular_occupation_in_india = india_high_salary["Occupation"].idxmax()
print(f"most popular occupation earning above 50K in India: {most_popular_occupation_in_india}")