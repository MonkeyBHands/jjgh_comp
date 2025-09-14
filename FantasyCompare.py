import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NFL dataset", layout="wide", page_icon="data/NFL/JJGH.jpeg")

st.title("JJGH Fantasy Player Comparison App")
st.write("This app will help you analyze NFL data effectively.")

# @st.cache_data
def load_data():
    data1=pd.read_csv('data/NFL/stats_player_week_2020.csv')
    data2=pd.read_csv('data/NFL/stats_player_week_2021.csv')
    data3=pd.read_csv('data/NFL/stats_player_week_2022.csv')
    data4=pd.read_csv('data/NFL/stats_player_week_2023.csv')
    data5=pd.read_csv('data/NFL/stats_player_week_2024.csv')
    data6=pd.read_csv('https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2025.csv')
    df=pd.concat([data1,data2,data3,data4,data5,data6])
    return df


df = load_data()
df['year_week'] = df['season'] + df['week']/25

# position = st.multiselect(
#     "Position",
#     df.position.unique(),
#     ["QB", "RB", "WR", "TE", "K"],
# )

name = st.multiselect(
    "Select Player(s)",
    df.player_display_name.unique(),
    ["Joe Burrow","Puka Nacua","Deebo Samuel Sr.","Derrick Henry","TreVeyon Henderson","Sam LaPorta","Isiah Pacheco","Matthew Golden","Joe Mixon","Cooper Kupp","Josh Palmer"],
)

st.sidebar.image("data/NFL/JJGH.jpeg", width=250)
# st.sidebar.title("Filters")
years = st.sidebar.slider("Season", 2020, 2025, (2024, 2025))
week = st.sidebar.slider("Week", 1, 22, (1, 18))

df_filtered = df[(df["player_display_name"].isin(name)) & (df["season"].between(years[0], years[1])) & (df["week"].between(week[0], week[1]))]
st.dataframe(df_filtered[['player_display_name','season','week','team','position','opponent_team','passing_tds','passing_interceptions','rushing_tds','receiving_tds','fantasy_points']])
st.write(f"Total records: {df_filtered.shape[0]}")

fig = plt.figure(figsize=(8,4))
for name,group in df_filtered.groupby('player_display_name'):
    plt.plot(group['year_week'],group['fantasy_points'],marker='x',label=f'{name}',alpha=0.5)
plt.title(f'Fantasy Points by Week')
plt.xlabel('Week')
plt.ylabel('Points')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
st.pyplot(fig)

st.write("All data provided by https://github.com/nflverse/nflverse-data/releases")
st.write("Brought to you by JJGH - There ain't no glory hole like a Jerry Jones Glory Hole!")
# st.image("https://upload.wikimedia.org/wikipedia/en/a/a2/National_Football_League_logo.svg", width=200)
# st.image("data/NFL/JJGH.jpeg", width=100)


