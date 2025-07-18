# Q1. 다음 코드의 출력 결과와 a is b 결과를 적으세요.

a = [1, 2, 3]
b = a
b.append(4)
print('a:', a)
print('a is b:', a is b)

# 출력
# a: [1, 2, 3, 4]
# a is b: True

# 왜 이렇게 나오는지 이해하기
# a와 b는 같은 객체를 참조하고 있기 때문에, b.append(4)를 하면 a도 변경된다.
# 즉, a와 b는 같은 객체를 참조하고 있기 때문에, a is b는 True가 나온다.

# ✅ 왜 이런 결과가 나올까?
# 🔍 핵심 개념: “변수는 객체를 참조한다”

b = a

# b는 a가 참조하고 있는 같은 객체를 참조하게 됨
# 즉, a와 b는 동일한 리스트 객체를 가리킴

b.append(4)

# 리스트는 **가변 객체(mutable)**이므로
# b.append(4)는 객체 자체를 수정
# a와 b는 같은 리스트를 공유하고 있으므로 → a도 변경된 것처럼 보임


# 🧠 메모리 구조 시각화
# 1️⃣ 초기 상태
# a ──► [1, 2, 3]

# 2️⃣ b = a 이후
# a ──┐
#     │
# b ──┘        →  [1, 2, 3]

# 3️⃣ b.append(4) 이후
# a ──┐
#     │
# b ──┘        →  [1, 2, 3, 4]

# 둘 다 같은 리스트를 공유하므로, 하나를 바꾸면 양쪽에 모두 반영됨


# 🔍 is 와 == 차이 확인
print(a == b)  # True → 값이 같음
print(a is b)  # True → 같은 객체 (id 같음)


# 🧪 실험: ID 확인
print(id(a))  # 예: 140330123456
print(id(b))  # 예: 140330123456 (같음)


# ❗️중요 비교 예제
a = [1, 2, 3]
b = a[:]        # 복사본 생성
b.append(4)

print(a)        # [1, 2, 3]
print(b)        # [1, 2, 3, 4]
print(a is b)   # False

# b = a[:]는 **얕은 복사(shallow copy)**이므로 서로 다른 객체


# ⚠️ 실무에서 주의할 점
# 리스트 같은 가변 객체를 다음과 같이 함수에 넘기면 원하지 않는 부작용이 생길 수 있음:

def f(x):
    x.append(999)

a = [1, 2, 3]
f(a)
print(a)  # [1, 2, 3, 999] ← 함수 안에서 바뀜!

# → 이런 경우에는 복사해서 넘기거나, 내부에서 새 리스트를 생성하는 방식을 고려해야 함


# ✅ 요약
# 개념	             설명
# a = [...]	        리스트 객체 생성
# b = a	            같은 객체 참조
# b.append(...)	    원본 리스트 변경됨 (가변 객체)
# a is b	        True (같은 객체)
# a == b	        True (값도 같음)

