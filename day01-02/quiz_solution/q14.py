# Q14. 파이썬에서 값을 전달할 때, call by value인지 reference인지 설명하고 예시를 드세요.

# 파이썬은 객체 참조를 전달(call by object reference)

def f(x): x.append(1)  
a = []  
f(a)
print(a)
f(a)  
print(a)

# 출력
# [1]
# [1, 1]

# 왜 이렇게 나오는지 이해하기
# 파이썬은 객체 참조를 전달(call by object reference)하므로 계속 원본 객체에 추가된다.

# 📌 주제: 파이썬은 객체 참조를 전달한다 (Call by Object Reference)
# 🧠 왜 이런 결과가 나오는가?
# a = [] → 빈 리스트 객체 생성
# f(a) 호출 → x는 a와 같은 리스트를 참조
# x.append(1) → 리스트 a 자체가 수정됨 (같은 객체니까!)
# 따라서 f()를 또 호출하면 a에 또 1이 추가됨



# 📦 파이썬은 Call by Value도 Call by Reference도 아님!

# 파이썬은 call by object reference 또는 call by sharing이라 불림
# 함수 인자 x는 객체의 참조값을 복사해서 전달
# 따라서 객체 자체가 mutable일 경우, 함수 내에서 외부 객체를 수정 가능


# 🔍 메모리 기준 시각적 이해

# a = []           # a → list object #1 (빈 리스트)

# f(a)             # x → list object #1
# 내부에서 object #1에 .append(1)

# f(a)             # x → 여전히 list object #1
# 다시 .append(1)

# 결국 a, x 모두 같은 메모리 주소의 객체를 가리킴.


# 🔁 반례: 불변 객체 (immutable)
def f(x):
    x = x + 1

a = 10
f(a)
print(a)   # 여전히 10

# ✅ 이유
# x = x + 1 → 새로운 int 객체를 만들고 x에 바인딩할 뿐

# 원래 a가 참조하던 객체는 변경되지 않음


# 📚 연습용 확장 예제
def f(x):
    x[0] = 99 # 내부 객체 수정

a = [1, 2, 3]
f(a)
print(a)  # [99, 2, 3]

# → 이 경우는 같은 객체를 참조한 채 그 객체의 내용을 수정했기 때문에 외부에서도 변화가 보입니다.


# ❓ 아래 코드는 왜 a는 그대로일까?
def f2(x):
    x = [99, 100]

a = [1, 2, 3]
f2(a)
print(a)  # [1, 2, 3] ← 내부 변경이 아닌 재바인딩이므로 영향 없음

# 🔍 핵심 개념: "함수 내부에서의 재바인딩은 외부 객체에 영향을 주지 않는다"
a = [1, 2, 3]
# → 변수 a는 어떤 리스트 객체를 참조

# f(a) 호출 시,
# → x라는 이름도 동일한 리스트를 참조하게 됨

# 하지만 x = [99, 100]는 기존 객체를 수정한 것이 아니라
# x가 새로운 리스트 객체를 참조하도록 재바인딩한 것

# 함수 내부에서 x가 새로운 객체를 가리키더라도
# 외부의 a는 여전히 원래 리스트를 참조하고 있음

# 🧠 시각적 설명 (텍스트로 메모리 표현)
# 1. 함수 호출 전:
# a ──► [1, 2, 3]

# 2. 함수 내부:
# x ──► [1, 2, 3]   ← a와 같은 객체 참조
# x = [99, 100]     ← 이제 x는 새로운 리스트를 참조함
# x ──► [99, 100]   ← a와의 연결은 끊김

# 3. 함수 호출 후:
# a ──► [1, 2, 3]   ← 원래 객체는 변경되지 않음



# 🔍 실전 예제: 딕셔너리 수정
def f(x):
    x['a'] = 99

a = {'a': 100}
