from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from app.exception.exception import CustomException
from app.logger.logger import logging
from app.config import Settings
import sys

class ResearcherAgent:
    def __init__(self):
        self.prompt = PromptTemplate(input_variables=["topic"],
                                     template="""Generate a detailed outline with exactly 12 chapter titles on the given topic: {topic} for an ebook. \noutput format:\n
            Example: ['Title1', 'Title2', 'Title3', 'Title4', 'Title5', 'Title6', 'Title7', 'Title8', 'Title9', 'Title10', 'Title11', 'Title12']\n
            Ensure that the output contains exactly 12 chapters and that the chapter titles do not contain any special keywords or symbols. \nNote: Strictly output should be only a proper python list like ['Title1', 'Title2', 'Title3', 'Title4', 'Title5', 'Title6', 'Title7', 'Title8', 'Title9', 'Title10', 'Title11', 'Title12']. **Not a single world is allowed except the title list in the output**
            Ignore below text:
            \n placeholder:{agent_scratchpad}""")
        
        self.llm = ChatGroq(api_key=Settings().GROQ_API_KEY, model="Llama-3.1-8b-instant")
        # self.tools = [search]
        self.tools = []

    def research(self, topic):
        try:
            # Use the prompt to generate chapter content
            research_agent = create_tool_calling_agent(self.llm,self.tools,self.prompt)
            research_agent_executor = AgentExecutor(agent=research_agent, tools=self.tools)
            response = research_agent_executor.invoke({"topic":topic})
            response = response.get("output")

            chapters = [a.strip("'").strip(" ").strip("\n").strip("'") for a in response[1:-1].split(", ")]

            return chapters

        except Exception as e:
            logging.exception(e)
            raise CustomException(e,sys)