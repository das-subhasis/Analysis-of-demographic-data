import pandas as pd


def calculate_demographic_data(print_data=True):
    dg_data = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = dg_data['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(dg_data['age'].sum()/dg_data['age'].shape[0],1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((dg_data[dg_data['education']=='Bachelors']['education'].shape[0]/dg_data.shape[0])*100,1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_eductation = dg_data[(dg_data['education']=='Bachelors') | (dg_data['education']=='Masters') | (dg_data['education']=='Doctorate')]
    lower_eductation = dg_data[(dg_data['education']!='Bachelors') & (dg_data['education']!='Masters') & (dg_data['education']!='Doctorate')]
    
    # percentage with salary >50K
    higher_education_rich = round((higher_eductation[higher_eductation['salary']=='>50K'].shape[0]/higher_eductation.shape[0])*100,1)
    lower_education_rich = round((lower_eductation[lower_eductation['salary']=='>50K'].shape[0]/lower_eductation.shape[0])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = dg_data['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =  dg_data[dg_data['hours-per-week']==min_work_hours].shape[0]

    rich_percentage =round((dg_data[(dg_data['hours-per-week']==min_work_hours) & (dg_data['salary']=='>50K')].shape[0]/num_min_workers)*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = dg_data[dg_data['salary']=='>50K']['native-country'].value_counts().index[0]
    highest_earning_country_percentage = round((dg_data[dg_data['salary']=='>50K']['native-country'].value_counts()[0]/dg_data[dg_data['salary']=='>50K']['native-country'].shape[0])*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = dg_data[(dg_data['salary']=='>50K') & (dg_data['native-country']=='India')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
