import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns', None)




class ReadData():

    def __init__(self, path):
        self.path = path

    def read_data_and_save_as_parquet_format(self):
        '''
        Reads data as a csv file and saves as parquet format for fast accessing 
        '''

        df =pd.read_csv(self.path + '.csv')
        df.to_parquet(self.path + '.parquet')

    

if __name__ == '__main__':
    dir_data = os.path.join( 'data')
    CHECK_DIR = os.path.isdir(dir_data)
    if not CHECK_DIR:
        os.makedirs(dir_data)


    path_to_file = os.path.join( 'data' , 'treatments_2017-2020' )
    read_data = ReadData(path_to_file)
    print(path_to_file)
    read_data.read_data_and_save_as_parquet_format()
    


