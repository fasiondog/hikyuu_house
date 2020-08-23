from hikyuu import SG_Single, AMA

# 部件作者
author = "fasiondog"

# 版本
version = '20200824'

# 帮助信息
doc = """
AMA信号指示器
使用《精明交易者》 [BOOK1]_ 中给出的曲线拐点算法判断曲线趋势，公式见下::

    filter = percentage * STDEV((AMA-AMA[1], N)

    Buy  When AMA - AMA[1] > filter
    or Buy When AMA - AMA[2] > filter
    or Buy When AMA - AMA[3] > filter 
"""

part = SG_Single(AMA())

if __name__ == '__main__':
    print(sg)