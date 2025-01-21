import pandas as pd
import random
import datetime

# Task: https://stepik.org/lesson/154087/step/1?unit=128454
# Однажды я попросил, чтобы студенты ответили на два вопроса анкеты «ваш год рождения» и «ваш возраст».
# Из их ответов я сформировал таблицу, в которой был столбец Р=«год рождения студента» и Q=«возраст студента».
# Оказывается, значение коэффициента корреляции признаков P и Q зависит от месяца, в котором проводилось анкетирование (это не шутка!).
# Укажите два месяца, которым соответствует наименьшее (по модулю) значение коэффициента корреляции признаков P и Q.

# For example, all students were born in 2000 or 2001, and test date is 20th date of each month in 2020.

# Generate randon dates of  birthdays
dates = []

while len(dates) < 500:
    try:
        dates.append(datetime.date(random.randint(2000, 2001), random.randint(1, 12), random.randint(1, 31)))
    except:
        continue

df = pd.DataFrame({'Date of birthday': dates})

# Function to calculate age
def age(birth_date, month):
    reference_date = datetime.date(2020, month, 20)
    days_difference = (reference_date - birth_date).days
    return int(days_difference // 365.25)

# adding age by month
for month in range(1, 13):
    column_name = f'Month_{month}'
    ages = [age(birth_date, month) for birth_date in df['Date of birthday']]
    df[column_name] = ages

# Add year of birthday as numeric column
df['year'] = df['Date of birthday'].apply(lambda x: x.year)

# Remove non-numerical columns
numeric_columns = df.select_dtypes(include=['number'])

# Calculate correlation
result = numeric_columns.corr().year.sort_values(ascending=False)
print(result.iloc[1:3])
