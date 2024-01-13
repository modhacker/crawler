word_dic = {
    "dog": "강아지",
    "cat": "고양이",
    "tiger": "호랑이",
    "lion": "사자"
}
# lion 키값 출력
print(word_dic["lion"])
# tiger 키값 수정
word_dic["tiger"] = "호랭이"
# tiger 키값 출력
print(word_dic["tiger"])
# word_dic 전체 값 출력
print(word_dic)
# bear 추가
word_dic["bear"] = "곰"
# word_dic 전체 값 출력
print(word_dic)