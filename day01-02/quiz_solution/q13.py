# Q13. 다음 중 `copy.copy()`와 `copy.deepcopy()`의 차이를 예시와 함께 설명하세요.

# copy.copy(): 얕은 복사
# copy.deepcopy(): 깊은 복사 (내부 객체도 복사)

import copy
a = [[1, 2]]
b = copy.copy(a)
b[0].append(3)
print(a == b)
print(a is b)
print(b)
print(a)

c = copy.deepcopy(a)
c[0].append(3)
print(a == c)
print(a is c)
print(c)
print(a)

# 출력
# True
# False
# [[1, 2, 3]]
# [[1, 2, 3]]
# False
# False
# [[1, 2, 3, 3]]
# [[1, 2, 3]]

# 왜 이렇게 나오는지 이해하기
# copy는 내부 객체까지 복사하지 않으므로 내부 객체는 같은 객체를 참조하게 된다.
# deepcopy는 내부 객체까지 재귀적으로 복사하므로 원본과 완전 독립적인 객체가 된다.


# 추가 예제
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# 원본 수정
original[0][0] = 99

print("original:", original)   # [[99, 2], [3, 4]]
print("shallow:", shallow)     # [[99, 2], [3, 4]]  ← 내부 리스트 공유됨
print("deep:", deep)           # [[1, 2], [3, 4]]   ← 내부 리스트도 별도 복사됨

# 🧠 그림 설명 (텍스트로 표현)
# original = [[1, 2], [3, 4]]
#           └─┬────┘
#             ↓
#       ┌──────────────┐
#       │ list (outer) │
#       └──────────────┘
#        ↓        ↓
#    [1, 2]     [3, 4] ← 내부 리스트 (inner)

# copy()       → outer list는 새로 생성, inner는 기존 공유
# deepcopy()   → outer + inner list 모두 새로 복사

# 출력
# original: [[99, 2], [3, 4]]
# shallow: [[99, 2], [3, 4]]
# deep: [[1, 2], [3, 4]]

# ⚠️ 주의할 점
# 불변 객체(int, str, tuple 등)는 copy든 deepcopy든 차이 없음 (복사해도 같은 객체 참조)

# 복잡한 중첩 구조, 클래스 인스턴스, 딕셔너리 안의 리스트 등에서는 deepcopy() 필요

# ✨ 실전 팁
# 설정 파일, 게임 상태, 복잡한 데이터 구조에서 안전하게 원본을 보호하려면 deepcopy()

# 단순 복사만 필요할 때는 copy()
