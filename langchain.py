#loading from hugging face
from langchain import HuggingFaceHub 
llm_hug = HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64})

#prompt templating
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
prompt = PromptTemplate(input_variables=['country'],
template = "tell me the capital of this {country}")

chain = LLMChain(llm=llm,prompt=prompt)
chain.run("india")

#combining multiple chain

prompt1 = PromptTemplate(input_variables=['country'],
                         template="tell me the capital of {country}")

chain1 = LLMChain(llm=llm,prompt=prompt1)

prompt2 = PromptTemplate(input_variables=['capital'],
                         template="suggest places to visis in {capital}")
chain2 = LLMChain(llm=llm,prompt=prompt2)

from langchain.chains import SimpleSequentialChain
chain = SimpleSequentialChain(chains=[chain1,chain2])
print(chain.run("india"))

#chat models

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
chatllm = ChatOpenAI(temperature=0.6,model='gpt-3.5-turbo')

chatllm
([SystemMessage(content="you are a comedian AI assistant"),
 HumanMessage(content="please provide some comedy punchline as")
 
 ])


#ooutput parses

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

class Commaseperatedoutput(BaseOutputParser):
    def parse(self,text:str):
        return text.strip().split()
    
template ="you are a helpful assistant.when user gives any input you should generate 5 words synonyms about it"
human_template ="{text}"
chatPrompt = ChatPromptTemplate.from_messages([
    ("system",template),
    ("human",human_template)
])

chain = chatPrompt|chatllm|Commaseperatedoutput()
chain.invoke({"text":"intelligent"})


#loading google gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

