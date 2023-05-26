class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        #not  my solution(remarks for self do it  again!)
        n = len(arr)
        i = n - 2

        # Find the first occurrence of arr[i] > arr[i+1]
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1

        if i == -1:
            return arr

        # Find the largest number in the suffix smaller than arr[i]
        j = n - 1
        while arr[j] >= arr[i] or arr[j] == arr[j-1]:
            j -= 1

        # Swap arr[i] with arr[j]
        arr[i], arr[j] = arr[j], arr[i]

        # # Sort the suffix starting from index i+1
        # arr[i+1:] = sorted(arr[i+1:])

        return arr
