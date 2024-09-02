import pandas as pd
import re
def rename_column(train_df, test_df=None):
    train_df.columns = list(map(lambda s: re.sub(r'\(.*\)', '', s), train_df.columns))
    train_df.columns = list(map(lambda s : s.strip(), train_df.columns))

    if test_df != None:
        test_df.columns = list(map(lambda s: re.sub(r'\(.*\)', '', s), test_df.columns))
        test_df.columns = list(map(lambda s : s.strip(), test_df.columns)) 
