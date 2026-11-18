import time


def is_palindrome(num):
    strnum = str(num)
    half = len(strnum)//2
    for i in range(half):
        if strnum[i] != strnum[len(strnum)-1-i]:
            return False
    return True

def find_2_sum(target):
    for i in range(1,target):
        if is_palindrome(i):
            if is_palindrome(target-i):
                return [target-i,i]
    return []

def find_sum(target):
    if is_palindrome(target):
        return [target]
    else:
        temp = find_2_sum(target)
        if len(temp) == 2:
            return temp
        for i in range(1,target):
            if is_palindrome(i):
                temp = find_2_sum(target-i)
                if len(temp) == 2:
                    return [i] + temp

start_time = time.perf_counter()
print(find_sum(109812))
end_time = time.perf_counter()
print(end_time-start_time)