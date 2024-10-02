from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import PromptTemplate
from app.exception.exception import CustomException
from app.logger.logger import logging
from langchain_groq import ChatGroq
from app.config import Settings
import traceback
import sys


class EditorAgent:
    def __init__(self):
        self.prompt = PromptTemplate(input_variables=["content"],
                                     template="""You are an expert eBook content editor. Your task is to review and correct the given chapter content to improve its overall quality. Ensure that the content is clear, well-structured, grammatically correct, and written in a professional yet approachable tone.

        Here are your instructions:

        1. **Grammar and Spelling**: Correct any grammatical errors, spelling mistakes, or awkward phrasing.
        2. **Clarity**: Ensure the content is easy to understand. Simplify complex sentences where necessary and break down any overly complicated ideas.
        3. **Structure**: Ensure that the chapter has a logical flow with proper transitions between paragraphs. Add or adjust headings, subheadings, and sections if needed for better readability.
        4. **Tone**: Ensure the writing has a formal yet accessible tone, suitable for a general audience, such as students, researchers, or general readers.
        5. **Conciseness**: Eliminate redundancy and unnecessary filler content while keeping the chapter comprehensive.
        6. **Consistency**: Maintain consistent terminology, style, and formatting throughout the content.
        7. **Focus**: Ensure that the content stays on topic and avoids unnecessary digressions.

        Input:
        - **Chapter Content**: {content}

        Now, review and correct the given chapter content based on the instructions. Return the improved content as a single corrected string of text.
        Note: Don't include chapter number and chapter title in the content.
        \n\n placeholder:{agent_scratchpad}
        """)
        
        self.llm = ChatGroq(api_key=Settings().GROQ_API_KEY, model="Llama-3.1-8b-instant")
        self.tools = []

    def edit(self, content):
        try:
            # Use the prompt to edit chapter content
            research_agent = create_tool_calling_agent(self.llm,self.tools,self.prompt)
            research_agent_executor = AgentExecutor(agent=research_agent, tools=self.tools)
            response = research_agent_executor.invoke({"content":content})
            edited_content = response.get("output")

            return edited_content

        except Exception as e:
            logging.exception(F"Error: {e} | Traceback: {traceback.format_exc()}")
            raise CustomException(e,sys)