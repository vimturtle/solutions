with open("input/day20.txt") as f:
    nums1 = [int(n) for n in f.read().splitlines()]
    nums2 = [811589153 * n for n in nums1]


def mix(nums, times):
    curr = list(range(len(nums)))
    for _ in range(times):
        for i, num in enumerate(nums):
            loc = curr.index(i)
            del curr[loc]
            curr.insert((loc + num) % len(curr), i)

    return curr


def grove(nums, mixed):
    zero_index = mixed.index(nums.index(0))
    return sum(nums[mixed[(zero_index + n) % len(mixed)]] for n in (1000, 2000, 3000))


print(grove(nums1, mix(nums1, 1)), grove(nums2, mix(nums2, 10)))
