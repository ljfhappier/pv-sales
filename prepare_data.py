import numpy as np
import pandas as pd
import os

# merge data on the month of year before
def merge_year_before(df,spdf,cols):
    '''
    input:
        df(pd.DataFrame)-the left merging data df
        psdf(pd.DataFrame)-the right merging data df
    putput:
        mergeddf-the left merged data df
    '''
    onlist=['province','model','regMonth']
    mergeddf=pd.merge(df,spdf,on=onlist,how='left',suffixes=('','_year_before'))
    #cols=['province','adcode','model','bodyType','regYear','regMonth','salesVolume_year_before','salesVolume']
    return mergeddf[cols]

#读入数据
train_sales_data=pd.read_csv('data/train_sales_data.csv')
evaluation_public_data=pd.read_csv('data/evaluation_public.csv')
# year before 处理
train_sales_data_2017=train_sales_data[train_sales_data['regYear']==2017]
train_sales_data_2016=train_sales_data[train_sales_data['regYear']==2016]

cols=['province','adcode','model','bodyType','regYear','regMonth'、
      ,'salesVolume_year_before','salesVolume']
train_sales_year_before_data=merge_year_before(train_sales_data_2017,train_sales_data_2016,cols)

