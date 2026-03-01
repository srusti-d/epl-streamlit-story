import streamlit as st
import pandas as pd


import os
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Shared constants used by charts.py
MONTH_MAP = {
    '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December',
    '01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May'
}
MONTH_ORDER = ['August', 'September', 'October', 'November', 'December',
               'January', 'February', 'March', 'April', 'May']

def get_running_total_wins(df: pd.DataFrame) -> pd.DataFrame:
    # Split into home and away, then combine into a single team-level view
    home = df[['Date', 'HomeTeam', 'FTR', 'Month_Name']].copy()
    away = df[['Date', 'AwayTeam', 'FTR', 'Month_Name']].copy()
    home['Won'] = (home['FTR'] == 'H').astype(int)
    away['Won'] = (away['FTR'] == 'A').astype(int)
    home = home.rename(columns={'HomeTeam': 'team'})
    away = away.rename(columns={'AwayTeam': 'team'})
    combined = pd.concat([home, away]).sort_values(['team', 'Date'])
    combined['TotalWinCount'] = combined.groupby('team')['Won'].cumsum()
    return combined

@st.cache_data
def load_data():
    # Load both season CSVs from data/ folder at project root
    szn_2324_df = pd.read_csv(os.path.join(BASE_DIR, '..', 'data', 'PL-season-2324.csv'))
    szn_2425_df = pd.read_csv(os.path.join(BASE_DIR, '..', 'data', 'PL-season-2425.csv'))

    # Parse dates and sort chronologically
    for df in [szn_2324_df, szn_2425_df]:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        df.sort_values('Date', inplace=True)

    # Cumulative win counts split by home and away
    szn_2324_df['HomeWinCount'] = (szn_2324_df['FTR'] == 'H').groupby(szn_2324_df['HomeTeam']).cumsum()
    szn_2324_df['AwayWinCount'] = (szn_2324_df['FTR'] == 'A').groupby(szn_2324_df['AwayTeam']).cumsum()
    szn_2425_df['HomeWinCount'] = (szn_2425_df['FTR'] == 'H').groupby(szn_2425_df['HomeTeam']).cumsum()
    szn_2425_df['AwayWinCount'] = (szn_2425_df['FTR'] == 'A').groupby(szn_2425_df['AwayTeam']).cumsum()

    # Labels
    szn_2324_df['Season'] = '2023-24'
    szn_2425_df['Season'] = '2024-25'
    both_szns_df = pd.concat([szn_2324_df, szn_2425_df], ignore_index=True)


    both_szns_df['Month_Str'] = both_szns_df['Date'].dt.strftime('%m')
    both_szns_df['Month_Name'] = both_szns_df['Month_Str'].map(MONTH_MAP)
    szn_2425_df['Month_Str'] = szn_2425_df['Date'].dt.strftime('%m')  
    szn_2425_df['Month_Name'] = szn_2425_df['Month_Str'].map(MONTH_MAP)

    # Red cards per team aggregated across home and away
    home_rcards = szn_2425_df.groupby('HomeTeam')['HR'].sum()
    away_rcards = szn_2425_df.groupby('AwayTeam')['AR'].sum()
    teams_rcards = away_rcards.add(home_rcards, fill_value=0)
    teams_rcards_df = teams_rcards.to_frame().reset_index()
    teams_rcards_df = teams_rcards_df.rename(columns={'AwayTeam': 'team', 0: 'red_cards'})

    # Running total wins for 2024-25 season
    teams_wins_df = get_running_total_wins(szn_2425_df)

    # Match-level penalty metrics
    szn_2425_df['total_fouls'] = szn_2425_df['HF'] + szn_2425_df['AF']
    szn_2425_df['total_cards'] = szn_2425_df['HY'] + szn_2425_df['AY'] + szn_2425_df['HR'] + szn_2425_df['AR']
    szn_2425_df['total_penalties'] = szn_2425_df['total_fouls'] + szn_2425_df['total_cards']
    szn_2425_df['match_id'] = range(len(szn_2425_df))

    # Melt for per-match penalty breakdown by home/away
    penalty_map = {
        'HF': ('Foul', 'Home Team'), 'AF': ('Foul', 'Away Team'),
        'HY': ('Yellow Card', 'Home Team'), 'AY': ('Yellow Card', 'Away Team'),
        'HR': ('Red Card', 'Home Team'), 'AR': ('Red Card', 'Away Team')
    }
    melted_df = szn_2425_df.melt(
        id_vars=[c for c in szn_2425_df.columns if c not in penalty_map],
        value_vars=list(penalty_map.keys()),
        var_name='Penalty Type', value_name='Count'
    )
    melted_df['Category'] = melted_df['Penalty Type'].map(lambda x: penalty_map[x][0])
    melted_df['Team'] = melted_df['Penalty Type'].map(lambda x: penalty_map[x][1])

    return both_szns_df, szn_2425_df, teams_rcards_df, teams_wins_df, melted_df