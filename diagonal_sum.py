import numpy as np


res =np.array( [[11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]])
        
# Reversing the arrays
diags = [res[::-1,:].diagonal(i) for i in range(-3,4)]
diags.extend(res.diagonal(i) for i in range(3,-4,-1))
end_res = [n.tolist() for n in diags]
diag_1 = end_res[3]
diag_2 = end_res[10]
count = 0
for i in (diag_1+diag_2):
    count = count+i
print count


#Output
23
