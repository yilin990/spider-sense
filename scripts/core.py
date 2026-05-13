#!/usr/bin/env python3
"""
蜘蛛感应 Core - 丝线震动检测 + 节点联动 V1.1
优化版：增加更多丝线和节点
"""
import subprocess
import json
import os

# ============================================
# 丝线定义（场景触发词）- V1.1
# ============================================
THREADS = {
    # 核心丝线（5个）
    "截图": ["截图", "截屏", "capture", "screenshot", "screen"],
    "搜索": ["搜索", "查资料", "查找", "search", "调研"],
    "发帖": ["发帖", "发布", "小红书", "post", "发文章"],
    "记忆": ["记住", "记忆", "存储", "memory", "存一下"],
    "商户": ["商户", "入驻", "表单", "merchant", "商家入驻"],
    # 新增丝线（6个）
    "打印": ["打印", "纸质", "print", "列印"],
    "看图": ["看图", "分析图", "图片理解", "vision", "图片", "图片分析"],
    "语音": ["语音", "说话", "发语音", "voice"],
    "飞书": ["飞书", "通知", "消息", "feishu"],
    "代码": ["代码", "脚本", "写代码", "code"],
    "文件": ["文件", "读取", "写入", "file"],
}

# ============================================
# 节点定义（能力网络）- V1.1
# ============================================
NODES = {
    "browser-automation": {
        "name": "浏览器自动化",
        "capabilities": ["screenshot", "fill_form", "auto_click", "scrape"],
        "trigger_keywords": ["截图", "浏览器", "填表", "自动化"],
    },
    "tavily": {
        "name": "搜索系统",
        "capabilities": ["web_search", "research", "analyze"],
        "trigger_keywords": ["搜索", "查", "查找", "search", "调研"],
    },
    "xhs-poster": {
        "name": "小红书发布",
        "capabilities": ["post_xhs", "publish", "content"],
        "trigger_keywords": ["发帖", "发布", "小红书", "post", "发文章"],
    },
    "signet": {
        "name": "记忆系统",
        "capabilities": ["remember", "recall", "search_memory"],
        "trigger_keywords": ["记住", "记忆", "存储", "memory", "存一下"],
    },
    "merchant-platform": {
        "name": "商户管理",
        "capabilities": ["merchant_apply", "merchant_preview", "qrcode"],
        "trigger_keywords": ["商户", "入驻", "表单", "商家入驻", "merchant"],
    },
    "printer": {
        "name": "打印系统",
        "capabilities": ["print", "format", "pdf"],
        "trigger_keywords": ["打印", "纸质", "print", "列印"],
    },
    "vision": {
        "name": "视觉理解",
        "capabilities": ["image_understand", "analyze", "describe"],
        "trigger_keywords": ["看图", "分析图", "图片理解", "vision"],
    },
    "voice": {
        "name": "语音合成",
        "capabilities": ["tts", "speak", "voice"],
        "trigger_keywords": ["语音", "说话", "发语音", "voice"],
    },
    "feishu": {
        "name": "飞书通知",
        "capabilities": ["notify", "message", "send"],
        "trigger_keywords": ["飞书", "通知", "消息", "feishu"],
    },
    "analysis": {
        "name": "数据分析",
        "capabilities": ["analyze", "report", "insight"],
        "trigger_keywords": ["分析", "报告", "analytics"],
    },
}

# ============================================
# 中枢判断逻辑
# ============================================
def central_brain(triggered_threads, activated_nodes):
    """中枢快速判断"""
    if not triggered_threads or not activated_nodes:
        return {"action": "wait", "reason": "no_trigger"}
    
    if len(triggered_threads) == 1 and len(activated_nodes) == 1:
        thread = list(triggered_threads.keys())[0]
        node = list(activated_nodes.keys())[0]
        node_info = NODES.get(node, {})
        return {
            "action": "execute",
            "target_node": node,
            "node_name": node_info.get("name", node),
            "thread": thread,
        }
    
    if len(activated_nodes) > 1:
        primary_node = list(activated_nodes.keys())[0]
        node_info = NODES.get(primary_node, {})
        return {
            "action": "execute_primary",
            "primary_node": primary_node,
            "primary_node_name": node_info.get("name", primary_node),
            "all_nodes": [NODES.get(n, {}).get("name", n) for n in activated_nodes.keys()],
            "reason": f"multi_node_{len(activated_nodes)}_detected"
        }
    
    return {"action": "wait", "reason": "unclear_trigger"}

# ============================================
# 丝线震动检测
# ============================================
def detect_thread_vibration(text):
    """检测丝线震动"""
    triggered = {}
    text_lower = text.lower()
    for thread_name, keywords in THREADS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                triggered[thread_name] = keyword
                break
    return triggered

# ============================================
# 节点激活检测
# ============================================
def activate_nodes(triggered_threads):
    """根据触发的丝线，激活对应节点"""
    activated = {}
    for thread in triggered_threads.keys():
        for node_name, node_info in NODES.items():
            if thread in node_info.get("trigger_keywords", []):
                activated[node_name] = node_info
    return activated

# ============================================
# 蜘蛛感应主函数
# ============================================
def spider_sense(text):
    """蜘蛛感应主函数"""
    triggered_threads = detect_thread_vibration(text)
    if not triggered_threads:
        return {"status": "no_trigger", "message": "无丝线震动"}
    
    activated_nodes = activate_nodes(triggered_threads)
    if not activated_nodes:
        return {"status": "no_node", "threads": triggered_threads}
    
    decision = central_brain(triggered_threads, activated_nodes)
    
    return {
        "status": "triggered",
        "threads": triggered_threads,
        "nodes": activated_nodes,
        "decision": decision
    }

# ============================================
# 测试
# ============================================
if __name__ == "__main__":
    test_cases = [
        "清禾帮我截图",
        "帮我搜索一下最新的AI技术",
        "我要发布小红书",
        "帮我记住这个重要信息",
        "商户入驻怎么做",
        "帮我打印这个文件",
        "看看这张图片",
        "发个飞书通知",
        "分析一下数据",
    ]
    
    print("🕸️ 蜘蛛感应 Core V1.1 测试")
    print(f"丝线数量: {len(THREADS)}")
    print(f"节点数量: {len(NODES)}")
    print("-" * 50)
    
    for text in test_cases:
        result = spider_sense(text)
        decision = result.get("decision", {})
        node_name = decision.get("node_name", "?")
        action = decision.get("action", "?")
        print(f"\n📥 {text}")
        print(f"   🧵 丝线: {list(result.get('threads', {}).keys())}")
        print(f"   📍 节点: {list(result.get('nodes', {}).keys())}")
        print(f"   🎯 决策: {action} -> {node_name}")