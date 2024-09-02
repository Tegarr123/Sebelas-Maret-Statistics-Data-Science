import pandas as pd
import re
def rename_column(df:pd.DataFrame):
    df.columns = list(map(lambda s: re.sub(r'\(.*\)', '', s), df.columns))
    df.columns = list(map(lambda s : s.strip(), df.columns))