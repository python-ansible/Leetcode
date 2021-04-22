# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
# 输入n，打印出s的所有可能的值出现的概率。
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
# 示例 1:
# 输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
# 示例2:
# 输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 1 2 3 4 5 6
# 2-1 3-2 4-3 5-4 6-5 7-6 8-5 9-4 10-3 11-2 12-1
# 3-1 4-3 5-6 6-10 7-15 8-21 9-25 10-27 11-27 12-25 13-21 14-15 15-10 16-6 17-3 18-1
# 3 111
# 4 112
# 5 113 122
# 6 114 123 222
# 7 115 124 133 223
# 8 116 125 134 224 233
# 9 126 135 144 225 234 333
# 10 136 145 226 235 244 334
# 11 146 155 236 245 335 344
# 12 156 246 255 336 345 444
# 13 256 346 355 445 661
# 14 266 356 446 554
# 15 366 456 555
# 16 466 556
# 17 566
# 18 666

# 还是dp
# 已知 i-1 枚骰子的结果
# tmp = [0] * (5 * i + 1)
# for j in range(len(dp)):
# 一个dp[j] 影响了下一轮的六个结果 dp[j+1~6]
#     for k in range(6):
#         tmp[j+k] += dp[j] / 6
from typing import List
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1/6] * 6
        for i in range(2, n+1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k] += dp[j]/6
            dp = tmp
        print(dp)
        print(sum(dp))
        return dp

if __name__ == '__main__':
    s = Solution()
    s.dicesProbability(3)

