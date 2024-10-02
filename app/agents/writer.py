from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import PromptTemplate
from app.exception.exception import CustomException
from app.logger.logger import logging
from langchain_groq import ChatGroq
from app.config import Settings
import traceback
import sys

    
class WriterAgent:
    def __init__(self):
        self.prompt = PromptTemplate(input_variables=["topic", "chapter"],
                                     template="""You are an expert eBook writer. Your task is to write a detailed, well-structured, and engaging chapter for an eBook based on the given chapter title and overall topic of the book. The chapter should be informative, easy to understand, and provide in-depth coverage of the subject matter.

        Here are your instructions:

        1. The content should be structured with proper headings, subheadings, and sections.
        2. The writing should be in a clear and engaging style, suitable for a broad audience such as students, researchers, or curious readers.
        3. Ensure the chapter content stays focused on the chapter title, but it should also be aligned with the overall topic of the book.
        4. Provide relevant examples, explanations, and any necessary background information to make the content more comprehensive and easier to understand.
        5. The length of the chapter should be around 1500-2000 words.
        6. Use a formal yet approachable tone. Avoid overly technical jargon unless it's explained well.

        Inputs:
        - **Topic**: {topic}
        - **Chapter Title**: {chapter}

        Now, based on the provided inputs, write the complete content for this chapter. The content should be returned as a single string of text.

        Note: Don't include chapter number and chapter title in the content.
        \n\n placeholder:{agent_scratchpad}
        """)
        
        self.llm = ChatGroq(api_key=Settings().GROQ_API_KEY, model="Llama-3.1-8b-instant")
        self.tools = []


    def write(self, chapter, topic):
        try:
            # Use the prompt to generate chapter titles
            research_agent = create_tool_calling_agent(self.llm,self.tools,self.prompt)
            research_agent_executor = AgentExecutor(agent=research_agent, tools=self.tools)
            response = research_agent_executor.invoke({"topic":topic, "chapter": chapter})
            chapter_content = response.get("output")

            return chapter_content

        except Exception as e:
            logging.exception(F"Error: {e} | Traceback: {traceback.format_exc()}")
            raise CustomException(e,sys)
