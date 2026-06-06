"""
Interview Tools - AI面试工具
支持面试题生成、模拟面试、简历优化
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class InterviewTools:
    """
    AI面试工具
    支持：题目、模拟、简历
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_questions(self, position: str, company: str, count: int = 10) -> List[Dict]:
        """生成面试题"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为{company}的{position}岗位生成{count}道面试题：

请返回JSON格式：
[
    {{"question": "问题", "type": "技术/行为/系统设计", "difficulty": "easy/medium/hard", "answer_points": ["要点1", "要点2"]}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"questions": content}]

    def simulate_interview(self, position: str, questions: List[str]) -> Dict:
        """模拟面试"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        questions_text = "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions[:5]))

        prompt = f"""请为{position}岗位进行模拟面试：

问题：
{questions_text}

请返回JSON格式：
{{
    "feedback": [
        {{"question": "问题", "sample_answer": "参考答案", "evaluation_criteria": "评估标准", "tips": "回答技巧"}}
    ],
    "overall_tips": ["总体建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"simulation": content}

    def optimize_resume(self, resume: str, position: str) -> Dict:
        """优化简历"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{position}岗位优化以下简历：

{resume[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "strengths": ["优势"],
    "weaknesses": ["不足"],
    "improvements": [
        {{"section": "部分", "original": "原文", "improved": "改进后", "reason": "原因"}}
    ],
    "keywords": ["应该包含的关键词"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_cover_letter(self, resume: str, position: str, company: str) -> str:
        """生成求职信"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{company}的{position}岗位生成求职信：

简历摘要：
{resume[:1000]}

要求：
1. 突出相关经验
2. 展示热情
3. 专业且个性化"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def analyze_salary(self, position: str, location: str, experience: str) -> Dict:
        """分析薪资"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析{location}的{position}岗位薪资（{experience}经验）：

请返回JSON格式：
{{
    "range": {{"min": "最低", "max": "最高", "average": "平均"}},
    "factors": ["影响因素"],
    "negotiation_tips": ["谈判技巧"],
    "benefits_to_consider": ["应考虑的福利"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"salary": content}


def create_tools(**kwargs) -> InterviewTools:
    """创建面试工具"""
    return InterviewTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Interview Tools")
    print()

    # 测试
    questions = tools.generate_questions("Python开发", "字节跳动", 5)
    print(json.dumps(questions, ensure_ascii=False, indent=2))
