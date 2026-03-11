# -*- coding: utf-8 -*-

"""
这个文件用于保存常见 Linux 命令的解释规则。
目标不是只告诉用户“命令是什么”，而是尽量告诉用户：
1. 这个命令什么时候用
2. 常见参数是什么意思
3. 初学者第一次该怎么一步一步使用
4. 执行后重点看什么输出
"""

COMMAND_RULES = [
    {
        "keywords": ["pwd"],
        "command_name": "pwd",
        "purpose": "显示当前工作目录的完整路径。",
        "common_options": [],
        "usage_scenarios": [
            "不知道自己现在在哪个目录",
            "排查相对路径错误",
            "切换目录后确认位置"
        ],
        "tips": [
            "初学 Linux 时，pwd 是最基础也最常用的命令之一",
            "当你遇到路径相关问题时，先敲 pwd 往往很有帮助"
        ],
        "beginner_steps": [
            {
                "step": "先直接查看当前目录",
                "command": "pwd",
                "purpose": "确认你当前所在的位置。",
                "look_for": "输出应该是一条完整路径，例如 /home/user/project。",
                "next_action": "如果这个路径不是你预期的位置，先用 cd 切换目录。"
            }
        ]
    },
    {
        "keywords": ["cd", "cd ..", "cd ~", "cd /"],
        "command_name": "cd",
        "purpose": "切换当前工作目录。",
        "common_options": [
            "cd ..：进入上一级目录",
            "cd ~：进入当前用户主目录",
            "cd /：进入根目录"
        ],
        "usage_scenarios": [
            "进入某个目录",
            "返回上一级目录",
            "回到主目录"
        ],
        "tips": [
            "很多“文件找不到”的问题，本质上都是因为当前目录不对",
            "切换目录后，最好再用 pwd 确认一下"
        ],
        "beginner_steps": [
            {
                "step": "先确认自己当前在哪个目录",
                "command": "pwd",
                "purpose": "避免盲目切换目录。",
                "look_for": "看当前路径是否符合预期。",
                "next_action": "如果不对，再决定要切换到哪里。"
            },
            {
                "step": "进入目标目录",
                "command": "cd 目录名",
                "purpose": "切换到你想进入的目录。",
                "look_for": "cd 本身通常没有输出，重点是不要报错。",
                "next_action": "切换后马上再执行 pwd 或 ls -l。"
            },
            {
                "step": "确认是否进入成功",
                "command": "pwd",
                "purpose": "验证目录切换是否成功。",
                "look_for": "输出路径应该已经变成目标目录。",
                "next_action": "如果还不对，检查目录名或路径是否写错。"
            }
        ]
    },
    {
        "keywords": ["ls", "ls -l", "ls -a", "ls -lh"],
        "command_name": "ls",
        "purpose": "查看目录中的文件和文件夹。",
        "common_options": [
            "-l：详细列表形式显示",
            "-a：显示隐藏文件",
            "-h：配合 -l 时让文件大小更易读"
        ],
        "usage_scenarios": [
            "查看当前目录下有什么文件",
            "确认文件是否存在",
            "观察文件权限和大小"
        ],
        "tips": [
            "初学者最常用的是 ls、ls -l、ls -a",
            "排障时建议优先用 ls -l，因为它会显示更多信息"
        ],
        "beginner_steps": [
            {
                "step": "先看当前目录里有什么",
                "command": "ls",
                "purpose": "快速查看当前目录下的文件和子目录。",
                "look_for": "确认目标文件名是否出现。",
                "next_action": "如果需要更多信息，再用 ls -l。"
            },
            {
                "step": "查看详细信息",
                "command": "ls -l",
                "purpose": "查看文件权限、属主、大小和修改时间。",
                "look_for": "重点看最前面的权限位、文件名、文件大小。",
                "next_action": "如果看不到目标文件，再考虑是不是目录不对。"
            },
            {
                "step": "如果怀疑有隐藏文件，显示隐藏文件",
                "command": "ls -a",
                "purpose": "查看以 . 开头的隐藏文件。",
                "look_for": "例如 .gitignore、.env、.config 等文件。",
                "next_action": "如果需要同时看详细信息，可用 ls -la。"
            }
        ]
    },
    {
        "keywords": ["cat", "cat -n"],
        "command_name": "cat",
        "purpose": "查看文件内容，也可用于简单拼接文本。",
        "common_options": [
            "cat 文件名：输出文件内容",
            "cat -n 文件名：显示行号"
        ],
        "usage_scenarios": [
            "快速查看短文件内容",
            "查看配置文件",
            "确认文件里到底写了什么"
        ],
        "tips": [
            "如果文件很长，cat 会一下刷满屏幕，这时更适合用 less 或 tail"
        ],
        "beginner_steps": [
            {
                "step": "先直接查看短文件内容",
                "command": "cat 文件名",
                "purpose": "快速确认文件内容。",
                "look_for": "看输出内容是否符合预期。",
                "next_action": "如果文件太长，改用 less 或 tail。"
            },
            {
                "step": "如果想定位具体行，可以带行号查看",
                "command": "cat -n 文件名",
                "purpose": "在阅读配置或报错文件时更容易定位。",
                "look_for": "重点看行号和对应内容。",
                "next_action": "后续如果需要搜索关键词，可以结合 grep。"
            }
        ]
    },
    {
        "keywords": ["tail", "tail -n", "tail -f"],
        "command_name": "tail",
        "purpose": "查看文件末尾内容，尤其适合看日志。",
        "common_options": [
            "tail -n 100 文件名：查看最后 100 行",
            "tail -f 文件名：持续跟踪日志更新"
        ],
        "usage_scenarios": [
            "查看日志最后几行",
            "观察服务运行日志",
            "排查最新报错"
        ],
        "tips": [
            "排障时，tail 是非常高频的命令",
            "tail -f 常用于实时看日志滚动输出"
        ],
        "beginner_steps": [
            {
                "step": "先看日志最后几十行",
                "command": "tail -n 50 日志文件名",
                "purpose": "先抓住最近发生的问题。",
                "look_for": "重点看 error、exception、traceback 等关键词。",
                "next_action": "如果内容不够，再增大行数。"
            },
            {
                "step": "如果你想实时观察日志变化",
                "command": "tail -f 日志文件名",
                "purpose": "持续跟踪日志输出。",
                "look_for": "看新日志是否持续出现、是否有报错。",
                "next_action": "如果想停止跟踪，按 Ctrl + C。"
            }
        ]
    },
    {
        "keywords": ["grep", "grep -i", "grep -n"],
        "command_name": "grep",
        "purpose": "在文本中搜索关键词。",
        "common_options": [
            "grep 关键词 文件名：搜索关键词",
            "grep -i：忽略大小写",
            "grep -n：显示行号"
        ],
        "usage_scenarios": [
            "在日志中搜索 error",
            "查找配置项",
            "过滤命令输出"
        ],
        "tips": [
            "grep 是 Linux 排障最常用的命令之一",
            "遇到大段日志时，不要硬看，先 grep 关键词"
        ],
        "beginner_steps": [
            {
                "step": "先搜索最明显的关键词",
                "command": "grep error 日志文件名",
                "purpose": "从长日志中快速定位错误。",
                "look_for": "观察输出中是否有 error 相关内容。",
                "next_action": "如果大小写不一致，再用 -i。"
            },
            {
                "step": "忽略大小写再搜一次",
                "command": "grep -i error 日志文件名",
                "purpose": "避免因为 Error、ERROR 等大小写差异漏掉信息。",
                "look_for": "看输出是否比上一步更多。",
                "next_action": "如果还想定位具体位置，加 -n。"
            },
            {
                "step": "显示行号方便后续定位",
                "command": "grep -n error 日志文件名",
                "purpose": "知道错误出现在第几行附近。",
                "look_for": "重点看输出前面的行号。",
                "next_action": "后续可以结合 cat -n 或 sed 查看上下文。"
            }
        ]
    },
    {
        "keywords": ["ps", "ps aux", "ps -ef"],
        "command_name": "ps",
        "purpose": "查看当前系统中的进程信息。",
        "common_options": [
            "ps aux：查看所有进程",
            "ps -ef：另一种常见格式"
        ],
        "usage_scenarios": [
            "确认某个程序是否在运行",
            "查找服务进程",
            "配合 grep 搜索目标进程"
        ],
        "tips": [
            "ps 往往需要和 grep 搭配使用",
            "如果你怀疑服务没有启动，先看进程再看端口"
        ],
        "beginner_steps": [
            {
                "step": "先查看所有进程",
                "command": "ps aux",
                "purpose": "了解当前系统里有哪些进程。",
                "look_for": "输出会很多，重点不在全部读完，而是确认命令能正常执行。",
                "next_action": "如果要找特定服务，马上配合 grep。"
            },
            {
                "step": "搜索目标进程",
                "command": "ps aux | grep 服务名",
                "purpose": "快速确认某个程序是否在运行。",
                "look_for": "如果看到对应服务进程，说明它大概率在运行；如果只有 grep 自己，说明目标进程可能不存在。",
                "next_action": "如果进程不存在，再回头检查服务启动是否失败。"
            }
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
            "查看某个端口是否在监听",
            "排查服务启动后是否占用了目标端口"
        ],
        "tips": [
            "如果你在排查 Connection refused，ss -ltnp 很关键",
            "输出里最重要的是端口号和进程信息"
        ],
        "beginner_steps": [
            {
                "step": "先查看所有监听中的 TCP 端口",
                "command": "ss -ltnp",
                "purpose": "确认系统上哪些端口已经被程序监听。",
                "look_for": "重点看 Local Address:Port 和 Process 信息。",
                "next_action": "如果端口太多，再用 grep 过滤。"
            },
            {
                "step": "如果你只关心某个端口，就过滤它",
                "command": "ss -ltnp | grep 8000",
                "purpose": "快速确认目标端口是否存在。",
                "look_for": "如果有输出，说明 8000 端口正在监听；如果没有，说明它没有监听。",
                "next_action": "如果没监听，再检查服务进程。"
            }
        ]
    },
    {
        "keywords": ["lsof", "lsof -i"],
        "command_name": "lsof",
        "purpose": "查看文件或端口被哪个进程占用。",
        "common_options": [
            "lsof -i :端口号：查看某个端口被谁占用"
        ],
        "usage_scenarios": [
            "排查端口占用",
            "定位占用端口的进程 PID"
        ],
        "tips": [
            "遇到 address already in use 时，lsof 非常好用"
        ],
        "beginner_steps": [
            {
                "step": "直接查目标端口被谁占用",
                "command": "lsof -i :端口号",
                "purpose": "找到占用该端口的进程。",
                "look_for": "重点看 COMMAND、PID、NAME。",
                "next_action": "找到 PID 后，可以决定是否结束该进程。"
            }
        ]
    },
    {
        "keywords": ["chmod", "chmod +x", "chmod 755"],
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
            "初学者一开始不理解数字权限没关系，可以先记住 chmod +x 的用法"
        ],
        "beginner_steps": [
            {
                "step": "先看当前权限",
                "command": "ls -l 文件名",
                "purpose": "确认修改前的权限状态。",
                "look_for": "看最前面的权限位是否有 x。",
                "next_action": "如果没有 x，就可以增加执行权限。"
            },
            {
                "step": "给文件增加执行权限",
                "command": "chmod +x 文件名",
                "purpose": "让该文件能够被执行。",
                "look_for": "命令本身通常没输出，执行后再看权限变化。",
                "next_action": "再执行 ls -l 文件名 检查结果。"
            },
            {
                "step": "再次查看权限是否修改成功",
                "command": "ls -l 文件名",
                "purpose": "确认权限位中是否出现 x。",
                "look_for": "如果看到 x，说明执行权限已经加上了。",
                "next_action": "可以重新运行原脚本进行测试。"
            }
        ]
    },
    {
        "keywords": ["curl", "curl -i", "curl -I", "curl -X"],
        "command_name": "curl",
        "purpose": "向 URL 发送请求，常用于测试接口和网页连通性。",
        "common_options": [
            "curl 地址：发送 GET 请求",
            "curl -I 地址：只查看响应头",
            "curl -i 地址：显示响应头和响应体",
            "curl -X POST 地址：发送 POST 请求"
        ],
        "usage_scenarios": [
            "测试网页是否可访问",
            "测试接口状态码",
            "排查请求超时或 404/500 问题"
        ],
        "tips": [
            "排查接口问题时，curl 是极高频命令",
            "先用 curl -I 看状态码，再决定是否看完整响应"
        ],
        "beginner_steps": [
            {
                "step": "先测试目标地址是否有响应",
                "command": "curl -I 目标地址",
                "purpose": "先看响应头和状态码。",
                "look_for": "重点看 HTTP 状态码，例如 200、404、500。",
                "next_action": "如果状态码异常，再进一步看完整响应。"
            },
            {
                "step": "查看完整响应内容",
                "command": "curl 目标地址",
                "purpose": "查看服务器实际返回的内容。",
                "look_for": "看返回体中是否有报错信息、HTML 页面或 JSON 数据。",
                "next_action": "根据返回内容继续判断问题在客户端还是服务端。"
            }
        ]
    },
    {
        "keywords": ["whoami"],
        "command_name": "whoami",
        "purpose": "显示当前登录用户名称。",
        "common_options": [],
        "usage_scenarios": [
            "确认当前用户身份",
            "排查权限问题"
        ],
        "tips": [
            "当你怀疑自己没有足够权限时，先看 whoami 很有帮助"
        ],
        "beginner_steps": [
            {
                "step": "查看当前用户身份",
                "command": "whoami",
                "purpose": "确认你现在是以谁的身份执行命令。",
                "look_for": "输出通常是一个用户名。",
                "next_action": "如果不是你预期的用户，要结合权限问题继续判断。"
            }
        ]
    }
]