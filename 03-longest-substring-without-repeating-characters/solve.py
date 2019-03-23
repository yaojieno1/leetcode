class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a = [-1] * 256   # 记录每个字符的索引
        record = 0       # 当前的不重复长度
        maxrec = 0       # 最长的记录
        ptr    = -1      # 当前记录的起始位置
        for i in range(len(s)):
            x = ord(s[i])
            if (a[x] == -1 or a[x] < ptr):
                # 没有重复，递增即可
                record += 1
                a[x] = i
                if (ptr == -1):
                    ptr = i
                continue
            else:
                # 出现重复，需要更新记录
                if (maxrec < record):
                    maxrec = record
                ptr    = a[x] + 1
                record = i - ptr + 1
                a[x]   = i
        # 遍历结束，刷新记录
        if (maxrec < record):
            maxrec = record
        return maxrec
                
