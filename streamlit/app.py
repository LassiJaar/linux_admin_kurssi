import streamlit as st
import mysql.connector
import pandas as pd
conn = mysql.connector.connect(host='localhost', user='exampleuser', password='>
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50',
conn)
conn.close()
st.title('Säädata Helsingistä, joka on haettu 15 minuutin välein ja tallennettu>
st.dataframe(df)
st.markdown('Line_chart on Streamlitin mukaan myös API. (???)')
st.line_chart(data=df, x='timestamp', y=['temperature'])




