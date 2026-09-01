class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numberList = {}

        for str in strs:
            number = [0] * 26
            for char in str:
                number[ord(char) - 97] += 1
            numberList[tuple(number)] = [str] + numberList.get(tuple(number), [])

        return list(numberList.values())

