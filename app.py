from main import get_few_shots_db_chain
import streamlit as st

st.title("Retail RAG Assistant: Database Q&A👕")

question=st.text_input("Question:")
if question:
    chain=get_few_shots_db_chain()
    answer= chain.run(question)
    st.header("Answer")
    st.write(answer)

