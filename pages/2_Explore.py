import streamlit as st
from utils.io import load_data
from charts.charts import chart_home_away_wins, chart_red_cards_wins, chart_referee_penalties


st.set_page_config(page_title="Explore", layout="wide")
both_szns_df, szn_2425_df, teams_rcards_df, teams_wins_df, melted_df = load_data() 

st.title("Interactive Exploratory View")
st.write("Use interaction to zoom and select highlight team-specific and season-specific patterns.")

st.header("Home & Away Wins by Season")
st.write("Switch between seasons and select a team to follow their home and away win trajectory month by month.")
st.altair_chart(chart_home_away_wins(both_szns_df), use_container_width=True)
st.markdown("**Guided prompts:**")
st.write("- Does your selected team perform better at home or away? Does this change between seasons?")
st.write("- Which teams show the biggest home/away performance gap?")

st.header("Red Cards vs Wins (2024-25)")
st.write("Brush over teams in the bar chart to highlight their win trajectory in the line chart.")
st.altair_chart(chart_red_cards_wins(teams_rcards_df, teams_wins_df), use_container_width=True)
st.markdown("**Guided prompts:**")
st.write("- Do the most disciplined teams consistently win more?")
st.write("- Are there any surprising outliers — high cards but high wins, or vice versa?")

st.header("Referee & Match Penalty Explorer (2024-25)")
st.write("Brush referees to filter the scatter plot by matches refereed by the selected individual, then click a match to inspect its penalty breakdown by home and away team.")
st.altair_chart(chart_referee_penalties(szn_2425_df, melted_df), use_container_width=True)
st.markdown("**Guided prompts:**")
st.write("- Which referee awards the most penalties on average?")
st.write("- Do high-foul matches always result in more cards, or does it vary by referee?")