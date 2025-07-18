# Q19. 파이썬에서 객체가 메모리상에서 사라지는 시점은 언제인가요? 간단한 예를 드세요.

# 참조가 0이 되면 GC에 의해 메모리 해제됨

a = [1, 2, 3]
del a  # 이후 메모리에서 사라짐
# 이후 a는 사용할 수 없음 → NameError 발생


# ✅ 핵심 개념: 참조 카운트(Reference Count)
# 파이썬의 객체 메모리 관리는 크게 두 가지 메커니즘으로 이루어집니다:
# 참조 카운팅(Reference Counting) ← 기본 방식
#가비지 컬렉터(Garbage Collector) ← 순환 참조 처리용


# 🧠 참조 카운트란?
# 객체가 생성되면 파이썬은 그 객체를 참조하는 변수나 이름의 수를 세고 있습니다.
# 참조 수가 0이 되면 → 해당 객체는 더 이상 사용되지 않음
# 그 순간 → 메모리에서 자동 해제


# 🧪 예제 흐름 설명
a = [1, 2, 3]      # 리스트 객체 생성, 참조 수: 1 (a)
b = a              # 참조 수: 2 (a, b)
del a              # 참조 수: 1 (b)
del b              # 참조 수: 0 → 메모리 해제됨


# 🧪 실제 실험
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 이상: getrefcount(x) 함수도 잠깐 참조함

y = x
print(sys.getrefcount(x))  # 3

del x
print(sys.getrefcount(y))  # 2

del y
# 이 시점에서 리스트는 참조 0 → 메모리에서 해제


# ❌ del이 객체를 지우는 게 아니다?
a = [1, 2, 3]
b = a
del a
print(b)  # 여전히 [1, 2, 3]

# → del a는 단지 변수 a와 객체의 연결을 끊는 것
# → 객체 자체는 여전히 살아 있음 (왜냐면 b가 참조하고 있으니까)


#💥 del 이후 사용 시 에러
a = [1, 2, 3]
del a
print(a)  # ❌ NameError: name 'a' is not defined


# 🔁 순환 참조는 어떻게 처리할까?
a = []
a.append(a)
del a
# 참조 카운트는 1이지만 → 순환 참조
# → 이럴 땐 파이썬의 `gc` 모듈이 처리

#→ 파이썬은 **순환 참조 탐지 및 해제를 위한 가비지 컬렉터(GC)**를 별도로 운영함


# ✅ 요약
# 동작	              의미
# del 변수명	       해당 변수의 이름과 객체 연결 끊음 (객체는 삭제되지 않을 수 있음)
# 참조 수가 0	       객체가 아무도 참조하지 않음 → 메모리에서 자동 삭제
# gc 모듈	          순환 참조 같은 특수 케이스에서 추가 정리 수행