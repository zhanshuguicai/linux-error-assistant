# -*- coding: utf-8 -*-

"""
这个文件用于保存常见 Linux 命令的解释规则。
第一版先覆盖最常用、最适合初学者的一批命令。
"""

COMMAND_RULES = [
    {
        "keywords": ["ls", "ls -l", "ls -a"],
        "command_name": "ls",
        "purpose": "查看目录中的文件和文件夹。",
        "common_options": [
            "-l：以详细列表形式显示",
            "-a：显示隐藏文件",
            "-h：配合 -l 使用时，文件大小更容易读"
        ],
        "usage_scenarios": [
            "查看当前目录内容",
            "检查某个文件是否存在",
            "观察文件权限"
        ],
        "tips": [
            "初学者最常用的是 ls 和 ls -l",
            "如果想看隐藏文件，可以用 ls -a"
        ]
    },
    {
        "keywords": ["cd"],
        "command_name": "cd",
        "purpose": "切换当前工作目录。",
        "common_options": [
            "cd ..：回到上一级目录",
            "cd ~：回到用户主目录",
            "cd /：进入根目录"
        ],
        "usage_scenarios": [
            "进入某个目录",
            "返回上一级目录",
            "切换到家目录"
        ],
        "tips": [
            "如果路径里有空格，注意加引号",
            "可以先用 pwd 查看当前所在位置"
        ]
    },
    {
        "keywords": ["pwd"],
        "command_name": "pwd",
        "purpose": "显示当前工作目录的完整路径。",
        "common_options": [],
        "usage_scenarios": [
            "确认自己当前在哪个目录",
            "排查路径相关问题"
        ],
        "tips": [
            "在初学 Linux 时，pwd 很常用",
            "配合 cd 一起使用最方便"
        ]
    },
    {
        "keywords": ["cat"],
        "command_name": "cat",
        "purpose": "查看文件内容，也可以用于拼接文件内容。",
        "common_options": [
            "cat 文件名：直接输出文件内容",
            "cat -n 文件名：显示行号"
        ],
        "usage_scenarios": [
            "快速查看短文件内容",
            "查看配置文件"
        ],
        "tips": [
            "如果文件很长，建议用 less 或 tail 更合适"
        ]
    },
    {
        "keywords": ["tail", "tail -n", "tail -f"],
        "command_name": "tail",
        "purpose": "查看文件末尾内容。",
        "common_options": [
            "tail -n 100 文件名：查看最后 100 行",
            "tail -f 文件名：持续跟踪日志输出"
        ],
        "usage_scenarios": [
            "查看日志最后几行",
            "实时观察日志变化"
        ],
        "tips": [
            "排障时 tail -n 和 tail -f 非常常用"
        ]
    },
    {
        "keywords": ["grep"],
        "command_name": "grep",
        "purpose": "在文本中搜索关键词。",
        "common_options": [
            "grep 关键词 文件名",
            "grep -i：忽略大小写",
            "grep -n：显示行号"
        ],
        "usage_scenarios": [
            "在日志中搜索 error",
            "查找配置项",
            "过滤命令输出结果"
        ],
        "tips": [
            "grep 是 Linux 排障时最常用的命令之一"
        ]
    },
    {
        "keywords": ["ps"],
        "command_name": "ps",
        "purpose": "查看当前系统中的进程信息。",
        "common_options": [
            "ps aux：查看所有进程",
            "ps -ef：另一种常见格式"
        ],
        "usage_scenarios": [
            "查看某个程序是否在运行",
            "排查后台服务进程"
        ],
        "tips": [
            "常与 grep 一起使用，例如 ps aux | grep python"
        ]
    },
    {
        "keywords": ["ss", "ss -ltnp"],
        "command_name": "ss",
        "purpose": "查看网络连接和端口监听情况。",
        "common_options": [
            "ss -ltnp：查看 TCP 监听端口和对应进程"
        ],
        "usage_scenarios": [
            "查看某个端口是否被监听",
            "排查服务是否成功启动"
        ],
        "tips": [
            "排查端口占用时非常有用"
        ]
    },
    {
        "keywords": ["chmod"],
        "command_name": "chmod",
        "purpose": "修改文件或目录权限。",
        "common_options": [
            "chmod +x 文件名：增加执行权限",
            "chmod 755 文件名：设置常见权限组合"
        ],
        "usage_scenarios": [
            "让脚本变得可执行",
            "修改文件访问权限"
        ],
        "tips": [
            "不理解数字权限时，可以先用 chmod +x 这种简单写法"
        ]
    },
    {
        "keywords": ["curl"],
        "command_name": "curl",
        "purpose": "向 URL 发送请求，常用于测试接口和网页连通性。",
        "common_options": [
            "curl 地址：发送 GET 请求",
            "curl -I 地址：只查看响应头",
            "curl -X POST 地址：发送 POST 请求"
        ],
        "usage_scenarios": [
            "测试接口是否可访问",
            "检查网页响应",
            "调试 HTTP 请求"
        ],
        "tips": [
            "Linux 排障和 API 调试时非常常用"
        ]
    }
]