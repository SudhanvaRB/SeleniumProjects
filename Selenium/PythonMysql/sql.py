'''
Created on May 2, 2019

@author: subharad
'''
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=IN-PNQ-DSQLDB01;'
                      'Database=ISG_MYC_TST;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('Select * from PS_ADDRESSES')

for row in cursor:
    print(row)
