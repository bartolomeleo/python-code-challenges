from collections import deque

queue=deque(['test 1', 'test 2', 'test3'])


queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves

squares = []
for x in range(10):
    squares.append(x**2)


listXNotY=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

listXNotYNotZ=[(x,y,z) for x in [1,2, 3] for y in [3,2,6] for z in [(x+1, y-1)] if x!=y]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

zipMatrix=list(zip(*matrix))

print('zipMatrix: ', zipMatrix)
print('queue: ', queue)
print('listXNotY: ', listXNotY)
print('listXNotYNotZ: ', listXNotYNotZ)
