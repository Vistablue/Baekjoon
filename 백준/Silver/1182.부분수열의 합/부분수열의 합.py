N, S = map(int, input().split())
nums = list(map(int, input().split()))

def count_subsets(idx, current_sum):   
    if idx == N:
        return 0

    count = 0

    if current_sum + nums[idx] == S:
        count += 1
        
    # 현재 숫자를 더하는 경우
    count += count_subsets(idx + 1, current_sum + nums[idx])

    #현재 숫자는 그냥 건너뛰는 경우
    count += count_subsets(idx + 1, current_sum)

    return count


print(count_subsets(0, 0))
