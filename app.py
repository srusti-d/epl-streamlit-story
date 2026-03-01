import streamlit as st
from PIL import Image

st.set_page_config(page_title="Narrative Visualization - English Premier League:", layout="wide")

st.title("English Premier League")
st.write(Image.open('images/epl.jpg'))
st.write("This project is a data story analyzing and visualizing English Premier League data from two seasons.\n")
st.write("The data story will analyze the following questions:\n 1) How does EPL team performance vary in home games within and across seasons? 2) Is there a relationship between the cumulative number of red cards a team gets and their performance in the season? 3) How does disciplinary action vary between referees at a match-level, and what type of penalties occur in each of these matches?\n")
st.write(
    "To explore this visual data story, please navigate it through the pages in the sidebar:\n"
    "- **Central Narrative**: We begin by taking into account season-wide performance metrics, then allowing match-level selection and referee filtering.\n"
    "- **Exploration**: Enables viewer-driven exploration of the interactive visualizations. \n"
    "- **Methodology**: We lay down some key details about our data and limitations to our analysis.\n"
)

st.info("Dataset: [English Premier League Data](https://datahub.io/core/english-premier-league).")
