# Space complexity (memory usage) 
# Most of the time, time complexity > space complexity 
# Most of the time, improving runtime comes at at the cost of space 

# When analyzing space complexity, we only consider additional memory 
# that we use 

# Space complexity: O(n) since the number of key-value pairs we store 
# in our dictionary == len(nums)
def two_sum(nums, target):
    d = {} # O(1)

    for index, num in enumerate(nums):  # O(n)
        d[num] = index

    # how many elements are in our dictionary? 
    # the number of key-value pairs in our dictionary == len(nums) 

    for index, num in enumerate(nums):  # O(n)
        diff = target - num

        if diff in d:
            if diff == num: 
                continue

            return [index, d[diff]]

    return [-1, -1]

# [1, 2, 3, 4, ..., 1000, 1, 2, 3, 4, ... 999]
# { 1, 2, 3, 4, ..., 1000 } 
# O(1/2 * n) ~ O(n)
def find_single_number(nums):
    s = set() # O(1)

    # Space complexity: O(n)
    for num in nums:
        if num in s:
            s.remove(num)
        else:
            s.add(num)

    return s.pop()

# Big O always assumes the worst case 
# [1, 2, 3, 4, 5], target = 1
# [1, 2, 3, 4, 5], target = 5 
# When you're doing time/space complexity analysis,
# assume the most conversative case 
def search(array, target):
    for item in array:
        if item == target:
            return True 

    return False


# my_list: O(n)
# my_second_list: O(26) 
# O(n) + O(26) == O(26 + n) ~ O(n)
def do_a_couple_things(n):
    my_list = []
    my_second_list = [0] * 26

    for _ in range(n):
        my_list.append("lambda")
        print(my_second_list[n % 25])

    return my_list
    