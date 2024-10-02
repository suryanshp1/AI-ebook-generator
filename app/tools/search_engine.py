from langchain_community.tools import DuckDuckGoSearchRun
from typing import Annotated, List, Tuple, Union
from langchain_core.tools import tool


@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun(max_results=2).run(search_query)