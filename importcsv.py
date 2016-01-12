import pandas as pd
df = pd.read_csv('ACS_14_5YR_S2302_with_ann.csv')
df.columns = [c.lower() for c in df.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/lab1')

df.to_sql("census1", engine)
