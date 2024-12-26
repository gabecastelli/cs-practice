from typing import List

def binary_search(arr: List[int], target: int) -> int:
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    arr = [1, 4, 2, 8, 10, 25, 35]
    arr.sort()
    print(arr)
    print(binary_search(arr, 8))
    print(binary_search(arr, 12))

if __name__ == '__main__':
    main()