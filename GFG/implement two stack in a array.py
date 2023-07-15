#User function Template for python3
class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.t1 = -1
        self.t2 = n

    def push1(self, x):
        if self.t2 - self.t1 > 1:
            self.t1 += 1
            self.arr[self.t1] = x

    def push2(self, x):
        if self.t2 - self.t1 > 1:
            self.t2 -= 1
            self.arr[self.t2] = x

    def pop1(self):
        if self.t1 >= 0:
            x = self.arr[self.t1]
            self.t1 -= 1
            return x
        return -1

    def pop2(self):
        if self.t2 < self.size:
            x = self.arr[self.t2]
            self.t2 += 1
            return x
        return -1

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

# } Driver Code Ends