class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canLadder(str1, str2):
            countDiff = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    countDiff += 1
            return countDiff == 1

        wordList.append(beginWord)

        edges = {word : [] for word in wordList}
        for f in wordList:
            for s in wordList:
                if f == s:
                    continue
                if canLadder(f, s):
                    edges[f].append(s)

        visited = set()
        def bfs(q):
            depth = 0
            while q:
                qLen = len(q)
                depth += 1
                for _ in range(qLen):
                    word = q.popleft()
                    if word in visited:
                        continue
                    visited.add(word)
                    if word == endWord:
                        return depth
                    else:
                        q.extend(edges[word])

            return 0

        q = collections.deque()
        q.append(beginWord)
        return bfs(q)
