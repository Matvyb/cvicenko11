import random


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def dcd(x):
    for i in range(x):
        print(i)


def main():
    numbers = random_numbers(10)
    sorted_num = bubble_sort(numbers)
    print(sorted_num)
    print(dcd(3))


if __name__ == "__main__":
    main()
