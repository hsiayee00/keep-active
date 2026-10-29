#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
keep-active —— 保持 GitHub 账号活跃度的轻量小脚本

用法：
    1) 把本仓库 clone 到本地
    2) 想起来就运行一次：  python keep_active.py
    3) 提交并推送：         git add activity.log && git commit -m "活跃一下" && git push

脚本会在 activity.log 追加一行记录（日期 + 一句随机鼓励语），
你把它提交并推送，GitHub 贡献图上就多一个绿点。
不需要每天跑，想起来戳一下就行。
"""
import datetime
import random

CHEERS = [
    "今天也要开心写代码呀",
    "绿点 +1，保持手感",
    "摸鱼也要摸得有仪式感",
    "代码即记录，记录即存在",
    "小步快跑，持续活跃",
]


def main():
    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {random.choice(CHEERS)}\n"
    with open("activity.log", "a", encoding="utf-8") as f:
        f.write(line)
    print("已记录一次活跃：")
    print("  " + line.strip())
    print("提示：git add activity.log && git commit -m \"活跃一下\" && git push")


if __name__ == "__main__":
    main()
