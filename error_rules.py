# -*- coding: utf-8 -*-

"""
这个文件保存第一版规则库。
用关键词匹配的方式处理几类常见 Linux / 网络报错。(好蠢啊)
"""

ERROR_RULES = [
    {
        "keywords": ["command not found"],
        "error_type": "命令不存在",
        "explanation": "系统找不到你输入的命令，说明当前命令无法被识别。",
        "possible_causes": [
            "命令拼写错误",
            "相关软件没有安装",
            "命令不在 PATH 环境变量中"
        ],
        "suggestions": [
            "检查命令拼写是否正确",
            "确认相关软件是否已经安装",
            "使用 which 或 whereis 检查命令位置",
            "检查 PATH 环境变量配置"
        ]
    },
    {
        "keywords": ["permission denied"],
        "error_type": "权限不足",
        "explanation": "当前操作没有足够权限执行，系统拒绝了这次请求。",
        "possible_causes": [
            "当前用户权限不足",
            "文件没有执行权限",
            "目标文件或目录的属主、权限设置不正确"
        ],
        "suggestions": [
            "检查当前用户是否有访问权限",
            "使用 ls -l 查看文件权限",
            "必要时使用 chmod 修改权限",
            "必要时使用 sudo 提升权限"
        ]
    },
    {
        "keywords": ["connection refused"],
        "error_type": "连接被拒绝",
        "explanation": "客户端尝试连接目标地址和端口，但对方没有接受连接请求。",
        "possible_causes": [
            "目标服务没有启动",
            "目标端口没有监听",
            "地址或端口写错"
        ],
        "suggestions": [
            "确认服务是否正在运行",
            "使用 ss -ltnp 或 netstat 检查端口监听情况",
            "检查 IP 地址和端口号是否正确",
            "先用 curl 测试目标地址"
        ]
    },
    {
        "keywords": ["no such file or directory"],
        "error_type": "文件或目录不存在",
        "explanation": "程序访问的文件或目录不存在，或者当前路径不正确。",
        "possible_causes": [
            "路径写错",
            "文件已经被删除或移动",
            "当前工作目录不正确"
        ],
        "suggestions": [
            "检查文件路径是否正确",
            "使用 ls 或 dir 查看目标文件是否存在",
            "确认当前工作目录是否正确",
            "尽量使用绝对路径进行测试"
        ]
    },
    {
        "keywords": ["read timed out", "timeout"],
        "error_type": "请求超时",
        "explanation": "请求在规定时间内没有收到完整响应，因此被系统中断。",
        "possible_causes": [
            "网络连接较慢",
            "目标服务响应过慢",
            "设置的 timeout 时间过短"
        ],
        "suggestions": [
            "检查当前网络连接情况",
            "适当增大 timeout 参数",
            "确认目标服务是否正常运行",
            "使用 curl 测试目标地址的响应情况"
        ]
    }
]