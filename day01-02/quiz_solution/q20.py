# Q20. del 키워드의 역할은 무엇인가요?

# 🔍 정의
# del은 변수 이름(name), 리스트/딕셔너리의 항목, 슬라이스, 객체 속성 등을 삭제하는 파이썬 키워드입니다.
#
# 하지만 핵심은 다음과 같습니다:
# del은 객체 자체를 삭제하는 것이 아니라, 객체에 연결된 **참조(바인딩된 이름)**를 제거하는 것이다.


# 📘 공식 설명 (Python Docs)
# "del deletes the reference to a name. 
# If the object is no longer referenced, it will be garbage collected."


# ✅ 예제 1: 변수 삭제
x = [1, 2, 3]
del x

# ❌ 이후 x는 참조 불가
print(x)  
# Traceback (most recent call last):
#   File "<python-input-14>", line 4, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined#

# x라는 이름이 객체와의 연결이 끊김
# 객체 자체는 다른 참조가 없다면 GC(Garbage Collector)에 의해 메모리에서 해제


# ✅ 예제 2: 리스트 요소 삭제
a = [1, 2, 3, 4]
del a[1]
print(a)  # [1, 3, 4]
# 인덱스 1(값: 2)에 해당하는 리스트 요소가 제거됨


# ✅ 예제 3: 딕셔너리 키 삭제
d = {'name': 'Alice', 'age': 30}
del d['age']
print(d)  # {'name': 'Alice'}


# ✅ 예제 4: 슬라이스 삭제
a = [1, 2, 3, 4, 5]
del a[1:4]
print(a)  # [1, 5]

# ✅ 예제 5: 객체 속성 삭제
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Alice')
del p.name
# ❌ 이후 p.name는 참조 불가
print(p.name)  # ❌ AttributeError: 'Person' object has no attribute 'name'
# 객체 속성 삭제 후 접근 시 에러


# 🧠 메모리 관점 이해
x = [1, 2, 3]
y = x
del x

# del x는 이름 x를 삭제할 뿐
# 객체 [1, 2, 3]은 여전히 y가 참조하고 있음
# → 메모리에서 해제되지 않음


# ⚠️ 주의할 점
# del은 변수명 또는 컬렉션 요소를 제거할 뿐,
# 객체 자체를 무조건 없애는 것은 아님
# 참조 수가 0이 된 객체만 메모리에서 제거됨 (Garbage Collected)


# ✅ 정리 요약
# 기능	                예시	                        설명
# 변수 삭제	           del x	                        변수 x 이름 삭제
# 리스트 요소 삭제	     del a[0]	                      인덱스 0 요소 제거
# 슬라이스 삭제	        del a[1:3]	                     리스트 일부 요소 제거
# 딕셔너리 키 삭제	     del d['key']	                  키-값 쌍 삭제
# 객체 자체 제거	    x에 대한 참조가 0이 될 때만 제거됨	     자동 GC 수행


# 🧾 Q20 답안 예시
# del 키워드는 변수, 리스트 요소, 딕셔너리 키 등에 대한 이름 또는 항목을 삭제하는 역할을 합니다.
# 이는 객체 자체를 삭제한다기보다는, 객체에 연결된 참조를 해제하는 것입니다.
# 예를 들어:

x = [1, 2, 3]
del x
print(x)  # ❌ NameError: 'x' is not defined

# 이 경우 x라는 이름이 제거되어 더 이상 사용할 수 없게 되며,
# 객체는 참조가 남아있지 않다면 자동으로 메모리에서 해제됩니다.