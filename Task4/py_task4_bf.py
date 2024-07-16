def calculate_moves(array, target) -> int:
    res = 0

    for element in array:
        res += abs(target - element)
    return res


nums = []


with open('numbers.txt', 'r') as f:
    for line in f:
        nums.append(int(line))


results = []
for element in set(nums):
    results.append(calculate_moves(nums, element))


print(min(results))
