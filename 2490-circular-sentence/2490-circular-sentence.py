# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        stack = []
        for word in sentence.split(" "):
            if stack and stack[-1] == word[0]:
                stack.pop()
            else:
                stack.append(word[0])
            stack.append(word[-1])
        return stack[0] == stack[1] and len(stack) == 2


sentence = "JuFZhkkASkRxIeiCOdGeELCMYHmuiqqLQqtjSxxHqnKrQOIEMxzkbapCCTvwaBlLXcGBVjqvppTJCttpbgbEcPEiSAcfcapXEUCdoQJvaUPCHRqVPuOghLqHWbFYgcMvxIufQTjpzmSMCAusXISLbJ aXOmiAAoYDyqqXwAe VnWA WZg uKlnD L UHRD"
print(Solution().isCircularSentence(sentence))
sentence = "leetcode exercises sound delightful"
print(Solution().isCircularSentence(sentence))
