import random
from pysat.solvers import Glucose3
import csv

try:
    k = input("please put k value: ")
    k = int(k)
except ValueError:
    print("k is not a number")


arr = []
for temp in range(1,k*k+1):
    arr.append(temp)

grid = []
for temp in range(k*k):
    temp1 = []
    for temp2 in range(k*k):
        temp1.append(0)
    grid.append(temp1)


N = k*k
    
    # A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
    
    # Checks whether it will be
    # legal to assign num to the
    # given row, col
def isSafe(grid, row, col, num):
    
        # Check if we find the same num
        # in the similar row , we
        # return false
    for x in range(N):
        if grid[row][x] == num:
            return False
    
        # Check if we find the same num in
        # the similar column , we
        # return false
    for x in range(N):
        if grid[x][col] == num:
            return False
    
        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
    startRow = row - row % k
    startCol = col - col % k
    for i in range(k):
        for j in range(k):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
    
    # Takes a partially filled-in grid and attempts
    # to assign values to all unassigned locations in
    # such a way to meet the requirements for
    # Sudoku solution (non-duplication across rows,
    # columns, and boxes) */
def solveSudoku(grid, row, col):
    
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
    if (row == N - 1 and col == N):
        return True
        
        # Check if column value  becomes 9 ,
        # we move to next row and
        # column start from 0
    if col == N:
        row += 1
        col = 0
    
        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
        
    for num in range(1,N+1):
        
            # Check if it is safe to place
            # the num (1-9)  in the
            # given row ,col  ->we
            # move to next column
        if isSafe(grid, row, col, num):
            
                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
            grid[row][col] = num
    
                # Checking for next possibility with next
                # column
            if solveSudoku(grid, row, col + 1):
                return True
    
            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
        grid[row][col] = 0
    return False
    
    # Driver Code
    
    # 0 means unassigned cells
x_pos = []
y_pos = []
for temp in range(k*k):
    x_pos.append(temp)
    y_pos.append(temp)

random.shuffle(x_pos)
random.shuffle(y_pos)

def checkZero(arr1):
    for temp in arr1:
        for temp1 in temp:
            if temp1 == 0:
                return True
    return False

run = True
while run:
    i = random.choice(x_pos)
    j = random.choice(y_pos)
    value = random.choice(arr)
    grid[i][j] = value
    if not (solveSudoku(grid, 0, 0)):
        grid[i][j] = 0
       
    if not(checkZero(grid)):
        # printing(grid)
        run = False
        break
            

ans = []

b = []
for i in range(1,k*k+1):
    for j in range(1, k*k+1):
        for temp in range(1, k*k+1):
            b.append(int(str(i)+str(j)+str(temp)))
        ans.append(b)
        b = []

for i in range(1,k*k+1):
    for j in range(1,k*k+1):
        for p in range(1,k**2+1):
            for q in range(p+1, k**2+1):
                b = []
                b.append(-1*int(str(i)+str(j)+str(p)))
                b.append(-1*int(str(i)+str(j)+str(q)))
                ans.append(b)

    #block clause
b = []
for temp in range(1,k*k+1):
    for i in range(1, k*k+1,k):
        for j in range(1,k*k+1,k):
            x = i
            while(x<i+k):
                y = j
                while(y<j+k):
                        
                    b.append(int(str(x)+str(y)+str(temp)))
                    y += 1
                x +=1
            ans.append(b)
            b=[]

    #clauses for showing all rows contain all value form 1-9

b = []
for i in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for j in range(1,k*k+1):
            b.append(int(str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]




    #clauses for showing all columns contain all value form 1-9
b = []
for j in range(1,k*k+1):
    for temp in range(1,k*k+1):
        for i in range(1,k*k+1):
            b.append(int(str(i)+str(j)+str(temp)))
        ans.append(b)
        b=[]

    #original values

for i,temp in enumerate(grid):
    for j,temp1 in enumerate(temp):
        if int(temp1) != 0:
            ans.append([-1*int(str(i+1)+str(j+1)+(str(temp1)))])

g = Glucose3()

for temp in ans:
    g.add_clause(temp)

g.solve()
answer =  g.get_model()

grid_1 = []
for temp in range(k*k):
    temp1 = []
    for temp2 in range(k*k):
        temp1.append(0)
    grid_1.append(temp1)

for temp in answer:
    if temp > 0:
        count = 1
        val=''
        temp = str(temp)
        while(count < len(temp)-1):
            val += temp[-1*count]
            count += 1
        grid_1[int(temp[0])-1][int(temp[1])-1] = int(val)
        

with open('original.csv','w') as csvfile:
    csvwriter =   csv.writer(csvfile)     
    csvwriter.writerows(grid)
    csvwriter.writerows(grid_1)
    # Second part algo
def make_grid(arr,grid):
        
    arr1 = []
    delta_temp = 0
    for temp in arr:
        arr1.append(temp)
        delta_temp += 1
        if delta_temp%(k*k) == 0:
            grid.append(arr1)
            arr1 = []


def check_number_solution(i,j,grid,count):
    if (i==N):
        i = 0
        j += 1
        if (j==N):
            return 1+count
    
    if grid[i][j] != 0:
        return check_number_solution(i+1,j,grid,count)
    val = 1
    while(val <= N and count < 2):
        if isSafe(grid,i,j,val):
            grid[i][j] = val
            count = check_number_solution(i+1,j,grid,count)
        val += 1
    grid[i][j] = 0
    return count
    

arr2 = []
arr_2 = []

for temp in grid:
    for temp1 in temp:
        arr2.append(temp1)

for temp in grid_1:
    for temp1 in temp:
        arr_2.append(temp1)

for i in range(k**(4)):
    a_temp = arr2[i]
    b_temp = arr_2[i]
    arr2[i] = 0
    arr_2[i] = 0
    grid = []
    grid_1 = []
    make_grid(arr2,grid)
    make_grid(arr_2,grid_1)
    sol_num = check_number_solution(0,0,grid,0)
    sol_num_1 = check_number_solution(0,0,grid_1,0)
    if not(sol_num_1 == 1):
        arr_2[i] = b_temp
    if not(sol_num == 1):
        arr2[i] = a_temp


with open('test.csv','w') as csvfile:
    csvwriter =   csv.writer(csvfile)          
    csvwriter.writerows(grid)
    csvwriter.writerows(grid_1)
    
print('first grid \n')
printing(grid)
print('\nsecond grid \n')
printing(grid_1)