# -*- coding: utf-8 -*-

"""
这里放 AI 接口配置。
如果你已经有可用的 API，可以直接填进去。
如果还没有，也可以先留空，程序会提示 AI 分析不可用。
"""

# 这里示例用 OpenAI 兼容接口的写法
API_BASE_URL = "https://api.openai.com/v1/chat/completions"

# 把这里换成你自己的 key
API_KEY = ""

# 模型名称按你实际可用的来改
MODEL_NAME = "gpt-4o-mini"

# 请求超时（秒）
REQUEST_TIMEOUT = 20