import pandas as pd
import streamlit as st

tracxn_df = pd.read_csv('tracxn_usa.csv')

st.header('Companies in the Agriculture and AI sectors in the USA')

st.dataframe(tracxn_df)
st.divider()

for row in tracxn_df.iterrows():
    
    favicon = f"https://www.google.com/s2/favicons?domain={row[1]['domain']}"
    
    st.markdown(f"""
        <h3>
            <img src="{favicon}" alt="{row[1]['company_name']}" width="25" height="25" align="left" style="margin-right: 10px; margin-bottom: 10px; border-radius: 10px;"/>
            {row[1]['company_name']}
        </h3>

        - Location: {row[1]['location_city']}, {row[1]['location_state']}
        - Founded: {row[1]['founding_year']}
        - Raised: {row[1]['money_raised']}
        - Status: {row[1]['stage']}
        
        > {row[1]['description']}
        
        <a href="https://{row[1]['domain']}" target="_blank">{row[1]['domain']}</a>
    """, unsafe_allow_html=True)
    st.divider()
