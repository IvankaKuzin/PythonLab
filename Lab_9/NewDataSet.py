import pandas as pd
import numpy as np

def new_dataset():
    rng = np.random.default_rng()
    df1 = pd.read_csv('group_data.csv')
    df2 = pd.DataFrame(rng.integers(0, 100, size=(10128, 1)), columns=['Test_colum'])
    df= pd.concat([df1, df2], axis=1)
    print(df)
    df.to_csv('NewDataSet.csv', index=False)

def mydataset_merge():
    main_dataframe=pd.read_csv('read.csv')
    created_dataframe=pd.read_csv('NewDataSet.csv')
    frames = [main_dataframe, created_dataframe]
    new_frame = pd.concat(frames, axis=1)
    print('New DataSet: ',new_frame)
    new_frame.to_csv('DatasetMerge.csv', index=False)
