import streamlit as st
import pandas as pd

def main():
    st.title("Hello from streamlit-demo!")
    

    votes = pd.read_csv("votes.csv")
    votes = votes[votes['round'] == 'final']

    votes['jury_points'] = votes['jury_points'].fillna(votes['total_points'])
    
    # typography() 
    tab1, tab2, tab3 = st.tabs(["By country", "Favourites", "Raw"])
    with tab1: 
        st.subheader("Votes for country")
        votes_for_selected_country(votes)

    with tab2:
        st.subheader("Who likes whom")
        who_likes_whom(votes)
    
    with tab3:
        votes.shape
        votes

def votes_for_selected_country(votes):
    all_countries = votes['to_country'].unique()
    all_countries.sort()
    chosen_country = st.selectbox('Pick a country', all_countries)
    votes_per_year = votes.groupby(['to_country', 'year']).sum().reset_index()
    denmark = votes_per_year[votes_per_year['to_country'] == chosen_country]
    st.line_chart(denmark, x='year', y='jury_points')
 
def who_likes_whom(votes):
    favourite_country = votes[votes['jury_points'] == 12]
    favourite_country = favourite_country.groupby(['from_country', 'to_country'])['jury_points'].count().reset_index()

    st.scatter_chart(favourite_country, x='from_country', y='to_country', size='jury_points')
    

def typography():   
    st.header("How is it going?") 
    st.subheader("Typography")

    st.text("Regular text")
    "text without function call"
    1 + 2

    st.text("st.echo")
    with st.echo():
        1 + 2

    st.divider()
    st.badge("New")

if __name__ == "__main__":
    main()
