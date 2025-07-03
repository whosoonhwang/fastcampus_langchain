# print("LangChain 테스트 시작")

# # ✅ 1. 환경변수 로딩용 모듈 가져오기
# import os
# from dotenv import load_dotenv
# # ✅ 2. .env 파일을 찾아서 환경변수로 로딩
# # 예: OPENAI_API_KEY=sk-xxxxx 가 환경에 등록됨
# load_dotenv()
# # ✅ 3. LangChain의 OpenAI 모델 객체 생성 시, 환경변수에서 키를 불러옴
# from langchain.llms import OpenAI
# # temperature=0: 창의성 줄이고 일관된 출력 기대
# # openai_api_key: 보안을 위해 코드에 직접 키를 쓰지 않고 환경에서 불러옴
# llm = OpenAI(
# temperature=0,
# openai_api_key=os.getenv("OPENAI_API_KEY")
# )



# import os
# from dotenv import load_dotenv

# load_dotenv()

# # 최신 방법에 맞게 import
# from langchain_community.llms import OpenAI

# llm = OpenAI(
#     temperature=0,
#     openai_api_key=os.getenv("OPENAI_API_KEY")
# )

import os
from dotenv import load_dotenv

load_dotenv()

# 최신 import 방법!
from langchain_openai import OpenAI

llm = OpenAI(
    temperature=0
)

response = llm("대한민국의 수도는?")
print(response)