#maximum  consecutive ones in a binary array

n=[1, 1, 0, 1, 1, 1, 0, 1, 1, 1,1,1,1, 1, 0, 1]
def max_consecutive_ones(arr):
    max_count = 0
    count = 0

    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

print("Maximum consecutive ones:", max_consecutive_ones(n))