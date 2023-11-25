# Pickle : 프로그램 상에서 사용되는 데이터를 파일 형태로 저장
# 열때는 binary가 포함

import pickle

profile_file = open("profile.pickle", "wb")    # write, binary / endcoding 설정 X
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)

# pickle을 이용해서 데이터를 파일에 쓰기
pickle.dump(profile, profile_file)    # pickle.dump(데이터, 파일) / 데이터를 파일에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb")    # read, binary
profile = pickle.load(profile_file)    # file에 있는 정보를 변수에 불러오기
print(profile)
profile_file.close()


# with 사용 시 파일을 열고 닫는 작업을 편하게 할 수 있음
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))    # 열었던 파일에 대해서 close() 필요 X

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

