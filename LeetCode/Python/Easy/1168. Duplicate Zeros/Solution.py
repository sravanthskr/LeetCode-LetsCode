class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        read = 0
        slot = 0
        while slot<len(arr):
            if arr[read]!=0:
                slot+=1
            else:
                slot+=2
            read+=1
        
        read-=1
        write = len(arr)-1

        if slot>len(arr):
            arr[len(arr)-1]=0
            read-=1
            write-=1
        
        while read>0:
            if arr[read]!=0:
                arr[write]=arr[read]
                write-=1
                read-=1
            else:
                arr[write]=0
                arr[write-1]=0
                write-=2
                read-=1
        return arr