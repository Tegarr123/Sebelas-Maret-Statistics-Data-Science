import pandas as pd
import re
import numpy as np
def rename_column(df:pd.DataFrame):
    df.columns = list(map(lambda s: re.sub(r'\(.*\)', '', s), df.columns))
    df.columns = list(map(lambda s : s.strip(), df.columns))
def fix_value(df:pd.DataFrame):
    df.index = df['ID']
    df['time'] = df['time'].apply(lambda x : pd.Timestamp(re.sub('T', ' ', x)))
    cat_val, _ = get_cat_num(df)
    for cat_col in cat_val:
        not_NaN_idx = ~df[cat_col].isna()
        df[cat_col][not_NaN_idx] = df[cat_col][not_NaN_idx].apply(lambda x : re.sub(',','.',x))
        df[cat_col] = df[cat_col].astype(float)
def get_cat_num(df:pd.DataFrame):
    cat_val = [i for i in df.columns if df[i].dtype == 'object']
    num_val = [i for i in df.columns if df[i].dtype != 'object']
    return cat_val, num_val
