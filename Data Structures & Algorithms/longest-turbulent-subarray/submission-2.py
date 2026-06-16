class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res=0
        def dfs(i,flag,ln):
            nonlocal res
            if i==len(arr)-1:
                if flag==True and arr[i]>arr[i-1]:
                    res=max(res,ln+1)
                    return 
                elif not flag and arr[i]<arr[i-1]:
                    res=max(res,ln+1)
                    return
                else:
                    res=max(res,ln)
                    return ln
            else:
                if flag and arr[i]>arr[i-1] :
                    res=max(res,ln)
                    dfs(i+1,False,ln+1)
                    return
                elif not flag and arr[i]<arr[i-1]:
                    res=max(res,ln)
                    dfs(i+1,True,ln+1)
                    return
                else:
                    res=max(res,ln)
                    if arr[i-1]<arr[i]:
                        dfs(i+1,True,1)
                    elif arr[i-1]>arr[i]:
                        dfs(i+1,False,1)
                    else:
                        dfs(i+1,False,1)
                        dfs(i+1,True,1)
                    return
        if len(arr)==1:
            return 1
        dfs(1,True,1)
        dfs(1,False,1)
        return res