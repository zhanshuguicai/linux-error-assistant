# -*- coding: utf-8 -*-

import requests
from config import API_BASE_URL, API_KEY, MODEL_NAME, REQUEST_TIMEOUT


def build_prompt(user_text):
    """
    构造提示词，要求模型输出更适合 Linux 新手的
    手把手排障和命令学习结果。
    """
    return f"""你现在是一个专门帮助 Linux 初学者排障和学习命令的助手。

用户输入的内容可能是：
1. 一段报错信息
2. 一个 Linux 命令
3. 一个使用场景描述

请你使用中文回答，并且严格按照下面格式输出：

识别类型：
问题解释：

可能原因：
1.
2.
3.

手把手操作步骤：
步骤1：
命令：
说明：
你应该观察：
下一步判断：

步骤2：
命令：
说明：
你应该观察：
下一步判断：

步骤3：
命令：
说明：
你应该观察：
下一步判断：

如果需要更多步骤，可以继续写步骤4、步骤5，不要强行只写3步。

要求：
1. 回答对象是 Linux 初学者
2. 不要只说“检查一下”，而要尽量给出可以直接复制到终端执行的命令
3. 每一步都必须说明“为什么执行这条命令”
4. 每一步都必须说明“执行后应该重点看什么输出”
5. 每一步都尽量说明“根据结果下一步怎么办”
6. 如果输入是一个命令，就重点解释“命令用途、常见参数、适用场景、如何一步步使用”
7. 如果输入是一个场景，就重点给出“推荐命令 + 先后顺序 + 观察点”
8. 不要输出寒暄，不要输出多余客套话
9. 如果信息不足，也先给出最合理的第一步命令，而不是只说“信息不足”
10.步骤和原因可能多或少于3，根据情况自行调整，上述只是限定输出格式

用户输入：
{user_text}
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