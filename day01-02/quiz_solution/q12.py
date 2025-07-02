Q12. 다음 코드의 문제점을 찾고 수정안을 제시하세요.
def append_to(element, to=[]):
    to.append(element)
    return to

## 정답

# 호출 예시
print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]
print(append_to(3))  # [1, 2, 3]

# ❌ 문제점 설명
# to=[]는 함수가 호출될 때마다 새로운 리스트를 생성하는 것처럼 보이지만,
# 실제로는 함수가 정의될 때 단 한 번만 평가되고 그 리스트가 계속 재사용됩니다.

# 즉, append_to()를 여러 번 호출해도 항상 같은 리스트 객체에 append가 누적되는 버그가 발생합니다.


# 🔍 시각적 메모리 구조
# 함수 정의 시점
# to ───► []

# 1차 호출 append_to(1)
# to ───► [1]

# 2차 호출 append_to(2)
# to ───► [1, 2]   ← 상태가 누적됨

# 3차 호출 append_to(3)
# to ───► [1, 2, 3] ← 의도치 않게 데이터가 축적됨


# ✅ 수정안: 올바른 코드
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


# 호출 예시
print(append_to(1))  # [1]
print(append_to(2))  # [2]
print(append_to(3))  # [3]


# ✅ 수정 이유
# None은 불변(immutable) 객체이므로 함수 정의 시 평가되어도 부작용 없음
# 함수가 호출될 때마다 to is None을 검사하여 새로운 리스트를 생성함
# 결과적으로 각 호출은 독립적인 리스트를 사용하게 되어 의도대로 동작


# 🧾 정답 예시 요약
# 문제점:
# - 디폴트 인자인 `to=[]`는 함수 정의 시 한 번만 평가되어, 여러 호출 간에 리스트가 공유되어 상태가 누적되는 버그가 발생합니다.

# 수정안:
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


# ✅ 실무 팁
# 상황	                         사용법
# 디폴트 인자로 불변 객체 사용	      OK (None, int, str, tuple)
# 디폴트 인자로 가변 객체 사용	      ❌ 반드시 None으로 대체하고 내부에서 새로 생성