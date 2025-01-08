from pathlib import Path
import sys
import os, getpass
from langchain_community.tools.tavily_search import TavilySearchResults
import json


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("TAVILY_API_KEY")

# Tavily search tool
tavily_search = TavilySearchResults(max_results=3)
search_docs = tavily_search.invoke("成都明天天气如何？")
print(json.dumps(search_docs, indent=4, ensure_ascii=False))
