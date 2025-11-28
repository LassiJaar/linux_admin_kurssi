import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Viikko 4")
tab1, tab2 = st.tabs(['Helsingin sää', 'Uber-data New York City'])

with tab1:
        conn = mysql.connector.connect(host='localhost', user='exampleuser', password='SALASANA', database='weather_db')
        df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
        df2 = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC',conn)
        conn.close()
        st.title('Säädata Helsingistä, joka on haettu 15 minuutin välein ja tallennettu tietokantaan.')
        st.dataframe(df)
        st.markdown('Ylläoleva pöytä listaa 50 viimeisintä hakua, kun taas alla oleva kaavio sisältää tietokannan jokaisen rivin.')
        st.line_chart(data=df2, x='timestamp', y=['temperature'])

with tab2:
        st.title('Uber tilaukset kaupungissa New York City')

        DATE_COLUMN = 'date/time'
        DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

        @st.cache_data
        def load_data(nrows):
            data = pd.read_csv(DATA_URL, nrows=nrows)
            lowercase = lambda x: str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
            return data

        data_load_state = st.text('Loading data...')
        data = load_data(10000)
        data_load_state.text("Valmis! (using st.cache_data)")

        if st.checkbox('Näytä raaka data'):
            st.subheader('Raaka data')
            st.write(data)
        st.subheader('Tilausten määrä tunneittain')
        hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.bar_chart(hist_values)

        hour_to_filter = st.slider('Tunti', 0, 23, 17)
        filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

        st.subheader('Kartta kaikista tilauksista kellonaikana %s:00' % hour_to_filter)
        st.map(filtered_data)

