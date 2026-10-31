import heapq

def ucs(tree, root, goal):
    queue = [(0, root)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        print(node)

        if node == goal:
            print("Total Cost:", cost)
            return

        for i, w in tree[node]:
            heapq.heappush(queue, (cost + w, i))

if __name__ == '__main__':
    tree = {
        1: [(2, 2), (3, 5)],
        2: [(4, 3), (5, 1)],
        3: [(6, 2)],
        4: [],
        5: [],
        6: []
    }

    ucs(tree, 1, 5)
