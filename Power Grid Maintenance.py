from typing import List
from collections import defaultdict
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        # Build connected components
        for u, v in connections:
            union(u, v)

        # Min-heap for each component
        comp_heap = defaultdict(list)

        for node in range(1, c + 1):
            root = find(node)
            heapq.heappush(comp_heap[root], node)

        # All stations initially online
        online = [True] * (c + 1)

        ans = []

        for t, x in queries:

            # Query type 1
            if t == 1:

                if online[x]:
                    ans.append(x)
                else:
                    root = find(x)
                    heap = comp_heap[root]

                    # Remove offline stations lazily
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        ans.append(heap[0])
                    else:
                        ans.append(-1)

            # Query type 2
            else:
                online[x] = False

        return ans
