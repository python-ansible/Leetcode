# 列表的 异或和（XOR sum）指对所有元素进行按位 XOR 运算的结果。
# 如果列表中仅有一个元素，那么其 异或和 就等于该元素。
# 例如，[1,2,3,4] 的 异或和 等于 1 XOR 2 XOR 3 XOR 4 = 4 ，而 [3] 的 异或和 等于 3 。
# 给你两个下标 从 0 开始 计数的数组 arr1 和 arr2 ，两数组均由非负整数组成。
# 根据每个 (i, j) 数对，构造一个由 arr1[i] AND arr2[j]（按位 AND 运算）结果组成的列表。
# 其中 0 <= i < arr1.length 且 0 <= j < arr2.length 。
# 返回上述列表的 异或和 。
# 示例 1：
# 输入：arr1 = [1,2,3], arr2 = [6,5]
# 输出：0
# 解释：列表 = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1] ，
# 异或和 = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0 。
# 示例 2：
# 输入：arr1 = [12], arr2 = [4]
# 输出：4
# 解释：列表 = [12 AND 4] = [4] ，异或和 = 4 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-xor-sum-of-all-pairs-bitwise-and
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        from itertools import product
        s = product(arr1,arr2)
        s2 = [x&y for x,y in s]
        res = 0
        for i in s2:
            res ^= i
        return res

# 满足交换律和结合律
from typing import List

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        s = 0
        for num in arr2:
            s ^= num
        ans = 0
        for num in arr1:
            ans ^= (num & s)
        return ans

if __name__ == '__main__':
    s = Solution()
    arr1, arr2 = [1,2,3], [6,5]
    print(s.getXORSum(arr1, arr2))
    arr1, arr2 = [12], [4]
    print(s.getXORSum(arr1, arr2))
