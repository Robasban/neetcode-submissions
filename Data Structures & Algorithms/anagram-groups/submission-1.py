class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numberList = {}

        for str in strs:
            number = [0] * 26
            for char in str:
                number[ord(char) - 97] += 1
            key = tuple(number)
            numberList[key] = [str] + numberList.get(key, [])

        return list(numberList.values())

