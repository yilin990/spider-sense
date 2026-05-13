#!/usr/bin/env python3
"""
蜘蛛感应 Executor - 执行脚本 V1.1
"""
import subprocess
import json
import os

# 脚本路径映射
SCRIPTS = {
    "browser-automation": "~/.openclaw/workspace/tools/playwright_screenshot.py",
    "tavily": "~/.openclaw/workspace/skills/tavily-web-search-for-openclaw/scripts/tavily_search.py",
    "xhs-poster": "~/.openclaw/workspace/tools/xhs_poster_v3.py",
    "signet": "~/.bun/bin/signet",
    "merchant-platform": "~/.openclaw/workspace/tools/merchant_platform.py",
    "printer": "~/.openclaw/workspace/tools/printer_hp4512.py",
    "vision": "~/.openclaw/workspace/tools/vision_understand.py",
    "voice": "~/.openclaw/workspace/tools/voice_skill_v1.py",
    "feishu": "~/.bun/bin/lark-cli",
    "analysis": "~/.openclaw/workspace/tools/tavily_search.py",
}

def execute_node(node_name, args=None):
    """根据节点名称执行对应脚本"""
    if node_name not in SCRIPTS:
        return {"status": "unknown_node", "node": node_name}
    
    script_path = os.path.expanduser(SCRIPTS[node_name])
    
    # 构建命令
    if node_name == "signet":
        cmd = f"{script_path} remember"
        if args:
            cmd += f" {args}"
    elif node_name in ["tavily", "analysis"]:
        cmd = f"python3 {script_path}"
        if args:
            cmd += f" --query '{args}'"
    elif node_name == "xhs-poster":
        cmd = f"python3 {script_path} --dry-run"
    elif node_name == "printer":
        cmd = f"python3 {script_path} --status"
    else:
        cmd = f"python3 {script_path}"
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return {
            "status": "executed",
            "node": node_name,
            "output": result.stdout[:300] if result.stdout else "执行完成",
            "error": result.stderr[:100] if result.stderr else ""
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "node": node_name}
    except Exception as e:
        return {"status": "error", "node": node_name, "error": str(e)[:100]}

def execute_with_feedback(decision, args=None):
    """执行并返回反馈"""
    if decision.get("action") not in ["execute", "execute_primary"]:
        return {"status": "skipped", "reason": decision.get("reason", "no_action")}
    
    node = decision.get("target_node") or decision.get("primary_node")
    result = execute_node(node, args)
    
    if result["status"] == "executed":
        return {
            "status": "success",
            "node": node,
            "output": result["output"][:200] if result.get("output") else "完成"
        }
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        node = sys.argv[1]
        args = sys.argv[2] if len(sys.argv) > 2 else None
        result = execute_node(node, args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("用法: python3 executor.py <node_name> [args]")
        print(f"可用节点: {list(SCRIPTS.keys())}")