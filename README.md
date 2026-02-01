# SpoonOS ReAct Agent Demo

基于 [SpoonOS](https://github.com/XSpoonAi/spoon-core) 框架构建的 **ReAct Agent**，实现加密货币价格分析功能。

## 项目简介

本项目使用 SpoonOS SDK 实现了一个 ReAct (Reasoning + Acting) 模式的智能代理，能够：

- 查询加密货币实时价格
- 获取 24 小时市场统计数据
- 分析 K 线数据
- 通过自然语言交互回答用户问题

## 演示视频

https://github.com/user-attachments/assets/demo.mov

> 注：上传到 GitHub 后，视频链接会自动更新。

## 技术栈

| 组件 | 说明 |
|------|------|
| [SpoonOS SDK](https://github.com/XSpoonAi/spoon-core) | AI Agent 开发框架 |
| [SpoonToolkits](https://github.com/XSpoonAi/spoon-toolkit) | 加密货币数据工具集 |
| ReAct Pattern | 推理 + 行动的 Agent 架构模式 |
| DeepSeek / OpenAI / Gemini | 可配置的 LLM 后端 |

## 项目结构

```
spoonos-react-agent-demo/
├── main.py              # 程序入口
├── src/
│   ├── __init__.py
│   └── agent.py         # ReAct Agent 核心实现
├── assets/
│   └── demo.mov         # 演示视频
├── requirements.txt     # Python 依赖
├── .env.example         # 环境变量模板
├── .gitignore           # Git 忽略配置
└── README.md            # 项目说明
```

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/spoonos-react-agent-demo.git
cd spoonos-react-agent-demo
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置你的 LLM API Key：

```bash
# 推荐使用 DeepSeek（性价比高）
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=your_api_key_here

# 或使用其他 Provider
# LLM_PROVIDER=openai
# OPENAI_API_KEY=your_api_key_here

# LLM_PROVIDER=gemini
# GEMINI_API_KEY=your_api_key_here
```

### 5. 运行 Agent

**交互模式：**

```bash
python main.py
```

**单次查询模式：**

```bash
python main.py "What is the current price of Bitcoin?"
```

## 使用示例

```
============================================================
  SpoonOS ReAct Agent - Crypto Price Analyzer
============================================================

Type your questions about cryptocurrency prices.
Type 'quit' or 'exit' to stop.

[You]: What is the current price of ETH?

[Agent]: Thinking...

[Agent]: The current price of Ethereum (ETH) is $3,245.67 USD.
         24h Change: +2.35%
         24h Volume: $12.5B

[You]: Show me BTC 24h statistics

[Agent]: Thinking...

[Agent]: Bitcoin (BTC) 24-Hour Statistics:
         - Current Price: $42,150.00
         - 24h High: $42,890.00
         - 24h Low: $41,200.00
         - 24h Volume: $28.3B
         - Price Change: +1.8%
```

## Agent 架构

```
┌─────────────────────────────────────────────────────────┐
│                    ReAct Agent                          │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   Reason    │───▶│    Act      │───▶│   Observe   │ │
│  │  (思考)     │    │  (执行)     │    │   (观察)    │ │
│  └─────────────┘    └─────────────┘    └─────────────┘ │
│         │                  │                  │        │
│         └──────────────────┴──────────────────┘        │
│                           │                            │
├───────────────────────────┼────────────────────────────┤
│                     Tools (工具)                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │GetTokenPrice │ │ Get24hStats  │ │ GetKlineData │   │
│  └──────────────┘ └──────────────┘ └──────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## 支持的 LLM Provider

| Provider | 说明 | 获取 API Key |
|----------|------|-------------|
| DeepSeek | 推荐，性价比高 | [platform.deepseek.com](https://platform.deepseek.com/) |
| OpenAI | GPT-4 系列 | [platform.openai.com](https://platform.openai.com/) |
| Anthropic | Claude 系列 | [console.anthropic.com](https://console.anthropic.com/) |
| Gemini | Google AI | [aistudio.google.com](https://aistudio.google.com/) |
| Ollama | 本地运行，免费 | [ollama.com](https://ollama.com/) |

## 工具说明

| 工具 | 功能 |
|------|------|
| `GetTokenPriceTool` | 获取加密货币实时价格 |
| `Get24hStatsTool` | 获取 24 小时市场统计数据 |
| `GetKlineDataTool` | 获取 K 线图数据 |

## 相关资源

- [SpoonOS 官方文档](https://xspoonai.github.io/)
- [SpoonOS Core](https://github.com/XSpoonAi/spoon-core)
- [SpoonOS Toolkit](https://github.com/XSpoonAi/spoon-toolkit)
- [SpoonOS Starter](https://github.com/XSpoonAi/spoon-starter)
- [Awesome Skills](https://github.com/XSpoonAi/spoon-awesome-skill)

## License

MIT License
