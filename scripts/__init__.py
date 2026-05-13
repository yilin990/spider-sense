#!/usr/bin/env python3
"""
蜘蛛感应 Heartbeat触发器
每分钟自动检测丝线震动
"""
import time
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from core import spider_sense
from executor import execute_with_feedback

def check(task, verbose=True):
    """检测并执行"""
    result = spider_sense(task)
    
    if result["status"] != "triggered":
        if verbose:
            print("🕸️ 无丝线震动")
        return None
    
    decision = result.get("decision", {})
    if decision.get("action") not in ["execute", "execute_primary"]:
        if verbose:
            print(f"🕸️ 决策: {decision.get('action')}")
        return result
    
    exec_result = execute_with_feedback(decision)
    
    if verbose:
        print(f"🕸️ {decision.get('node_name')} -> {exec_result.get('status')}")
    
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        check(task)
    else:
        print("用法: python3 heartbeat_trigger.py <任务>")