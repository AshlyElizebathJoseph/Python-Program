import pandas as pd
a=pd.read_csv('/home/sjcet/Ashly (AI & DS LAB)/house rent.csv')       #To read a csv file
a.sort_values(by=['Area'],ascending=True)      #To sort the file content, ascending=True means sorting in increasing order
