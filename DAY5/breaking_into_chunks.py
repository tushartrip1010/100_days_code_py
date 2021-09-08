def bc(gl,n):
    return [gl[ele:ele+n] for ele in range(1,len(gl),n)]

gl = [10, 45, 20, 62, 47, 85, 12, 63, 24, 78, 10]
n = 3
print(bc(gl, n))                                        
