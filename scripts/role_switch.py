#!/usr/bin/env python3
"""
蜘蛛感应 - 角色代入
临时代入角色，自动切换丝线和节点联动逻辑
"""

# ============================================
# 角色定义
# ============================================
ROLES = {
    "打印助手": {
        "name": "打印助手",
        "description": "远程打印服务专家",
        "active_threads": ["打印", "文件", "纸质", "服务器"],
        "active_nodes": ["printer", "browser-automation"],
        "deactivated_nodes": ["xhs-poster", "creative"],
        "default_action": "printer"
    },
    "民宿管家": {
        "name": "民宿管家",
        "description": "民宿运营管理专家",
        "active_threads": ["客人", "房源", "入住", "退房", "预订"],
        "active_nodes": ["merchant-platform", "signet", "tavily"],
        "deactivated_nodes": ["creative", "xhs-poster"],
        "default_action": "merchant-platform"
    },
    "小红书运营": {
        "name": "小红书运营",
        "description": "小红书内容运营专家",
        "active_threads": ["笔记", "发布", "数据", "粉丝", "内容"],
        "active_nodes": ["creative", "xhs-poster", "tavily"],
        "deactivated_nodes": ["printer"],
        "default_action": "xhs-poster"
    },
    "商户拓展": {
        "name": "商户拓展",
        "description": "商户拓展和入驻服务",
        "active_threads": ["商户", "入驻", "商家", "签约"],
        "active_nodes": ["merchant-platform", "signet", "browser-automation"],
        "deactivated_nodes": ["creative", "xhs-poster"],
        "default_action": "merchant-platform"
    },
    "默认": {
        "name": "默认",
        "description": "通用模式",
        "active_threads": [],
        "active_nodes": ["signet", "tavily", "browser-automation", "xhs-poster", "merchant-platform"],
        "deactivated_nodes": [],
        "default_action": None
    }
}

# ============================================
# 当前角色
# ============================================
current_role = "默认"

def switch_role(role_name):
    """切换角色"""
    global current_role
    if role_name in ROLES:
        current_role = role_name
        return {
            "status": "switched",
            "role": ROLES[role_name]["name"],
            "description": ROLES[role_name]["description"],
            "active_nodes": ROLES[role_name]["active_nodes"]
        }
    return {"status": "error", "message": f"未知角色: {role_name}"}

def get_current_role():
    """获取当前角色"""
    return ROLES.get(current_role, ROLES["默认"])

def get_active_nodes():
    """获取当前激活的节点"""
    role = get_current_role()
    return role.get("active_nodes", [])

def get_deactivated_nodes():
    """获取当前停用的节点"""
    role = get_current_role()
    return role.get("deactivated_nodes", [])

def is_node_active(node):
    """检查节点是否激活"""
    if current_role == "默认":
        return True
    active_nodes = get_active_nodes()
    return node in active_nodes

def role_based_filter(nodes):
    """基于角色的节点过滤"""
    if current_role == "默认":
        return nodes
    
    active = get_active_nodes()
    deactivated = get_deactivated_nodes()
    
    filtered = {}
    for node, info in nodes.items():
        if node in deactivated:
            continue
        if node in active or current_role == "默认":
            filtered[node] = info
    
    return filtered

def format_role_status():
    """格式化角色状态"""
    role = get_current_role()
    return {
        "current_role": role["name"],
        "description": role["description"],
        "active_nodes": role["active_nodes"],
        "active_threads": role["active_threads"]
    }

# ============================================
# 测试
# ============================================
if __name__ == "__main__":
    print("🕸️ 角色代入测试\n")
    
    # 测试切换角色
    test_roles = ["打印助手", "民宿管家", "小红书运营", "商户拓展"]
    
    for role_name in test_roles:
        result = switch_role(role_name)
        print(f"✅ 切换到: {result['role']}")
        print(f"   描述: {result['description']}")
        print(f"   激活节点: {result['active_nodes']}")
        print()
    
    # 切换回默认
    switch_role("默认")
    print("🔄 切换回: 默认模式")