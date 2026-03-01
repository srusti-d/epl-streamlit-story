import streamlit as st
import altair as alt
from utils.io import load_data
from charts.charts import (
    base_theme,
    chart_home_away_wins, 
    chart_red_cards_wins, 
    chart_referee_penalties
)

st.set_page_config(page_title="Story", layout="wide")

both_szns_df, szn_2425_df, teams_rcards_df, teams_wins_df, melted_df = load_data()  # unpack all dataframes from load_data

st.title("A Data Story: English Premier League Patterns")
st.markdown("**Central question:** *How do team performance, discipline, and referee behaviour shape outcomes across the 2023-24 and 2024-25 seasons?*")

st.header("1) Home vs Away Performance by Season")
st.write("We start by comparing cumulative wins at home and away across both seasons. Select a team and season to trace their trajectory.")
st.altair_chart(chart_home_away_wins(both_szns_df), use_container_width=True)
st.caption("Takeaway: Some teams are clearly stronger at home; others sustain performance away from their stadium.")

st.header("2) Do Red Cards Cost Teams Wins?")
st.write("We examine whether teams that accumulate more red cards tend to win less over the 2024-25 season. Brush over teams in the bar chart to highlight their win trajectories.")
st.altair_chart(chart_red_cards_wins(teams_rcards_df, teams_wins_df), use_container_width=True)
st.caption("Takeaway: The relationship is not straightforward — some high-card teams still perform well, suggesting other factors dominate.")

st.header("3) Referee Strictness and Match-Level Penalties")
st.write("Finally, we look at how referees differ in the penalties they award, and whether fouls and cards cluster in specific match types. Brush referees on the left, then click a match point to see its penalty breakdown.")
st.altair_chart(chart_referee_penalties(szn_2425_df, melted_df), use_container_width=True)
st.caption("Takeaway: Certain referees consistently award more penalties. High-foul matches don't always produce high card counts.")