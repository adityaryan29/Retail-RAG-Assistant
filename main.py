from langchain_groq import ChatGroq
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.vectorstores import Chroma
import os
from few_shots import few_shots

from dotenv import load_dotenv
load_dotenv()

def get_few_shots_db_chain():
    llm = ChatGroq(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        temperature=0.5
    )
    db_user="root"
    db_password="root"
    db_host="localhost"
    db_name="atliq-tshirts"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorestore = Chroma.from_texts(to_vectorize,
                                     embedding=embeddings,
                                     metadatas=few_shots
                                     )
    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorestore, k=2)
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}\n\n"
    )
    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )
    chain = SQLDatabaseChain.from_llm(
        llm,
        db,
        prompt=few_shot_prompt,
        verbose=True
    )
    return chain

if __name__ == '__main__':
    chain = get_few_shots_db_chain()
    print(chain.run("How many tshirts are left in stock in total in stock?"))











