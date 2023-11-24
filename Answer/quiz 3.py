# 사이트 별 password 생성
# ex) http://naver.com
# 1. http:// 제외
# 2. 처음 만나는 (.) 이후 부분 제외
# 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"
# 생성 비밀번호 : nav51!

url = "http://google.com"
word = url.replace("http://", "")
word = word[:word.index(".")]
pw = word[:3] + str(len(word)) + str(word.count('e')) + "!"

print(f"{url}의 PW : {pw}")