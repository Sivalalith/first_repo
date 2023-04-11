class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index_list = []
        if (needle not in haystack):
            return -1
        for h_index in range(0,len(haystack)):
            count = 0
            for n_index in range(0,len(needle)):
                if needle[n_index] != haystack[n_index+h_index]:
                    index_list = []
                    break
                index_list.append(n_index+h_index)
                count += 1
            if count == len(needle):
                return index_list[0]
                break
        if count == len(needle):
            return index_list[0]
