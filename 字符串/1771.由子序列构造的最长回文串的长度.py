# 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串：
# 从 word1 中选出某个 非空 子序列 subsequence1 。
# 从 word2 中选出某个 非空 子序列 subsequence2 。
# 连接两个子序列 subsequence1 + subsequence2 ，得到字符串。
# 返回可按上述方法构造的最长 回文串 的 长度 。
# 如果无法构造回文串，返回 0 。
# 字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。
# 回文串 是正着读和反着读结果一致的字符串。
# 示例 1：
# 输入：word1 = "cacb", word2 = "cbba"
# 输出：5
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。
# 示例 2：
# 输入：word1 = "ab", word2 = "ab"
# 输出：3
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。
# 示例 3：
# 输入：word1 = "aa", word2 = "bb"
# 输出：0
# 解释：无法按题面所述方法构造回文串，所以返回 0 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximize-palindrome-length-from-subsequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 516 s = word1+word2
# dp[i][j] 表示由i开始j结束的最长回文串的长度
# if s[i] = s[j] dp[i][j] = dp[i+1][j-1] +2
# else dp[i][j] = max(dp[i+1][j], dp[i][j-1]
# i < len(word1) and j >= len(word1)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        res = 0
        for j in range(1,n):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < len(word1) and j >= len(word1):
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return res

if __name__ == '__main__':
    a = Solution()
    word1, word2 = 'aabbcc', 'aaccbb'
    word1, word2 = 'aa', 'bb'
    word1, word2 = "febeeb", "d"
    print(a.longestPalindrome(word1, word2))