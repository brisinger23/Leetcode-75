class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [False]*len(rooms)
        q = deque()
        q.append(0)

        while q:
            curr = q.popleft()
            visit[curr] = True
            
            for v in rooms[curr]:
                if not visit[v]:
                    q.append(v)

        return all(visit)
