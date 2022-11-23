#code transfer parquet file to csv file

import os

import pandas as pd
import pyarrow.parquet as pq


def read_pyarrow(path, use_threads=1):
#read parquet file using pyarrow
    return pq.read_table(path, use_threads=use_threads).to_pandas()


def get_file_list(file_dir='.'):
# get all the parquet file under the folder
    L = []
    for root, _, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.parquet':
                L.append(os.path.join(root, file))
    return L


def get_csv(file_list):
# read the parquet file and save as csv table
    init_flag = 0
    for f in file_list:
        print('The current handling file is:\n', f)
        if init_flag == 0:
            init_df = read_pyarrow(f)
            init_flag = 1
        else:
            t_df = read_pyarrow(f)
            init_df = pd.concat([init_df, t_df])
    return init_df


path = '/Users/samwang/Downloads/wildhunt/test/W4-snr5-mpro7.5/ls_dr9_tractor' #path to the parquet file

file_list = get_file_list(path) #transfer all the parquet file to one csv file
df = get_csv(file_list)
df.to_csv('./parquet_data.csv',
          sep=',', index=False, mode='w', line_terminator='\n', encoding='utf-8')

