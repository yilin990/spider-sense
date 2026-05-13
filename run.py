#!/usr/bin/env python3
"""
SpiderSense 蜘蛛感应 - 入口文件
"""
import sys
import os

# 添加scripts目录到路径
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from scripts.core import spider_sense
from scripts.executor import execute_with_feedback

def main():
    if len(sys.argv) < 2:
        print("🕸️ SpiderSense 蜘蛛感应")
        print("=" * 40)
        print("用法: python3 run.py <任务>")
        print("示例: python3 run.py 截图")
        return
    
    task = " ".join(sys.argv[1:])
    
    # 丝线检测
    result = spider_sense(task)
    
    if result["status"] != "triggered":
        print(f"🕸️ 无丝线震动: {task}")
        return
    
    decision = result.get("decision", {})
    node_name = decision.get("node_name", "?")
    action = decision.get("action", "?")
    
    print(f"📥 {task}")
    print(f"🧵 丝线: {list(result.get('threads', {}).keys())}")
    print(f"📍 节点: {list(result.get('nodes', {}).keys())}")
    print(f"🎯 决策: {action} -> {node_name}")
    
    # 执行
    if decision.get("action") in ["execute", "execute_primary"]:
        exec_result = execute_with_feedback(decision)
        if exec_result.get("status") == "success":
            print(f"✅ 执行成功")
        else:
            print(f"📤 执行状态: {exec_result.get('status')}")

if __name__ == "__main__":
    main()