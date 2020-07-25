class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 长度
        length = 0
        # 字符字典
        adict = {}
        # 计数
        flag = 0
        # 上一个相同的字符下标
        last_same_char = 0
        # 遍历从1开始
        for i in range(1, len(s) + 1):
            # 如果有之前出现过的字符，字典能找到
            if adict.get(s[i - 1], 0):
                # 只有大于有效
                # 当前循环
                this_same_char = adict[s[i - 1]]
                # 当当前的上一个相同值大于上一个相同值，即在上一个值的右边时有效
                # ‘ds（last_same_char）sd（this_same_char）此时d虽然有相同但标记是无效的
                if this_same_char > last_same_char:
                    # 相同标志后移
                    flag = i - this_same_char
                    last_same_char = this_same_char
                    # 大于后的距离判定，字符字串的长度
                    if length < i - this_same_char:
                        length = i - this_same_char
                # 小于则当前匹配无效，进行计数
                else:
                    flag += 1
                    if flag > length:
                        length = flag
            else:
                # 计数
                flag += 1
                if flag > length:
                    length = flag
            # 无论是否出现过，进行替换或赋初值
            adict[s[i - 1]] = i
            # print(length)

        return length


fff = Solution()

cc = "tmmzuxt"
print(fff.lengthOfLongestSubstring(cc))
