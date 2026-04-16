'''
Cleaning the dataset from :
- missing CustomerID
- cancelled orders (InvoiceNo starts with C)
- negativ UnitPrice
Creates TotalPrice column
'''


__author__ = "Ernest Rouyrre"


import pandas as pd
from src.utils.helpers import get_logger


logger = get_logger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Clean the dataset from :
    - missing CustomerID
    - cancelled orders (InvoiceNo starts with C)
    - negativ UnitPrice
    Creates TotalPrice column
    '''
    initial_len = len(df)
    df = df.dropna(subset=['CustomerID'])
    df = df[~df['InvoiceNo'].str.startswith('C')]
    df = df[df['UnitPrice'] > 0]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    logger.info(f"Removed {initial_len - len(df)} rows, {len(df)} remaining")
    return df
