# impiorting the modules
import pandas as pd
import numpy as np

# creating a DataFrame
# students = {'Student': ['Amit', 'Cody',
#                         'Darren', 'Drew'],
#             'RollNumber': [1, 5, 10, 15],
#             'Grade': ['A', 'C', 'F', 'B']}
# df = pd.DataFrame(students,
#                   columns=['Student', 'RollNumber',
#                            'Grade'])
# # displaying the original DataFrame
# print("Original DataFrame")
# print(df)
#
# # saving as a CSV file
# df.to_csv('Students.csv', sep='\t')

# loading the CSV file
new_df = pd.read_csv('Students.csv')

# displaying the new DataFrame
print('Data from Students.csv:')
print(new_df)