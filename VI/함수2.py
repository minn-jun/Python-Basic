def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 기본값 사용
def a_profile(name, age=17, main_lang="파이썬"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

a_profile("유재석")
a_profile("김태호")


# 키워드값 사용
def b_profile(name, age, main_lang):
    print(name, age, main_lang)

b_profile(name="유재석", main_lang="파이썬", age=20)
b_profile(main_lang="자바", age=25, name="김태호")


# 가변인자 사용
# 필요한 전달값의 수가 다를 때
def c_profile(name, *language):
    print(f"이름:{name}", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

c_profile("유재석", "Python", "C", "C++", "C#")
c_profile("김태호", "Java", "Kotlin", "Go")