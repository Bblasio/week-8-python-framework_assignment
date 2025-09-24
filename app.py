import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def run_app():
    st.title("WHO COVID-19 Global Data Explorer")
    st.write("Simple exploration of global COVID-19 case and death statistics by country and region.")
    # Load data
    import os
    if not os.path.exists('metadata.csv'):
        st.error("metadata.csv not found in the app directory. Please ensure the file is present.")
        st.stop()
    df = pd.read_csv('metadata.csv')
    # Sidebar filters
    regions = df['WHO Region'].unique().tolist()
    selected_region = st.sidebar.selectbox("Select WHO Region", ["All"] + regions)
    if selected_region != "All":
        df = df[df['WHO Region'] == selected_region]
    # Top 10 countries by cumulative cases
    st.subheader("Top 10 Countries by Cumulative Cases")
    top_cases = df.sort_values('Cases - cumulative total', ascending=False).head(10)
    fig1, ax1 = plt.subplots()
    ax1.barh(top_cases['Name'], top_cases['Cases - cumulative total'])
    ax1.set_xlabel('Cumulative Cases')
    ax1.set_ylabel('Country')
    ax1.set_title('Top 10 Countries by Cumulative Cases')
    st.pyplot(fig1)
    # Top 10 countries by cumulative deaths
    st.subheader("Top 10 Countries by Cumulative Deaths")
    top_deaths = df.sort_values('Deaths - cumulative total', ascending=False).head(10)
    fig2, ax2 = plt.subplots()
    ax2.barh(top_deaths['Name'], top_deaths['Deaths - cumulative total'])
    ax2.set_xlabel('Cumulative Deaths')
    ax2.set_ylabel('Country')
    ax2.set_title('Top 10 Countries by Cumulative Deaths')
    st.pyplot(fig2)
    # Show sample data
    st.subheader("Sample Data Table")
    st.dataframe(df.head(20))

if __name__ == "__main__":
    run_app()
