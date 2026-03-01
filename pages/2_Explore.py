import streamlit as st
from utils.io import load_weather
from charts.charts import chart_dashboard, chart_temp_diff_wind

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")

st.header("Exercise 7: Extreme daily temperature differences by weather type")
st.write("We wish to see whether, for each weather type, do more extreme temperature differences correlate with levels of wind and precipitation? Select a specific time range and a weather type to examine corresponding wind and precipitation differences.")
st.altair_chart(chart_temp_diff_wind(df), use_container_width=True)
st.caption("Takeaway: Across weather types, there is primarily low precipitation (with the exception of rain and drizzle, of course). " \
"Wind speeds are generally low to moderate. However, wind speeds increase in the later months of a year, more evident under snowy and rainy conditions.")

