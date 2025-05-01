class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        queue = deque()
        visited = set()
        queue.append(("0000",0))
        visited.add("0000")
        number_choice = {
            "0":["9","1"],
            "1":["2","0"],
            "2":["3","1"],
            "3":["4","2"],
            "4":["5","3"],
            "5":["6","4"],
            "6":["7","5"],
            "7":["8","6"],
            "8":["9","7"],
            "9":["0","8"],
        }
        while(queue):
            (cur,depth) = queue.popleft()
            print(cur,depth)
            if cur == target:
                return depth
            if cur in dead:
                continue
            for i in range(4):
                for choice in number_choice[cur[i]]:
                    print(choice)
                    new = cur[:i] + choice + cur[i+1:]
                    if new not in visited:
                        queue.append((new,depth+1))
                        visited.add(new)
        return -1


        