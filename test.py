import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('data/premierLeague_tables_1992-2017.csv')

df = df[['season', 'team', 'points']]
df = df.pivot_table(values='points', index=['season'], columns='team')
df.fillna(0, inplace=True)
df.sort_values(list(df.columns), inplace=True)
df = df.sort_index()
df.iloc[:, 0:-1] = df.iloc[:, 0:-1].cumsum()

top_prem_clubs = set()

for index, row in df.iterrows():
    top_prem_clubs |= set(row[row > 0].sort_values(ascending=False).head(6).index)

df = df[list(top_prem_clubs)]

bcr.bar_chart_race(df=df,
                   n_bars=6,
                   sort='desc',
                   title='Premier League Clubs Points Since 1992',
                   filename='pl_clubs.mp4')