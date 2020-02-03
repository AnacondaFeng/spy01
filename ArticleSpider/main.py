from scrapy.cmdline import execute  # 用于pycharm启动spider脚本

import sys
import os

# print(__file__) #当前文件所在文件路径

# print(os.path.dirname(os.path.abspath(__file__)))

"""
执行脚本
"""
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "jobbole"])
