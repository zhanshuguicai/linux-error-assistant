# -*- coding: utf-8 -*-

"""
这个文件用于保存“场景 -> 推荐命令”的规则。
适合初学者在不知道具体命令时使用。
"""

SCENARIO_RULES = [
    {
        "keywords": ["查看当前目录", "当前目录", "我在哪个目录"],
        "scenario": "查看当前所在目录",
        "recommended_commands": [
            "pwd"
        ],
        "explanation": "pwd 可以显示当前工作目录的完整路径。"
    },
    {
        "keywords": ["查看目录内容", "列出文件", "看文件列表"],
        "scenario": "查看目录中的文件和文件夹",
        "recommended_commands": [
            "ls",
            "ls -l",
            "ls -a"
        ],
        "explanation": "ls 用来列出目录内容，ls -l 可以看详细信息，ls -a 可以看隐藏文件。"
    },
    {
        "keywords": ["查看日志最后100行", "看日志最后几行", "查看日志"],
        "scenario": "查看日志文件末尾内容",
        "recommended_commands": [
            "tail -n 100 文件名",
            "tail -f 文件名"
        ],
        "explanation": "tail -n 可以查看最后若干行，tail -f 可以持续跟踪日志更新。"
    },
    {
        "keywords": ["搜索错误", "搜索日志关键词", "查找error"],
        "scenario": "在日志或文件中搜索关键词",
        "recommended_commands": [
            "grep error 文件名",
            "grep -i error 文件名"
        ],
        "explanation": "grep 用于在文本中搜索关键词，非常适合日志排查。"
    },
    {
        "keywords": ["查看进程", "看程序是否运行", "检查进程"],
        "scenario": "查看当前系统中的进程",
        "recommended_commands": [
            "ps aux",
            "ps aux | grep 进程名"
        ],
        "explanation": "ps 用于查看进程，结合 grep 可以查找目标程序是否在运行。"
    },
    {
        "keywords": ["查看端口占用", "检查端口监听", "看端口"],
        "scenario": "查看端口监听情况",
        "recommended_commands": [
            "ss -ltnp",
            "lsof -i :端口号"
        ],
        "explanation": "ss -ltnp 可以看监听端口和进程信息，lsof 也常用于查看端口占用。"
    },
    {
        "keywords": ["测试网址", "测试接口", "测试连通性"],
        "scenario": "测试 URL 或接口是否可访问",
        "recommended_commands": [
            "curl 地址",
            "curl -I 地址"
        ],
        "explanation": "curl 可以快速测试网页或接口是否可访问。"
    },
    {
        "keywords": ["给脚本加执行权限", "脚本不能运行", "权限不够"],
        "scenario": "给脚本或文件增加执行权限",
        "recommended_commands": [
            "chmod +x 文件名",
            "ls -l 文件名"
        ],
        "explanation": "chmod +x 可以增加执行权限，ls -l 可以查看当前权限。"
    }
]