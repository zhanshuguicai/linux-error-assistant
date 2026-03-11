# Linux 新手报错分析与命令解释助手

## 中文简介

这是一个使用 Python 编写的小工具，目标是帮助 Linux 初学者更容易理解常见报错、常用命令和基础排障思路。

当前版本支持四类功能：

- 报错分析
- 命令解释
- 场景命令检索
- AI 分析

和普通“只给几句解释”的工具不同，这个项目更强调：

- 宝宝级别的 debug 流程教学
- 用更容易理解的中文解释问题
- 给出更适合新手的排查思路
- 尽量提供可以直接复制到终端执行的命令
- 告诉用户每一步应该看什么输出、下一步怎么判断

---

## 当前功能

目前已经实现：

1. **报错分析**
   - 识别部分常见 Linux / 网络 / 服务相关错误
   - 输出错误类型、问题解释、可能原因
   - 提供更适合新手的手把手排查步骤

2. **命令解释**
   - 解释常见 Linux 命令的作用
   - 给出常见参数
   - 给出适用场景和新手使用步骤

3. **场景命令检索**
   - 当用户不知道具体命令时，可以直接输入“想做什么”
   - 程序会返回推荐命令和建议顺序

4. **AI 分析**
   - 对规则库未覆盖的问题，尝试使用 AI 给出更灵活的解释
   - AI 输出同样强调“步骤、命令、观察点、下一步判断”

## 当前覆盖内容

### 报错分析目前覆盖的典型类型

- `command not found`
- `permission denied`
- `connection refused`
- `no such file or directory`
- `read timed out`
- `timeout`
- `address already in use`
- `port is already allocated`
- `name or service not known`
- `temporary failure in name resolution`
- `404 not found`
- `500 internal server error`

### 命令解释目前覆盖的典型命令

- `pwd`
- `cd`
- `ls`
- `cat`
- `tail`
- `grep`
- `ps`
- `ss`
- `lsof`
- `chmod`
- `curl`
- `whoami`

### 场景命令检索目前覆盖的典型场景

- 查看当前目录
- 查看目录内容
- 查看日志
- 搜索日志关键词
- 查看进程
- 查看端口占用
- 测试网址或接口
- 给脚本加执行权限
- 查看当前用户

---

## 项目结构

```text
linux-error-assistant/
├─ main.py
├─ error_rules.py
├─ command_rules.py
├─ scenario_rules.py
├─ ai_analyzer.py
├─ config.py
├─ sample_inputs.txt
├─ outputs/
├─ requirements.txt
├─ README.md
```

## 文件说明

- `main.py`：主程序入口，负责菜单、输入、结果打印和保存
- `error_rules.py`：报错分析规则库
- `command_rules.py`：命令解释规则库
- `scenario_rules.py`：场景命令检索规则库
- `ai_analyzer.py`：AI 分析逻辑
- `config.py`：AI 接口配置
- `sample_inputs.txt`：示例输入
- `outputs/`：分析结果输出目录

## 运行环境

建议运行环境：

- Python 3.9 及以上版本

当前依赖：

- `requests`

## 安装依赖

```bash
pip install -r requirements.txt
```

`requirements.txt` 内容示例：

```txt
requests
```

## 运行方式

在项目目录下运行：

```bash
python main.py
```

程序启动后会显示菜单：

```text
请选择功能：
1. 报错分析
2. 命令解释
3. 场景命令检索
4. AI 分析
```

然后根据提示输入内容即可。

## 使用示例

### 1. 报错分析

输入：

```text
Permission denied
```

程序会输出：

- 错误类型
- 问题解释
- 可能原因
- 手把手排查步骤
- 每一步建议执行的命令
- 每一步应该观察什么

### 2. 命令解释

输入：

```text
ss -ltnp
```

程序会输出：

- 命令用途
- 常见参数
- 适用场景
- 新手上手步骤
- 每一步应该重点看哪些输出

### 3. 场景命令检索

输入：

```text
查看端口占用
```

程序会输出：

- 识别到的场景
- 推荐命令
- 建议操作顺序
- 每一步的说明和观察点

### 4. AI 分析

输入：

```text
curl 请求超时怎么办
```

如果已经配置 AI 接口，程序会尝试用更灵活的方式输出：

- 识别类型
- 问题解释
- 可能原因
- 手把手操作步骤
- 每一步的命令与观察点

## 设计思路

这个项目不是单纯做“报错识别”，而是希望尽量向“适合 Linux 初学者的排障学习工具”靠近。

因此在设计上，我做了几个取舍：

- 规则库优先
- 对常见问题先用规则库覆盖（这样稳定、可控，也更容易解释）
- 输出尽量步骤化
- 不只告诉用户“检查一下”，而是尽量告诉用户“下一步在终端输入什么”
- 每一步都给观察点
- 不是只给命令，还尽量告诉用户执行后看什么、怎么判断下一步
- AI 作为增强，用来处理规则库暂时没覆盖的问题，也用来让分析更灵活

## AI 配置说明

如果你想使用 AI 分析功能，需要在 `config.py` 中配置：

- `API_BASE_URL`
- `API_KEY`
- `MODEL_NAME`
- `REQUEST_TIMEOUT`

例如：

```python
API_BASE_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "你的key"
MODEL_NAME = "gpt-4o-mini"
REQUEST_TIMEOUT = 20
```

如果 `API_KEY` 为空，程序会提示 AI 分析不可用。

## 输出文件

程序每次分析后会把结果保存到 `outputs/` 目录中，文件名中包含时间戳，例如：

```text
outputs/analysis_20260311_203015.json
```

这样做的目的是：

- 保留分析记录
- 方便后续查看
- 为以后做历史记录功能留出空间

## 当前不足

这个项目目前还是第一版，仍然有不少不足，例如：

- 规则覆盖范围还不够全面
- 规则匹配目前主要依赖关键词，仍然比较基础
- 命令解释和场景检索还可以继续扩展
- AI 分析依赖外部接口，可能受到网络和配置影响
- 还没有图形界面
- 还没有批量分析功能

## 后续计划

后续我希望继续完善：

- 扩展更多常见报错类型
- 扩展更多 Linux 命令解释
- 扩展更多“新手常见场景”
- 增加批量分析功能
- 增加更清晰的结果展示方式
- 尝试加入更细的错误分类
- 进一步优化 AI 输出稳定性

## 项目定位

这个项目是一个面向 Linux 初学者的学习型小助手：

- 帮助理解常见报错
- 帮助理解常见命令
- 帮助把“知道问题”变成“知道下一步怎么操作”

## 作者

本人