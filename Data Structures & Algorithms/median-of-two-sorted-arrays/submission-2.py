class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median: even: 2 numbers. odd: 1 number
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        # 1 1 1 1 1
        # 1 2 3 4 5 6 7 8 9

        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = l + (r - l) // 2
            j = half - i - 2

            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-inf")
            if i + 1 < len(A):
                Aright = A[i + 1]
            else:
                Aright = float("inf")

            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float("-inf")
            if j + 1 < len(B):
                Bright = B[j + 1]
            else:
                Bright = float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min (Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            
