# -*- coding: utf-8 -*-

"""
这个文件保存 Linux / 网络 / 服务相关的常见报错规则。
当前版本强调：
1. 识别错误类型
2. 解释问题
3. 给出更适合新手的手把手排查步骤
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
        "step_by_step": [
            {
                "step": "先检查命令拼写是否正确",
                "command": "（手动检查你输入的命令）",
                "purpose": "排除最常见的拼写错误。",
                "look_for": "例如 python 写成 pyhton，chmod 写成 chmode。",
                "next_action": "如果拼写无误，再继续看命令是否存在。"
            },
            {
                "step": "检查系统是否能找到该命令",
                "command": "which 命令名",
                "purpose": "查看该命令是否已经安装并位于 PATH 中。",
                "look_for": "如果 which 没有输出，说明系统通常找不到这个命令。",
                "next_action": "如果 which 没输出，再检查是否安装相关软件。"
            },
            {
                "step": "进一步查看命令位置说明",
                "command": "whereis 命令名",
                "purpose": "看系统中是否存在该命令的相关文件。",
                "look_for": "如果 whereis 也几乎没有结果，说明大概率没有安装。",
                "next_action": "如果确实没安装，就去安装对应软件。"
            },
            {
                "step": "如果命令明明存在但仍找不到，检查 PATH",
                "command": "echo $PATH",
                "purpose": "确认命令所在目录是否包含在 PATH 中。",
                "look_for": "看命令实际所在目录是否出现在 PATH 输出里。",
                "next_action": "如果没有，需要补 PATH 或使用绝对路径执行。"
            }
        ]
    },
    {
        "keywords": ["permission denied"],
        "error_type": "权限不足",
        "explanation": "当前操作没有足够权限执行，系统拒绝了这次请求。",
        "possible_causes": [
            "当前用户权限不足",
            "文件没有执行权限",
            "文件或目录权限位设置不正确",
            "文件属主不是当前用户"
        ],
        "step_by_step": [
            {
                "step": "先查看目标文件或目录的权限信息",
                "command": "ls -l 文件名",
                "purpose": "确认权限位、属主和属组信息。",
                "look_for": "重点看最前面的权限位，例如是否有 x；还要看属主是不是你当前用户。",
                "next_action": "如果没有 x，可以继续给它增加执行权限。"
            },
            {
                "step": "如果文件没有执行权限，给它增加执行权限",
                "command": "chmod +x 文件名",
                "purpose": "让脚本或程序文件具备执行权限。",
                "look_for": "执行后再次运行 ls -l 文件名，确认权限位里出现 x。",
                "next_action": "如果权限已正确但仍失败，继续检查用户权限。"
            },
            {
                "step": "查看当前用户是谁",
                "command": "whoami",
                "purpose": "确认当前执行命令的用户身份。",
                "look_for": "看当前用户是否应该有权限访问该文件或目录。",
                "next_action": "如果当前用户权限不足，可以尝试 sudo。"
            },
            {
                "step": "尝试使用管理员权限执行",
                "command": "sudo 你的命令",
                "purpose": "确认问题是否由用户权限不足引起。",
                "look_for": "如果 sudo 后命令可以执行，说明原问题大概率是权限不足。",
                "next_action": "如果 sudo 也失败，需要进一步检查文件属主和目录权限。"
            }
        ]
    },
    {
        "keywords": ["connection refused"],
        "error_type": "连接被拒绝",
        "explanation": "客户端尝试连接目标地址和端口，但对方没有接受连接请求。",
        "possible_causes": [
            "目标服务没有启动",
            "目标端口没有监听",
            "IP 地址或端口写错",
            "程序启动后立刻退出"
        ],
        "step_by_step": [
            {
                "step": "先确认你访问的地址和端口是否写对了",
                "command": "（手动核对 URL / IP / 端口）",
                "purpose": "排除最基础的输入错误。",
                "look_for": "重点确认协议、IP、域名、端口号是否正确。",
                "next_action": "如果地址无误，再看服务是否真的启动。"
            },
            {
                "step": "检查目标端口是否正在监听",
                "command": "ss -ltnp",
                "purpose": "查看系统中哪些 TCP 端口正在监听。",
                "look_for": "看输出里是否出现目标端口，例如 :8000、:8080。",
                "next_action": "如果没有目标端口，说明服务大概率没有正常启动。"
            },
            {
                "step": "检查服务进程是否存在",
                "command": "ps aux | grep 服务名",
                "purpose": "确认服务程序本身是否正在运行。",
                "look_for": "如果看不到对应进程，说明程序可能没有启动成功或已经退出。",
                "next_action": "如果进程不存在，就去查看启动日志。"
            },
            {
                "step": "在本机先测试一次服务是否可访问",
                "command": "curl http://127.0.0.1:端口",
                "purpose": "判断服务在本机是否正常提供响应。",
                "look_for": "如果本机都访问失败，说明问题更可能在服务本身；如果本机成功但外部失败，问题更可能在网络、防火墙或代理。",
                "next_action": "根据本机访问结果再继续排查网络层。"
            }
        ]
    },
    {
        "keywords": ["no such file or directory"],
        "error_type": "文件或目录不存在",
        "explanation": "程序访问的文件或目录不存在，或者当前路径不正确。",
        "possible_causes": [
            "路径写错",
            "文件已经移动或删除",
            "当前工作目录不正确",
            "使用了错误的相对路径"
        ],
        "step_by_step": [
            {
                "step": "先确认当前所在目录",
                "command": "pwd",
                "purpose": "看你当前到底位于哪个目录。",
                "look_for": "确认输出路径是不是你以为的那个位置。",
                "next_action": "如果目录不对，先切换到正确位置。"
            },
            {
                "step": "查看当前目录中有什么文件",
                "command": "ls -l",
                "purpose": "确认目标文件是否真的在当前目录下。",
                "look_for": "检查输出里是否出现目标文件名。",
                "next_action": "如果没有这个文件，说明路径可能写错了。"
            },
            {
                "step": "如果你知道大概在哪个目录，先切换过去",
                "command": "cd 正确目录",
                "purpose": "进入更可能包含目标文件的目录。",
                "look_for": "切换后再执行 pwd 和 ls -l，确认文件是否存在。",
                "next_action": "如果仍找不到，考虑直接使用绝对路径。"
            },
            {
                "step": "使用绝对路径重新执行命令",
                "command": "/完整/路径/文件名",
                "purpose": "避免相对路径受到当前工作目录影响。",
                "look_for": "如果绝对路径能成功，说明原问题主要是路径写法不对。",
                "next_action": "后续尽量确认当前目录后再使用相对路径。"
            }
        ]
    },
    {
        "keywords": ["read timed out", "timeout"],
        "error_type": "请求超时",
        "explanation": "请求在规定时间内没有收到完整响应，因此被系统中断。",
        "possible_causes": [
            "网络较慢",
            "目标服务响应过慢",
            "超时时间设置过短",
            "远端服务压力较大或异常"
        ],
        "step_by_step": [
            {
                "step": "先确认目标地址是否能连通",
                "command": "curl -I 目标地址",
                "purpose": "快速测试目标地址是否有基本响应。",
                "look_for": "看是否能拿到响应头，或者是否直接卡住。",
                "next_action": "如果 curl 也很慢或失败，说明问题可能在网络或目标服务。"
            },
            {
                "step": "尝试完整请求一次，观察响应速度",
                "command": "curl 目标地址",
                "purpose": "看目标地址是否能在终端中返回内容。",
                "look_for": "观察响应是否明显很慢，或者是否报错。",
                "next_action": "如果响应很慢，考虑增大 timeout。"
            },
            {
                "step": "适当增大程序中的超时时间",
                "command": "把 timeout 参数从 5 改成 10 或 20",
                "purpose": "确认是否只是超时时间过短。",
                "look_for": "如果增大 timeout 后成功，说明原问题更像慢响应而非完全不可用。",
                "next_action": "如果仍超时，需要继续排查目标服务状态。"
            },
            {
                "step": "如果你能控制服务端，检查服务端日志",
                "command": "tail -n 100 日志文件名",
                "purpose": "确认服务端是否存在慢查询、报错或卡死。",
                "look_for": "重点看错误、阻塞、重启、连接异常等日志。",
                "next_action": "根据日志继续定位根因。"
            }
        ]
    },
    {
        "keywords": ["address already in use", "port is already allocated"],
        "error_type": "端口已被占用",
        "explanation": "程序想绑定某个端口，但该端口已经被其他进程占用了。",
        "possible_causes": [
            "已有同类服务正在运行",
            "之前的进程没有正常退出",
            "你选用的端口被其他程序占用"
        ],
        "step_by_step": [
            {
                "step": "先查看哪个进程占用了目标端口",
                "command": "lsof -i :端口号",
                "purpose": "找到占用该端口的进程。",
                "look_for": "重点看 PID 和 COMMAND 字段。",
                "next_action": "找到进程后决定是结束它还是换端口。"
            },
            {
                "step": "也可以从监听视角再确认一次",
                "command": "ss -ltnp | grep 端口号",
                "purpose": "确认端口确实在被监听，并查看对应进程信息。",
                "look_for": "观察输出中是否出现目标端口以及进程名。",
                "next_action": "如果确认被占用，可以结束旧进程。"
            },
            {
                "step": "如确认是无用旧进程，可结束该进程",
                "command": "kill -9 进程PID",
                "purpose": "释放被占用的端口。",
                "look_for": "执行后再次运行 lsof -i :端口号，确认端口是否已释放。",
                "next_action": "如果不方便结束旧进程，也可以直接换一个端口。"
            },
            {
                "step": "如果不想动旧进程，就改用新端口启动",
                "command": "把程序配置端口改成另一个未占用端口",
                "purpose": "绕开端口冲突。",
                "look_for": "重启后确认新端口已经成功监听。",
                "next_action": "后续保持端口配置的一致性。"
            }
        ]
    },
    {
        "keywords": ["name or service not known", "temporary failure in name resolution"],
        "error_type": "DNS 解析失败",
        "explanation": "系统无法把域名解析成 IP 地址，因此请求无法继续。",
        "possible_causes": [
            "DNS 配置异常",
            "网络环境不稳定",
            "域名本身写错",
            "临时的 DNS 服务故障"
        ],
        "step_by_step": [
            {
                "step": "先检查域名拼写是否正确",
                "command": "（手动检查域名）",
                "purpose": "排除最基础的输入错误。",
                "look_for": "例如 github.cm、gihub.com 这类拼写问题。",
                "next_action": "如果拼写无误，再检查 DNS 解析。"
            },
            {
                "step": "尝试手动解析域名",
                "command": "nslookup 域名",
                "purpose": "检查系统能否把域名解析成 IP。",
                "look_for": "如果 nslookup 失败，说明 DNS 解析确实有问题。",
                "next_action": "如果解析失败，再检查网络和 DNS 配置。"
            },
            {
                "step": "检查网络连通性",
                "command": "ping 8.8.8.8",
                "purpose": "确认基础网络是否通畅。",
                "look_for": "如果连 IP 都 ping 不通，说明问题可能不只是 DNS，而是网络本身。",
                "next_action": "如果 IP 可通但域名不通，问题更偏 DNS。"
            },
            {
                "step": "重新测试域名访问",
                "command": "curl 域名地址",
                "purpose": "确认解析和访问是否恢复。",
                "look_for": "如果后续恢复正常，可能是临时 DNS 故障。",
                "next_action": "如果仍不行，考虑更换 DNS 或检查代理。"
            }
        ]
    },
    {
        "keywords": ["404 not found", "404"],
        "error_type": "资源不存在（404）",
        "explanation": "请求到达了服务器，但服务器上没有你请求的这个资源路径。",
        "possible_causes": [
            "URL 路径写错",
            "资源已经删除",
            "接口版本或路由变更",
            "请求方法与接口定义不一致"
        ],
        "step_by_step": [
            {
                "step": "先确认 URL 路径是否正确",
                "command": "（手动检查 URL）",
                "purpose": "排除路径拼写错误或层级写错。",
                "look_for": "例如 /api/v1/test 和 /api/test 是否写混了。",
                "next_action": "如果路径无误，再直接请求一次观察返回。"
            },
            {
                "step": "用 curl 直接请求该地址",
                "command": "curl -I 目标URL",
                "purpose": "确认服务器返回的状态码是否确实是 404。",
                "look_for": "重点看 HTTP 状态码是否为 404。",
                "next_action": "如果一直是 404，说明不是客户端偶发问题。"
            },
            {
                "step": "如果这是接口地址，检查接口文档或路由配置",
                "command": "（查看接口文档 / 路由定义）",
                "purpose": "确认当前接口路径是否真的存在。",
                "look_for": "看文档中的接口路径、版本号、请求方法是否和你现在一致。",
                "next_action": "如果文档变了，就按最新路径重新请求。"
            }
        ]
    },
    {
        "keywords": ["500 internal server error", "500"],
        "error_type": "服务器内部错误（500）",
        "explanation": "请求已经到达服务器，但服务器在处理请求时发生了内部异常。",
        "possible_causes": [
            "服务端代码报错",
            "数据库或依赖服务异常",
            "参数导致服务端逻辑崩溃"
        ],
        "step_by_step": [
            {
                "step": "先确认服务端确实返回 500",
                "command": "curl -I 目标URL",
                "purpose": "确认状态码是否为 500。",
                "look_for": "重点看 HTTP 状态码和响应头。",
                "next_action": "如果确认是 500，问题重点在服务端。"
            },
            {
                "step": "查看服务端日志",
                "command": "tail -n 100 日志文件名",
                "purpose": "找到导致 500 的真实异常信息。",
                "look_for": "重点找 traceback、exception、error 等关键词。",
                "next_action": "先定位第一条真正的异常，再决定修复路径。"
            },
            {
                "step": "如果服务是本机运行的，检查进程是否反复退出重启",
                "command": "ps aux | grep 服务名",
                "purpose": "看服务是否稳定运行。",
                "look_for": "如果进程频繁退出，说明内部问题可能比较严重。",
                "next_action": "结合日志继续定位。"
            }
        ]
    }
]