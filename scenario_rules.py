# -*- coding: utf-8 -*-

"""
这个文件用于保存“场景 -> 推荐命令”的规则。
目标是帮助 Linux 初学者在不知道具体命令时，
也能先按场景找到合适的命令和操作顺序。
"""

SCENARIO_RULES = [
    {
        "keywords": ["查看当前目录", "当前目录", "我在哪个目录", "现在在哪"],
        "scenario": "查看当前所在目录",
        "recommended_commands": [
            "pwd"
        ],
        "explanation": "这个场景最适合先用 pwd，因为很多路径问题的根源就是你并不在自己以为的目录里。",
        "step_by_step": [
            {
                "step": "先查看当前目录",
                "command": "pwd",
                "purpose": "确认你当前所在路径。",
                "look_for": "输出应该是一条完整路径。",
                "next_action": "如果路径不对，再使用 cd 切换。"
            }
        ]
    },
    {
        "keywords": ["查看目录内容", "列出文件", "看文件列表", "目录里有什么"],
        "scenario": "查看目录中的文件和文件夹",
        "recommended_commands": [
            "ls",
            "ls -l",
            "ls -a"
        ],
        "explanation": "这个场景通常先从 ls 开始，再根据需要看详细信息或隐藏文件。",
        "step_by_step": [
            {
                "step": "先看目录里有什么",
                "command": "ls",
                "purpose": "快速查看当前目录下的文件和子目录。",
                "look_for": "看目标文件名是否出现。",
                "next_action": "如果想看更详细信息，再用 ls -l。"
            },
            {
                "step": "看详细信息",
                "command": "ls -l",
                "purpose": "查看权限、大小、修改时间等信息。",
                "look_for": "重点看权限位和文件名。",
                "next_action": "如果怀疑有隐藏文件，再用 ls -a。"
            },
            {
                "step": "查看隐藏文件",
                "command": "ls -a",
                "purpose": "确认目录中是否存在隐藏文件。",
                "look_for": "看是否有以 . 开头的文件。",
                "next_action": "如果需要同时看详细信息，可用 ls -la。"
            }
        ]
    },
    {
        "keywords": ["查看日志最后100行", "看日志最后几行", "查看日志", "看日志"],
        "scenario": "查看日志文件末尾内容",
        "recommended_commands": [
            "tail -n 100 文件名",
            "tail -f 文件名"
        ],
        "explanation": "排障时通常先看日志最后几十或几百行，因为最近的报错往往最重要。",
        "step_by_step": [
            {
                "step": "先查看日志最后 100 行",
                "command": "tail -n 100 日志文件名",
                "purpose": "快速抓住最近发生的问题。",
                "look_for": "重点看 error、exception、traceback 等关键词。",
                "next_action": "如果信息不够，再扩大行数范围。"
            },
            {
                "step": "如果想实时观察日志变化",
                "command": "tail -f 日志文件名",
                "purpose": "持续跟踪新日志输出。",
                "look_for": "看是否持续出现报错、重连、重启等信息。",
                "next_action": "停止时按 Ctrl + C。"
            }
        ]
    },
    {
        "keywords": ["搜索错误", "搜索日志关键词", "查找error", "查日志里的关键词"],
        "scenario": "在日志或文件中搜索关键词",
        "recommended_commands": [
            "grep error 文件名",
            "grep -i error 文件名",
            "grep -n error 文件名"
        ],
        "explanation": "当日志很长时，不要硬读，先 grep 关键词通常更高效。",
        "step_by_step": [
            {
                "step": "先搜索最明显的关键词",
                "command": "grep error 文件名",
                "purpose": "先快速筛出错误相关行。",
                "look_for": "看输出中是否有包含 error 的内容。",
                "next_action": "如果没有，再尝试忽略大小写。"
            },
            {
                "step": "忽略大小写搜索",
                "command": "grep -i error 文件名",
                "purpose": "避免因为大小写差异漏掉内容。",
                "look_for": "看是否出现更多匹配结果。",
                "next_action": "如果想定位具体位置，再加 -n。"
            },
            {
                "step": "显示行号",
                "command": "grep -n error 文件名",
                "purpose": "方便后续定位上下文。",
                "look_for": "重点看前面的行号。",
                "next_action": "可再结合 cat -n 或 tail 查看上下文。"
            }
        ]
    },
    {
        "keywords": ["查看进程", "看程序是否运行", "检查进程", "看服务有没有启动"],
        "scenario": "查看当前系统中的进程",
        "recommended_commands": [
            "ps aux",
            "ps aux | grep 进程名"
        ],
        "explanation": "如果你怀疑程序根本没启动，先看进程比先看端口更直接。",
        "step_by_step": [
            {
                "step": "先确认系统里有哪些进程",
                "command": "ps aux",
                "purpose": "查看系统当前运行的进程。",
                "look_for": "输出会很多，重点是确认命令可用。",
                "next_action": "如果你关心某个具体服务，再配合 grep。"
            },
            {
                "step": "搜索目标进程",
                "command": "ps aux | grep 服务名",
                "purpose": "快速确认目标服务是否在运行。",
                "look_for": "如果只看到 grep 本身，说明目标进程可能不存在。",
                "next_action": "如果进程不存在，再去查启动日志或启动命令。"
            }
        ]
    },
    {
        "keywords": ["查看端口占用", "检查端口监听", "看端口", "端口是不是开着"],
        "scenario": "查看端口监听情况",
        "recommended_commands": [
            "ss -ltnp",
            "ss -ltnp | grep 端口号",
            "lsof -i :端口号"
        ],
        "explanation": "如果问题和端口有关，先看监听状态，再看具体进程。",
        "step_by_step": [
            {
                "step": "先看当前所有监听端口",
                "command": "ss -ltnp",
                "purpose": "确认系统哪些端口已经被监听。",
                "look_for": "重点看 Local Address:Port 和 Process。",
                "next_action": "如果端口太多，再过滤目标端口。"
            },
            {
                "step": "过滤具体端口",
                "command": "ss -ltnp | grep 8000",
                "purpose": "只看目标端口是否存在。",
                "look_for": "如果有输出，说明端口在监听；如果没有，说明没监听。",
                "next_action": "如需知道是谁占用，再用 lsof。"
            },
            {
                "step": "查看具体是哪个进程占用端口",
                "command": "lsof -i :8000",
                "purpose": "确认 PID 和进程名。",
                "look_for": "重点看 COMMAND 和 PID。",
                "next_action": "根据 PID 决定是否结束进程或改端口。"
            }
        ]
    },
    {
        "keywords": ["测试网址", "测试接口", "测试连通性", "接口能不能访问"],
        "scenario": "测试 URL 或接口是否可访问",
        "recommended_commands": [
            "curl -I 地址",
            "curl 地址"
        ],
        "explanation": "测试接口时，建议先看响应头和状态码，再看完整内容。",
        "step_by_step": [
            {
                "step": "先看状态码和响应头",
                "command": "curl -I 地址",
                "purpose": "快速判断目标是否有响应、状态码是否正常。",
                "look_for": "重点看 HTTP 状态码，例如 200、404、500。",
                "next_action": "如果状态码异常，再看完整返回内容。"
            },
            {
                "step": "再看完整响应内容",
                "command": "curl 地址",
                "purpose": "查看服务器真实返回了什么。",
                "look_for": "看是否返回 HTML、JSON，或者直接报错。",
                "next_action": "根据返回内容继续判断问题在客户端还是服务端。"
            }
        ]
    },
    {
        "keywords": ["给脚本加执行权限", "脚本不能运行", "权限不够", "文件不能执行"],
        "scenario": "给脚本或文件增加执行权限",
        "recommended_commands": [
            "ls -l 文件名",
            "chmod +x 文件名"
        ],
        "explanation": "遇到脚本无法执行时，先确认权限，再决定是否加执行位。",
        "step_by_step": [
            {
                "step": "先看当前权限",
                "command": "ls -l 文件名",
                "purpose": "确认文件是否已经有执行权限。",
                "look_for": "重点看最前面的权限位里有没有 x。",
                "next_action": "如果没有 x，再用 chmod +x。"
            },
            {
                "step": "增加执行权限",
                "command": "chmod +x 文件名",
                "purpose": "让该文件具备执行权限。",
                "look_for": "命令本身通常没输出。",
                "next_action": "执行后再次运行 ls -l 确认。"
            },
            {
                "step": "再次确认权限是否已修改",
                "command": "ls -l 文件名",
                "purpose": "确保权限位里已经出现 x。",
                "look_for": "如果有 x，说明可执行权限已经加上。",
                "next_action": "现在可以重新尝试运行脚本。"
            }
        ]
    },
    {
        "keywords": ["查看当前用户", "我是谁", "当前用户是谁"],
        "scenario": "确认当前执行命令的用户身份",
        "recommended_commands": [
            "whoami"
        ],
        "explanation": "很多权限问题都和当前用户身份直接相关。",
        "step_by_step": [
            {
                "step": "查看当前用户",
                "command": "whoami",
                "purpose": "确认你当前是以哪个用户身份执行命令。",
                "look_for": "输出通常是一个用户名。",
                "next_action": "如果不是预期用户，再结合 sudo 或权限配置继续判断。"
            }
        ]
    }
]