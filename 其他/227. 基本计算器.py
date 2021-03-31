# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
# 示例 1：
# 输入：s = "3+2*2"
# 输出：7
#
# 示例 2：
# 输入：s = " 3/2 "
# 输出：1
#
# 示例 3：
# 输入：s = " 3+5 / 2 "
# 输出：5
#
# 1 <= s.length <= 3 * 105
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
# 题目数据保证答案是一个 32-bit 整数

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s += '$'
        opr = '+'
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            else:
                if c == ' ': continue
                elif opr == '+':
                    stack.append(num)
                elif opr == '-':
                    stack.append(-num)
                elif opr == '*':
                    stack.append(stack.pop()*num)
                elif opr == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(abs(top)/abs(num)))
                    else:
                        stack.append(top//num)
                opr = c
                num = 0
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate('3+2*2'))
    print(s.calculate(' 3/2 '))
    print(s.calculate(' 3 + 5 / 2 '))