import os 
import google.generativeai as genai 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

load_dotenv()


os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model=genai.GenerativeModel('gemini-pro')

# response = model.generate_content("what is data science")
# print(response.text)

#using prompt templating

template = """ you are an helpful assistant , you are an expert that 
answer the question {question} in simple and bullet points"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt|llm|StrOutputParser()
result = chain.invoke(
    {
    'question':'what is data science'
    }
)
print(result)