# -*- coding: utf-8
'''
凑硬币
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
输入描述
第一行两个个整数N和K， N代表需要达到的总金额，K代表有K种面额的硬币，用空格分隔。

第二行为K个整数a1,a2...ak，用空格分隔，代表K种面额的硬币。
输出描述
一个整数代表用所给面额的硬币组合成N的方案数。
'''


class Al:

    def trace(self, total, nums):
        '''
        方法一暴力遍历(回溯 - 深度遍历)
        @total: 总和
        @nums：不同面额的硬币
        @return： 组合方案
        '''

        def traceback(msum):
            if msum == total:
                self.count += 1
                return self.count

            for num in nums:
                if msum + num > total:
                    break
                traceback(msum + num)
        self.count = 0
        traceback(0)
        return self.count

    def dp(self, total, nums):
        '''
        方法二动态规划
        dp[i] = sum(dp[i-num])
        区分先后顺序的排列组合
        '''

        dp = [0 for _ in range(total + 1)]
        for num in nums:
            dp[num] = 1

        for i in range(total + 1):
            for num in nums:
                j = i - num
                if j < 0: break

                dp[i] += dp[j]

        return dp[-1]


    def minc(self, total, coins):
        '''
        使用最少硬币个数凑成目标数
        @total：目标
        @coins：硬币不同面值, 一般会是一个常量[1, 3, 5]
        @return: 最少需要的硬币数目
        '''
        dp = ['inf' for _ in range(total + 1)]
        dp[0] = 0

        for index in range(total + 1):
            for coin in coins:
                if index - coin < 0: break

                dp[index] = min(dp[index], dp[index - coin] + 1)

        return dp[-1]


al = Al()
ret = al.dp(5, [1, 2, 5])
print('Total:{}\tCoins={}\t排列组合数目:{}'.format(5, [1, 2, 5], ret))
c = al.minc(11, [1, 3, 5])
print('Total:{}\tCoins={}\t最少使用硬币数:{}'.format(11, [1, 3, 5], c))

