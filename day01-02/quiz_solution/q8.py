# Q8. `id()` 함수의 의미는 무엇인가요? 직접 예시를 들어 설명해보세요.

# 정답 예시:
# id()는 객체의 고유한 메모리 주소(혹은 identity)를 반환합니다.

a = [1,2,3]
b = a
print(id(a), id(b))  # 같은 주소



# 🔍 id() 함수란?
# id(obj)는 **파이썬 객체의 정체성(identity)**을 나타내는 고유한 정수값을 반환합니다.

# 이 값은 객체가 메모리상에서 차지하는 주소에 대응하는 값입니다.
# (CPython 구현에서는 실제 메모리 주소와 거의 같음)


# 📘 공식 정의 (Python Doc)
# id(object)
# Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.


# 🧪 예제
a = [1, 2, 3]
b = a

print(id(a))  # 예: 140330123456
print(id(b))  # 예: 140330123456 (같음)
print(a is b) # True

#✨ 해설:
# a와 b는 같은 리스트 객체를 참조하므로 id(a) == id(b)

# 따라서 a is b는 True



# 🔁 반례: 다른 객체
x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))  # 예: 140330111000
print(id(y))  # 예: 140330222000 (다름)
print(x == y) # True (값은 같음)
print(x is y) # False (객체는 다름)


# ⚠️ 주의: id()는 객체가 소멸되면 재사용될 수 있음
a = [1, 2, 3]
print(id(a))   # 예: 1400...

del a

b = [4, 5, 6]
print(id(b))   # 같은 id 나올 수도 있음! (GC 후 주소 재사용)
# → id 값은 객체가 살아 있는 동안만 고유함


# 💬 실무 활용
# a is b의 내부 비교에 사용됨: id(a) == id(b)
# 객체 동일성 체크 (예: None, singleton, memoization 등)
# 디버깅할 때 객체 추적에 유용함


# ✅ 요약
# 항목	            설명
# id()	          객체의 고유한 identity (보통 메모리 주소) 반환
# ==	          값 비교
# is	          객체 비교 (id(a) == id(b))
# 가변 객체	        같은 id면 내부 수정 공유
# 불변 객체	        같은 값을 가지더라도 다른 id일 수 있음



# 📌 정답 요약 예시

# `id()` 함수는 객체의 고유한 정체성(= identity)을 나타내는 정수값을 반환합니다.  
# CPython에서는 이 값은 객체의 메모리 주소와 유사하며, 객체가 살아 있는 동안 유일하게 유지됩니다.

# 예:
a = [1, 2, 3]
b = a
print(id(a), id(b))  # 같은 객체 → 같은 id
