import plotly.figure_factory as ff
import pandas as pd
import csv
import scipy 
df=pd.read_csv("C:/Users/dell/Desktop/Python/folderA/datas/data(class 108).csv")
fig=ff.create_distplot([df["Weight"].tolist()],["Weight"],show_hist=False)
fig.show()