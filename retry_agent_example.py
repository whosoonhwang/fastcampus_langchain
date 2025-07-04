import os
from dotenv import load_dotenv
from typing import TypedDict, List
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, END

#환경 변수
load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# 도구 함수 정의
def add_two(x: str) -> str:
    try:
        return str(float(x) + 2)
    except Exception:
        return "도구 실행 실패: 숫자만 입력해 주세요."
    
def population_lookup(city: str) -> str:
    data = {
        "서울": "9,515,000명 (2023년 기준)",
        "부산": "3,343,000명 (2023년 기준)"
    }
    return data.get(city.strip().lower(), f"{city}의 인구 정보를 찾을 수 없습니다.")

# 메시지 상태 정의
class AgentState(TypedDict):
    messages: List[BaseMessage]

# 도구 리스트 정의
tools = [
    Tool(name="AddTwo", func=add_two, description="입력된 숫자에 2를 더하는 단순 계산 전용 도구입니다. 인구질의나 날짜 계산에는 절대 사용하지마세요."),
    Tool(name="PopulationLookup", func=population_lookup, description="도시 인구를 조회합니다.")
]

#LLM정의 (ReAct agent는 verbose=True만 있어도 추론 흐름 출력)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, verbose=True)

# ReAct Agent 생성
react_agent = create_react_agent(model=llm, tools=tools, debug=True)

#LangGraph 구성 (단순한 선형 흐름)
graph = StateGraph(AgentState)
graph.add_node("agent", react_agent)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

# 그래프 컴파일 
app = graph.compile()

# 테스트 실행
response = app.invoke({
    "messages": [HumanMessage(content="서율의 인구는 몇 명이야?")]
})

# 결과 출력
for m in response["messages"]:
    print(m.__class__.__name__,":",getattr(m, "content", repr(m)))
