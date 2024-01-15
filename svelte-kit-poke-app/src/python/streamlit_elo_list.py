import streamlit as st 
import pandas as pd
from database_connection import database_query


elo_dataframe = pd.DataFrame(database_query("SELECT * FROM elo_table"), columns=('Pokemon', 'Elo', 'Match-ups', 'Wins', 'Losses', 'Draws', 'Win Rate'))
elo_dataframe.set_index('Pokemon', inplace=True)

st.title('Elo List')
st.write(elo_dataframe)



