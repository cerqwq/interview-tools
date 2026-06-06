# 💼 Interview Tools

AI面试工具，支持面试题生成、模拟面试、简历优化。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- ❓ 面试题生成
- 🎭 模拟面试
- 📄 简历优化
- ✉️ 求职信生成
- 💰 薪资分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from interview_tools import create_tools

tools = create_tools()

# 生成面试题
questions = tools.generate_questions("Python开发", "字节跳动", 10)

# 模拟面试
simulation = tools.simulate_interview("Python开发", questions)

# 简历优化
optimization = tools.optimize_resume(resume_text, "Python开发")

# 求职信
cover_letter = tools.generate_cover_letter(resume, "Python开发", "字节跳动")

# 薪资分析
salary = tools.analyze_salary("Python开发", "北京", "3年")
```

## 📁 项目结构

```
interview-tools/
├── tools.py       # 面试工具核心
└── README.md
```

## 📄 许可证

MIT License
