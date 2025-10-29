A = [1, 2, 3, 4, 5]
B = [0, 0, 0, 0, 0]
n = 4
for i in range(1, n + 1):
    s = 0
    for j in range(1, i + 1):
        for k in range(1, j + 1):
            s = s + A[k]
    B[i] = s
    
print(B)


# import numpy as np
# # i j
# # k l
# def order(matrix):
#     identity = np.matrix([[1, 0], [0, 1]])
#     pow = matrix
#     exponent = 0
#     while not np.all(np.equal(matrix, identity)):
#         exponent += 1
#         pow = matrix * pow
#     return exponent

# for i in range(0,2):
#     for j in range(0,2):
#         for k in range(0,2):
#             for l in range(0,2):
#                 mat = np.matrix([[i, j], [k, l]])
#                 det = np.linalg.det(mat)
#                 if abs(det) % 2 == 0:
#                     continue
#                 print(mat)
#                 print(order(mat))
#                 print()
                