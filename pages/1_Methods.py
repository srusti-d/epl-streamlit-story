import streamlit as st

st.set_page_config(page_title="Methods", layout="wide")

st.title("Methods & Limitations")

st.subheader("Data Source")
st.info("Dataset: [English Premier League Data](https://datahub.io/core/english-premier-league).")
st.info("From this data source, two CSVs were downloaded locally, each corresponding to either the 2023-24 season or 2024-25 season. Each row represents a single match.")
st.write("- Variables used: Home Team, Away Team, Home Team & Away Teams' Fouls + Yellow Cards + Red Cards ('HF', 'AF', 'HY', 'AY', 'HR', 'AR'), Referee, Full-Time Match Score Results for each team (FTHG, FTAG)")


st.subheader("Preprocessing")
st.write("- Dates were parsed using `dayfirst=True` to handle the UK date format (DD/MM/YYYY), then rows were sorted chronologically within each season before any cumulative calculations were made.")
st.write("- Cumulative win counts were computed separately for home and away games by grouping on `HomeTeam` and `AwayTeam` respectively, then applying a cumulative sum on a boolean indicator of whether the result (`FTR`) matched a home (`H`) or away (`A`) win.")
st.write("- For the referee and penalty analysis, match-level penalty columns were aggregated into `total_fouls`, `total_cards`, and `total_penalties`, and the data was melted from wide to long format to enable grouped bar charts breaking down penalty types by home and away team.")

st.subheader("Transformations")
st.write("- A `Month_Name` column was derived from the match date and mapped to ordered month labels (August through May) to reflect the football season calendar rather than the standard calendar year.")
st.write("- Red card totals were computed per team by summing home red cards (`HR`) and away red cards (`AR`) separately via `groupby`, then adding them together with `fill_value=0` to handle teams that received cards only in one context.")
st.write("- A `match_id` index was assigned to each 2024-25 match to enable point-level selection linking the scatter plot to the penalty breakdown bar chart.")

st.subheader("Limitations")
st.write("- The 2024-25 season data may be incomplete depending on when the CSV was last updated, meaning cumulative win and card counts for later months could underrepresent the full picture.")
st.write("- The penalty breakdown chart only shows counts for a single selected match at a time, so it is not suitable for identifying broader patterns across referees or teams without repeated interaction.")