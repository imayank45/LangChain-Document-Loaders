from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    input_variables=["poem"],
    template="Write a summary on following poem:\n\n{poem}",
)

parser = StrOutputParser()

chain = prompt | model | parser


loader = TextLoader("poem-on-football.txt")

docs = loader.load()
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)

results = chain.invoke({'poem':docs[0].page_content})
print(results)