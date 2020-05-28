#Print matrix
def p(matrix,n):
    for i in range(n):
        print(matrix[i])

#Rotates matrix 90 degrees Clockwise
def rotate_matrix(arr, size):
    rot = []
    for i in range(size):
        rot.append([])
        for j in range(size):
            rot[i].append(0)
    
    for i in range(size):
        for j in range(size):
            #Tranpose
            rot[i][j] = arr[j][i]
        for j in range(size//2):
            #Flip accross center
            rot[i][j], rot[i][size-j-1] = rot[i][size-j-1], rot[i][j]
    return rot


        


count= 0 
size=3 # input size
arr = []

#Creates original matrix
for i in range(size):
    arr.append([])
    for j in range(size):
        arr[i].append(count)
        count+=1

#Print original
p(arr, size)            
#Peform rotation magic on original matrix
rot = rotate_matrix(arr,3)
#Print rotates
p(rot, size)