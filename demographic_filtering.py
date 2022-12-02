import pandas as pd

df = pd.read_csv('articles.csv', low_memory=False)

df = df.sort_values(['total_events'], ascending=[False])

output=df[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()
