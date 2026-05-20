# 🕸️ SpiderSense — 像蜘蛛一样思考的AI Agent

> 多节点分布式思考系统，让AI能够感知丝线震动、联动节点、调动能力

[![GitHub stars](https://img.shields.io/github/stars/yilin990/spider-sense)](https://github.com/yilin990/spider-sense)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-green)](https://openclaw.ai/)

## 核心理念

SpiderSense（蜘蛛感应）让AI像蜘蛛一样思考：

- **🕸️ 连接**：多节点多能力网络
- **📳 感应**：场景触发，全局联动  
- **🧠 思考**：多节点分布式思考
- **⚡ 中枢**：快速判断，调动技能网

## 功能特性

- 11个丝线震动检测
- 10个能力节点联动
- 中枢快速决策
- 多节点思考（调研部/记忆部/执行部/创意部/审批部）
- 角色代入（打印助手/民宿管家/小红书运营/商户拓展）

## 丝线（触发词）

| 丝线 | 触发关键词 |
|------|-----------|
| 截图 | 截图、截屏、capture、screenshot |
| 搜索 | 搜索、查资料、查找、search |
| 发帖 | 发帖、发布、小红书、post |
| 记忆 | 记住、记忆、存储、memory |
| 商户 | 商户、入驻、表单、merchant |
| 打印 | 打印、纸质、print |
| 看图 | 看图、分析图、图片理解、vision |
| 语音 | 语音、说话、发语音、voice |
| 飞书 | 飞书、通知、消息、feishu |
| 代码 | 代码、脚本、写代码、code |
| 文件 | 文件、读取、写入、file |

## 节点（能力）

| 节点 | 能力 |
|------|------|
| browser-automation | 浏览器自动化、截图、填表 |
| tavily | 搜索系统、网络搜索 |
| xhs-poster | 小红书发布 |
| signet | 记忆系统 |
| merchant-platform | 商户管理 |
| printer | 打印系统 |
| vision | 视觉理解 |
| voice | 语音合成 |

## 安装

```bash
# 复制到 OpenClaw skills 目录
cp -r spider-sense ~/.openclaw/workspace/skills/

# 运行
python3 run.py
```

## 工作原理

```
触发词(丝线震动)
    ↓
中枢感知 → 判断类型
    ↓
调度对应节点 → 执行能力
    ↓
结果汇总 → 返回输出
```

## 应用场景

- **📸 截图助手** — 看到屏幕内容，理解并分析
- **🔍 调研员** — 自动搜索信息，整理报告
- **📝 发帖运营** — 批量发布小红书/抖音内容
- **🏪 商户管理** — 表单填写、数据同步
- **🖨️ 打印管家** — 自动排版、一键打印

## 未来演进

- ControlNet 姿态控制 → 更精确的视觉理解
- 多Agent协作 → 节点可以自主协同
- 商业化落地 → 商户图书馆场景

## License

MIT — Created by [赵奕霖 & 清禾](https://github.com/yilin990)

---

*像蜘蛛一样思考，像清禾一样行动* 🕸️🌿
