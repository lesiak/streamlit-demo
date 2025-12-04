import streamlit as st
import pandas as pd

def main():
    st.title("Hello from streamlit-demo!")
    # typography() 

    votes = pd.read_csv("votes.csv")
    votes = votes[votes['round'] == 'final']

    votes['jury_points'] = votes['jury_points'].fillna(votes['total_points'])
    votes.shape
    votes

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
