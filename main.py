import streamlit as st

def main():
    st.title("Hello from streamlit-demo!")
    typography()

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
