import numpy as np
import  pandas as pd
students_perfomans = pd.read_csv('accountancy.csv')
#mean_Pupa_A = students_perfomans.loc[students_perfomans.lunch == 'free/reduced'][students_perfomans['writi
#print(students_perfomans.groupby('Type').aggregate({'writing score': 'mean'}))
#print(students_perfomans.iloc[0:,0:7])
#print(students_perfomans.loc[students_perfomans.gender == 'female',['gender', 'writing score']])
#mean_writing_score = students_perfomans['writing score'].mean()
#stud_st = students_perfomans.loc[students_perfomans.lunch == 'standard',['math score', 'reading score', 'writing score']]
#stud_l = students_perfomans.loc[students_perfomans.lunch != 'standard',['math score', 'reading score', 'writing score']]
#print(stud_st.describe())
#print(stud_l.describe())

#mean_writing_score = students_perfomans.loc[students_perfomans.lunch == 'free/reduced'][students_perfomans['writing score']].mean()
#print(mean_writing_score)
#print(mean_writing_score)
#print(students_perfomans.loc[students_perfomans['legs'] == 2].iloc[:95, 0:5])
#print(students_perfomans[students_perfomans['writing score']  > 100 ]) #and students_performance.gender == 'female'])
#print(students_perfomans.loc[students_perfomans.lunch == 'free/reduced',['lunch', 'writing score']])

#print(students_perfomans.loc[students_perfomans.lunch == 'free/reduced'].mean()) #,['lunch', 'writing score']])
#students_perfomans = students_perfomans \
#    .rename(columns =
#            {'parental level of education': 'parental_level_of_education',
#             'test preparation course': 'test_preparation_course',
#             'math score': 'math_score',
#             'reading score': 'reading_score',
#             'writing score': 'writing_score'})
#wr = 98
Pupa_A = students_perfomans.query('Executor == "Loopa" & Type == "F" ')
print(Pupa_A.describe())

#print(students_perfomans.query('gender == "female" &  writing_score > @wr'))
#print(students_perfomans.head())
#score_columns = [i for i in list(students_perfomans) if 'score' in i]
#print(students_perfomans[score_columns].head())
#print(students_perfomans.filter(like='score'))
#st_mean = students_perfomans.groupby('gender', as_index=False)\
#    .aggregate({'math_score': 'mean', 'reading_score': 'mean'})\
#    .rename(columns = {'math_score': 'mean_math_score', 'reading_score': 'mean_reading_score'})
#print(st_mean)
#stud = students_perfomans.sort_values(['legs'])\
 #   .groupby('legs').head(5)
#print(students_perfomans)