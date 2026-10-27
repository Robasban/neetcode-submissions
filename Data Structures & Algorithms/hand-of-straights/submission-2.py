class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()

        track = dict()

        for num in hand:
            track[num] = track.get(num, 0) + 1
        
        i = 0
        while i < len(hand):

            amt = track[hand[i]]

            for j in range(1, groupSize):
                if track.get(hand[i] + j, 0) < amt:
                    return False

            for j in range(0, groupSize):
                track[hand[i] + j] -= amt

            while i < len(hand) and track[hand[i]] == 0:
                i += 1

        return True