import pandas as pd
import re
def rename_column(train_df:pd.DataFrame):
    train_df.columns = list(map(lambda s: re.sub(r'\(.*\)', '', s), train_df.columns))
    train_df.columns = list(map(lambda s : s.strip(), train_df.columns))