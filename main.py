import streamlit as st
import pandas as pd

def main():
    st.title("Hello from streamlit-demo!")
    

    votes = pd.read_csv("votes.csv")
    votes = votes[votes['round'] == 'final']

    votes['jury_points'] = votes['jury_points'].fillna(votes['total_points'])
    
    # typography() 
    who_likes_whom(votes)


    votes.shape
    votes


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
