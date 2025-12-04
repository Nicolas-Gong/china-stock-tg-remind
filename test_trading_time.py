#!/usr/bin/env python3
"""
测试交易时间功能
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from stock_bot import is_trading_time

def test_trading_time():
    """测试交易时间判断"""
    print("测试交易时间判断功能...")

    # 测试A股
    print("1. 测试A股代码:")
    print(f"   600519 (茅台): {is_trading_time('600519')}")
    print(f"   000001 (平安): {is_trading_time('000001')}")
    print(f"   300308 (中际旭创): {is_trading_time('300308')}")

    # 测试港股
    print("2. 测试港股代码:")
    print(f"   00001 (长和): {is_trading_time('00001')}")
    print(f"   00002 (中电控股): {is_trading_time('00002')}")

    # 测试美股
    print("3. 测试美股代码:")
    print(f"   AAPL (苹果): {is_trading_time('AAPL')}")
    print(f"   TSLA (特斯拉): {is_trading_time('TSLA')}")

    # 测试未知代码
    print("4. 测试未知代码:")
    print(f"   UNKNOWN: {is_trading_time('UNKNOWN')}")

    print("\n注意：测试结果取决于当前时间和工作日")
    print("周六日所有市场都返回False")

if __name__ == "__main__":
    test_trading_time()
