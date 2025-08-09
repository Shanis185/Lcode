import pandas as pd
from main import calculate_age, create_age_group

def test_calculate_age():
    assert calculate_age("30/09/1997") == 26
    assert calculate_age("13/11/1999") == 24
    assert calculate_age("07/01/1985") == 39

def test_create_age_group():
    assert create_age_group(24) == 'Below 25'
    assert create_age_group(25) == '25 to 30'
    assert create_age_group(30) == '25 to 30'
    assert create_age_group(31) == 'Above 30'

def test_total_points():
    driver_df = pd.read_csv('E:\Downloads\drivers.csv')
    driver_df['Age'] = driver_df['Date of Birth'].apply(calculate_age)
    driver_df['Age Group'] = driver_df['Age'].apply(create_age_group)
    points_by_age = driver_df.groupby('Age Group')['Points'].sum().reset_index()
    
    # Check the sum matches the total points in the dataset
    total_points = driver_df['Points'].sum()
    assert points_by_age['Points'].sum() == pytest.approx(total_points)
    
    # Check specific age groups
    below_25 = driver_df[driver_df['Age'] < 25]['Points'].sum()
    assert points_by_age[points_by_age['Age Group'] == 'Below 25']['Points'].values[0] == pytest.approx(below_25)