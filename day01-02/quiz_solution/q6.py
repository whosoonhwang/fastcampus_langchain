# Q6. 다음 중 `id(a) == id(b)`를 만족하는 경우를 고르세요. (복수선택 및 무선택 가능)

#a
a = [1, 2]; b = a
print(id(a) == id(b))

#b
a = [1, 2]; b = [1, 2]
print(id(a) == id(b))

#c  
a = (1, 2); b = (1, 2)
print(id(a) == id(b))

#d
a = 300; b = 300
print(id(a) == id(b))

#e
a = 'abc'; b = 'abc'
print(id(a) == id(b))


# 출력
# True
# False
# False
# False
# True

# 왜 이렇게 나오는지 이해하기
# a 같은 리스트 객체 참조
# b 다른 리스트 객체 참조
# c 다른 튜플 객체 참조
# d 같은 정수 객체 참조
# e 같은 문자열 객체 참조 (문자열 interning 가능성 있음)

추가 설명

# 🔍 개념 정리
# Interning: 동일한 문자열을 여러 번 생성해도 같은 메모리 주소를 사용하도록 하는 최적화

# 적용 대상:
# 짧고 자주 사용되는 문자열 (특히 영문자, 숫자, 밑줄만 포함된 경우)

# 변수명, 키워드처럼 파이썬 내부에서 자주 쓰이는 문자열

# 직접 intern 처리한 문자열 (sys.intern() 사용)

a = "hello"
b = "hello"
print(a is b)  # True (interned)

a = "hello world"
b = "hello world"
print(a is b)  # 보장되지 않음 (False일 수 있음)


# 🧪 실험 코드

a = 'hello'
b = ''.join(['h', 'e', 'l', 'l', 'o'])

print(a == b)     # True (내용 동일)
print(a is b)     # False (객체 다름)


import sys

a = 'hello'
b = ''.join(['h', 'e', 'l', 'l', 'o'])
c = sys.intern(b)

print(a is c)     # True (interned to same object)

# 문자열 interning은 성능 및 메모리 사용 최적화를 위해 사용되며, is 비교에서 주의해야 합니다.
# 문자열이 자동 intern 되는지 여부는 문자열 내용과 생성 방식에 따라 다릅니다.
# intern 적용 여부를 강제하려면 sys.intern()을 사용하세요.
