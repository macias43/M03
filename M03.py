class Solution:
    def sort012(self,arr,n):
        # code here
        a=0
        b=0
        c=0
        for i in range(0,len(arr),1):
            if arr[i]==0:
                a+=1
            elif arr[i]==1:
                b+=1
            elif arr[i]==2:
                c+=1
        for i in range(0,len(arr),1):
            if a>0:
                arr[i]=0
                a-=1
            elif b>0:
                arr[i]=1
                b-=1
            elif c>0:
                arr[i]=2
                c-=1