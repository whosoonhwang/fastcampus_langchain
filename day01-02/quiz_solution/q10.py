# Q10. 다음 중 `a is b`가 `True`를 반환할 가능성이 가장 높은 경우는? 본인의 생각을 작성해보세요.

# 1
a = 10; b = 10
print(a is b)
#
# 2
a = []; b = []
print(a is b)

# 3
a = {}; b = {}
print(a is b)

# 4
a = 'hello'; b = ''.join(['h', 'e', 'l', 'l', 'o'])
print(a is b)

# 출력
# True
# False
# False
# False

# 왜 이렇게 나오는지 이해하기
# 1. a와 b는 같은 객체를 참조하고 있기 때문에, a is b는 True가 나온다. -5~256 정수는 캐시되어 있음
# 2. a와 b는 다른 객체를 참조하고 있기 때문에, a is b는 False가 나온다. 리스트는 가변 객체이므로 새로운 객체를 생성
# 3. a와 b는 다른 객체를 참조하고 있기 때문에, a is b는 False가 나온다. 딕셔너리는 가변 객체이므로 새로운 객체를 생성
# 4. a와 b는 다른 객체를 참조하고 있기 때문에, a is b는 False가 나온다. 문자열은 불변 객체이므로 새로운 객체를 생성



# ✅ 정답: 1번
# 이유:
# **정수 10은 작은 정수(small integer)**에 해당 → 파이썬 내부에서 캐싱됨
# 파이썬은 -5 ~ 256 사이의 정수 객체를 미리 만들어 두고 공유하므로,

a = 10
b = 10
print(a is b)  # True
# → a와 b는 동일한 객체를 참조하게 됨 (a is b == True)


# ❌ 오답 해설
# 2. a = []; b = []
# 리스트는 매번 새로운 객체 생성

# a is b → False

a = []
b = []
print(a is b)  # False


# 3. a = {}; b = {}
# 딕셔너리도 리스트와 마찬가지로 매번 새로운 객체 생성

# a is b → False



# 4. a = 'hello'; b = ''.join(['h','e','l','l','o'])
# 이건 문자열 내용은 같지만,
# ''.join()을 통해 런타임에 생성된 문자열 → interning이 보장되지 않음

a = 'hello'
b = ''.join(['h', 'e', 'l', 'l', 'o'])
print(a == b)  # True
print(a is b)  # False (보통은)

# a is b는 False일 가능성이 높음
# 물론 sys.intern()을 사용하면 True가 될 수 있음 (강제 intern 가능)


# 🧠 정리: a is b == True 가능성 순위
# 선택지	가능성	   이유
# 1번	   ✅ 높음	정수 10은 캐싱됨 (-5~256)
# 4번	   ⚠️ 중간	 문자열 interning은 상황에 따라 다름
# 2번	   ❌ 낮음	[]는 새 리스트
# 3번	   ❌ 낮음	{}는 새 딕셔너리


# ✅ 결론
# 정답: 1번 a = 10; b = 10
# 이유: 파이썬은 -5 ~ 256 범위의 정수를 캐싱하므로 a is b가 True일 가능성이 가장 높습니다.