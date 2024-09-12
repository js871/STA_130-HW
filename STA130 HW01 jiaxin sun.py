#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.
import pandas as pd

# Load the Titanic dataset from seaborn's built-in dataset
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Display the first few rows of the dataset
print("First few rows of the Titanic dataset:\n", titanic.head())

# Check for missing values
missing_values = titanic.isnull().sum()

print("\nMissing values in each column:\n", missing_values)


# In[2]:


#2
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv'
villagers_df = pd.read_csv(url)

# Print the number of rows and columns
print(f'Number of rows: {villagers_df.shape[0]}')
print(f'Number of columns: {villagers_df.shape[1]}')

# Observations: an observation refers to row in the DataFrame, where each row represents a unique villager with various attributes, such as name, gender, species.
# Variables: Variables are the columns in the dataset, representing the features of villagers (e.g., gender, species, personality).


# In[3]:


#3
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv'
villagers_df = pd.read_csv(url)

# Summarize each column
for column in villagers_df.columns:
    print(f"Summary of '{column}':")
    print(villagers_df[column].value_counts(), "\n")


# In[4]:


#4
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv'
villagers_df = pd.read_csv(url)

# Check for missing values
missing_values = villagers_df.isnull().sum()

# Show which columns have missing values
print(missing_values)


# In[4]:


#4

#（1）.About the discrepancies between df.shape and df.describe:
#df.shape: This function returns the overall dimensions of the dataset, specifically the number of rows (observations) and columns (variables). 
#For example, if the dataset contains 300 rows and 10 columns, will return , regardless of whether the columns are numeric or non-numeric.df.shape(300, 10)
#df.describe(): This function provides summary statistics for numeric columns only by default. It will ignore non-numeric (categorical) columns
#unless explicitly told to include them using . It summarizes only the numeric columns by providing information like the count, mean, standard deviation, etc.df.describe(include='all')

#（2）.About the number of Columns Analyzed:
#df.shape reflects all columns in the dataset (numeric and non-numeric).
#df.describe() only includes the numeric columns, hence fewer columns are reported.


# In[5]:


#5
#(1)Attribute: attribute is a kind of data related to an object. it shows the feature of the object and it does not need parentheses when we use it. 
#An attribute provide information more easier to get and understand. It is accessed directly like a variable.

#(2)Method: method is a kind of function which use to execute operations and computations. 
#It requires parentheses when we call it, in order to help it process data.


# In[6]:


#6
#'count': The number of non-null observations in the dataset for each variable. It tells us how many data points are available.
#'mean': the average value of the observations for each variable. 
#'std': the whole name of std is standard deviation.If it shows as a axes, the more concentrated the point distribution is,the std will be more higher. In conclusion, a higher standard deviation indicates more variability.
#'min': it is the smallest value in the dataset, represent the minimum limit of the data range.
#'25%': it represents the value below which 25% of the data points are found. It shows where the bottom quarter of the data lies.
#'50%',This is the middle value of the dataset. Half of the data points are below this value, and half are above it. It gives an idea of the center of the data.
#'75%': This is the value below which 75% of the data points are found. It shows where the top quarter of the data lies.
#'max': This is the highest value in the dataset. It marks the upper end of the data range.


# In[7]:


#7
#(1)Use case: Assume I have a dataset of students' grades (df) with columns: student_name, math_score,and english_score. 
#The english_score column has many missing values. I want to analyze the data, when I use df.dropna() to remove only the rows that have missing values. 
#This is useful, rather than using del df['col']. because removing a few rows with missing values keeps the majority of the data. I will not lose other students data.

#(2)use case: Assume I have a dataset of students' grades (df) with columns, there are many columns of english_score, math_score and number of good deed.
#I want to analyze these data and select the best student. But this time the english_score losing over 90% of data,since the column is nearly empty, 
#it’s better to delete it altogether than risk skewing the analysis.

#(3)Applying del df['col'] before df.dropna() can be important because it ensures that dropping columns with excessive missing data 
#before filtering out rows with just a few missing values. This prevents the potential loss of valuable rows that might only be missing data in the now-deleted column,
#thereby maximizing the amount of usable data.

#(4)
student_name   math_score   english_score   science_score
Alice          85           90              NaN
Bob            78           NaN             NaN
Carol          92           85              89
Dave           NaN          76              91
#Step 1: Analyze Missing Data: The science_score column has 2 missing values,some rows (like Bob's) have multiple missing values.

#Step 2: use del df['science_score'] to remove the column because it has too many missing values. 

del df['science_score']

#Step3: use df.dropna() to remove rows with any remaining missing values.

df = df.dropna()

# Reason: Deleting the science_score column because it had too many missing values, making it unreliable for analysis.
# Removing rows with missing values: After deleting the science_score column, we used df.dropna() to remove rows with any other 
# missing values (e.g., rows with missing math_score or history_score). This ensures that the final dataset is complete 
# and ready for analysis without gaps.

# Before and after: Before cleaning: We had 4 rows and 3 columns.There were multiple missing values, particularly in the science_score column.
# After cleaning: We now have 1 row and 2 columns. The dataset is complete, with no missing values.


# In[7]:


#7 here is the complete code below:

get_ipython().system('pip install pandas numpy')
import pandas as pd
import numpy as np

# Create the initial dataset, using np.nan for missing values
data = {
    'student_name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'math_score': [85, 78, 92, np.nan],
    'english_score': [90, np.nan, 85, 76],
    'science_score': [np.nan, np.nan, 89, 91],
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset before cleaning
print("Dataset before cleaning:")
print(df)

# Delete the 'science_score' column due to too many missing values
del df['science_score']

# Remove rows with any remaining missing values
df_cleaned = df.dropna()

# Display the dataset after cleaning
print("\nDataset after cleaning:")
print(df_cleaned)


# In[8]:


#8 
#（1）df.groupby("col1"): Groups the DataFrame df by unique values in the column col1. 
#This means all rows with the same value in col1 are put into the same group
#["col2"]: From each group created, this selects the col2 column.

!pip install pandas
import pandas as pd
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)
embarked_fare_summary = df.groupby('embarked')['fare'].describe()
print(embarked_fare_summary)

#explain: df.groupby('embarked'): Groups the data by the embarked column 
#(which indicates the port of embarkation: C = Cherbourg, Q = Queenstown, S = Southampton).
#['fare']: Focuses on the fare column (ticket price) for analysis.
#.describe(): Provides summary statistics of the fare column for each embarkation port group, showing the distribution of ticket prices.

#（2）Scope of Analysis:df.describe(): Provides a summary of statistics for each column in the entire DataFrame. 
#The count here represents the total number of non-missing values for each column across the whole dataset. 
#This gives a global view of data availability and distribution.df.groupby("col1")["col2"].describe(): Provides statistics for col2 within each group defined by col1. 
#The count in this context represents the number of non-missing values in col2 for each distinct value of col1. This gives a detailed view of data within specific groups.
#Handling of Missing Values: df.describe(): The count reflects the overall impact of missing values on each column in the entire DataFrame.
#Missing values affect the count, mean, and other statistics across the whole dataset.df.groupby("col1")["col2"].describe(): The count is specific to each group,
#so it shows how missing values are distributed within each group rather than the entire dataset. Different groups may have different numbers of missing values,
#which affects the count and other statistics for col2 within each group

#（3）I input those errors in my code, and test whether chatgpt can fix it and make it working. 
# Here are the chatgpt's resolution and my opinions

# A：
#Fix the Error: To fix this, simply add the missing import statement at the beginning of code:
import pandas as pd

# B：
#Correct the Typo: correct the typo in the file name to 'titanic.csv'.
import pandas as pd
# Correct URL or file name
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)
# Perform analysis
summary = df.describe()
print(summary)

#C:
#Correct the Variable Name: Check code to ensure that using the correct variable name. In this case, change DF to df.
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# Correct variable name
grouped_summary = df.groupby("embarked")["fare"].describe()
print(grouped_summary)

#D
#If code should be pd.read_csv(url) but I accidentally write pd.read_csv(url, Python will raise a SyntaxError.
#This is because the closing parenthesis is missing.

#E
#Mistyping a Function Name:
#If the code should be df.groupby("col1")["col2"].describe(), but I mistakenly write df.group_by("col1")["col2"].describe(), 
#Python will raise an AttributeError because group_by is not a valid method for a DataFrame; the correct method is groupby.
#Mistyping a Method Name:
#Similarly, if the code should be df.groupby("col1")["col2"].describe(), but I mistakenly write df.groupby("col1")["col2"].describle(),
#Python will raise an AttributeError because describle is not a valid method; the correct method is describe.

#F
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# Mistyped column name
grouped_summary = df.groupby("Sex")["age"].describe()
print(grouped_summary)

KeyError: 'Sex'
    
#Check Column Names: Use df.columns to list all available columns in your DataFrame.
#Update the Code: Ensure you use the exact column names from df.columns in both groupby and selection.


#G
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# Missing quotes around column name
grouped_summary = df.groupby(sex)["age"].describe()
print(grouped_summary)

NameError: name 'sex' is not defined

#chatGPT give me a way to solve it:
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# Correct use of quotes around column names
grouped_summary = df.groupby("sex")["age"].describe()
print(grouped_summary)

#In my opinion, the chatgpt is more helpful to solve the problems. 
#Because it will offer many resolutions when I have no idea about how to fix these errors, and I learnt a lot from chatgpt.


# In[9]:
#9 YES
