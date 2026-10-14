# find missing number in array


def find_missing(arr, n):
    total = (n * (n + 1)) // 2
    sum_arr = sum(arr)
    return total - sum_arr

# Example usage
arr = [1, 2, 4, 5, 6]
n = 6
print("Missing number is:", find_missing(arr, n))