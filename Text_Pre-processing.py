import pandas as pd
import re

def clean_text(df, column):
    df[column] = df[column].str.lower()
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
    df[column] = df[column].apply(lambda x: x.split())
    return df
