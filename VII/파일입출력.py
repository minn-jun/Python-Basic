# score_file을 새로 작성하기 위해 w(write)로 열기
score_file = open("score.txt", "w", encoding="utf8")

print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)

score_file.close()    # 파일을 열고난 후에는 반드시 닫기


# score_file에 새로운 내용을 추가하기 위해 a(append)로 열기
# 기존에 있던 파일을 "w"로 열게 되면 덮어쓰기가 됨.
score_file = open("score.txt", "a", encoding="utf8")

score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")    # .write를 사용할 시 줄바꿈 X

score_file.close()


# score_file에 있는 내용을 읽기 위해 r(read)로 열기
score_file = open("score.txt", "r", encoding="utf8")

# print(score_file.read())    # 파일 내 모든 내용 출력

print(score_file.readline())    # 줄 별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline(), end="")    # end=""를 넣어 줄바꿈 X
print(score_file.readline())

score_file.close()


score_file = open("score.txt", "r", encoding="utf8")

# 파일 내용이 몇 줄로 되어있는지 모를 경우
# while True:
#     line = score_file.readline()
#     if not line:    # 읽어온 내용이 없을 경우
#         break
#     print(line, end="")

lines = score_file.readlines()    # 모든 라인을 list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()