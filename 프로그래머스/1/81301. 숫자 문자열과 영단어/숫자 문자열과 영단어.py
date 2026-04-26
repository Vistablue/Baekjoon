def solution(s):
    words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    for i, word in enumerate(words):
        s = s.replace(word, str(i))

    return int(s)


# 테스트
print(solution("one4seveneight"))  
print(solution("23four5six7"))     
print(solution("2three45sixseven"))
print(solution("123"))              