from langchain.agents import Agent, AgentExecutor, create_react_agent
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import tool
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def search_places(destination: str) -> str:
    """Search for the best places to visit in the given destination."""
    # This function would contain logic to search for places.
    return f"Best places to visit in {destination}: Get the latest information about the best places to visit in {destination}. And the local attractions."

# model = ChatMistralAI(
#     model="mistral-large-latest",
#     api_key=os.getenv("MISTRAL_API_KEY"),
#     temperature=0.2,
# )

model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-pro",
    api_key = os.getenv("GOOGLE_API_KEY"),
)

template = "Give all the details about the travel destination {destination}. Include information about the best places to visit, things to do, and accommodations."

prompt_template = ChatPromptTemplate.from_template(template)

new_prompt_template = hub.pull("hwchase17/react")

tools = [
    search_places,
]

researcher = create_react_agent(
    # name = "Travel Researcher",
    # role = "Searches for travel destinations, activities, and accommodations based on user preferences",
    llm = model,
    tools=tools,
    prompt = new_prompt_template,

    # verbose = True,
)

result =  AgentExecutor(
    agent=researcher,
    tools=tools,
    verbose=True,
)

while True:
    destination = input("Enter your travel destination: ")
    if destination.lower() == "exit":
        break
    result.invoke({"destination": destination, "input": prompt_template})
    print(result)
    print("--------------------------------------------------")

