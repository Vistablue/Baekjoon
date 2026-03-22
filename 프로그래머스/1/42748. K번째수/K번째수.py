def solution(array, commands):
    answer = []
    # 중첩 인덱싱 형태
    for c in commands: # [[2, 5, 3], [4, 4, 1], [1, 7, 3]] 형태면 
        i = c[0] # 첫번째루프에서 [2,5,3]의 0번째 인덱스 2를추출
        j = c[1]
        k = c[2]
        
        # 파이썬 슬라이싱 규칙때문에 -1
        slice = array[i-1:j]
        slice.sort()
        
        answer.append(slice[k-1])
        
    return answer

