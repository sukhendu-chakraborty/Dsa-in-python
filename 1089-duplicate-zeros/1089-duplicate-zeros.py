class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead
        """
        n = len(arr)
        c = 0
        for r in range (len(arr)):
            if arr[r]==0:
                c+=2
            else:
                c+=1
            if c>=n:
                break
        w = n-1
        if c == n+1:
            arr[w]=0
            w-=1
            r-=1
        while r >=0:
            if arr[r]!=0:
                arr[w]=arr[r]
                w-=1
            else:
                arr[w]=0
                arr[w-1]=0
                w-=2
            r-=1
        