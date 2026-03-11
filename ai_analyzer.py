# -*- coding: utf-8 -*-

import requests
from config import API_BASE_URL, API_KEY, MODEL_NAME, REQUEST_TIMEOUT


def build_prompt(error_text):
    """
    构造提示词，要求模型按固定格式输出，
    避免回答太发散。
    """
    return f"""你现在是一个帮助大学生学习 Linux 排障的助手。

请分析下面这段报错信息，并严格按照以下格式输出：

错误类型：
问题解释：
可能原因：
1.
2.
3.
排查建议：
1.
2.
3.

要求：
1. 输出内容使用中文
2. 表达尽量清楚、具体、适合初学者
3. 不要输出多余寒暄
4. 如果信息不足，可以明确指出需要补充什么

报错信息：
{error_text}
"""


def analyze_with_ai(error_text):
    """
    调用 AI 接口分析报错。
    如果没有配置 API_KEY，就返回失败提示。
    """
    if not API_KEY.strip():
        return {
            "success": False,
            "content": "AI 分析不可用：当前还没有在 config.py 中配置 API_KEY。"
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": build_prompt(error_text)
            }
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(
            API_BASE_URL,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        data = response.json()
        content = data["choices"][0]["message"]["content"]

        return {
            "success": True,
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "content": f"AI 分析失败：{str(e)}"
        }