#User function Template for python3

class Solution:
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.SolveSudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True
    
    def is_valid(self, board, row, col, num):
    # Check if 'num' is not in the same row, column, or subgrid
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j], end= " ")
        # Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends