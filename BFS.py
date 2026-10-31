#implementing BFS
import collections
import queue
from asyncio import graph
def bfs(tree,root):
    visited = set()
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in tree[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)
if __name__ == '__main__': #dictionary
    tree = {1:[2,3],2:[4,5],3:[6],4:[],5:[],6:[]}
    bfs(tree,1)


