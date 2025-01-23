import random
import datetime
import pandas as pd

# random.seed(42) # Fix random seed for testing
amount_of_students = 3000 # For instance, 3000 students

# Create random students birthdays for survey
def generate_random_dob_students():
    birthday_dates = []

    while len(birthday_dates) < amount_of_students:
        try:
            birthday_dates.append(datetime.date(random.randint(2000,2001), random.randint(1,12), random.randint(1, 31)))
        except:
            continue

    df = pd.DataFrame({'Date of birth': birthday_dates})
    return df

df_dob = generate_random_dob_students() # Generate random Dates Of Birthdays and adding to DataFrame


# Add year as direct column
df_dob['Year_of_birth'] = df_dob['Date of birth'].apply(lambda x: x.year)


# survey function to calculate age
def survey(date_of_survey, birth_date):
    age = (date_of_survey - birth_date).days
    return int(age//365.25)


# Calculate ages for each student in every month
for month in range(1, 13):
    column_name = f'Month_{month}'
    ages = []
    date_of_survey = datetime.date(2020, month, 15)  # Survey date always 15th day of month

    for birth_date in df_dob['Date of birth']:
        ages.append(survey(date_of_survey, birth_date))

    # Add Age columns by Month to DataFrame
    df_dob[column_name] = ages


# Remove non-numeric columns
numerical_columns = df_dob.select_dtypes(include=['number'])

# Calculate correlation for every month
correlation = numerical_columns.corr().Year_of_birth

# Find the minimum correlation
min_month = correlation.sort_values(ascending=False)

# print(f'Correlation for all month:\n {correlation}')
print(f'Min correlation in:\n{min_month.iloc[1:3]}')