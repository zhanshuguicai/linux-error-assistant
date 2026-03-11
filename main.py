# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime

from error_rules import ERROR_RULES
from command_rules import COMMAND_RULES
from scenario_rules import SCENARIO_RULES
from ai_analyzer import analyze_with_ai


def analyze_by_rules(error_text):
    text_lower = error_text.lower()

    for rule in ERROR_RULES:
        for keyword in rule["keywords"]:
            if keyword in text_lower:
                return {
                    "mode": "规则报错分析",
                    "recognized": True,
                    "input_text": error_text,
                    "error_type": rule["error_type"],
                    "explanation": rule["explanation"],
                    "possible_causes": rule["possible_causes"],
                    "step_by_step": rule["step_by_step"],
                    "matched_keyword": keyword
                }

    return {
        "mode": "规则报错分析",
        "recognized": False,
        "input_text": error_text,
        "error_type": "未识别错误",
        "explanation": "当前规则库没有识别出该报错。",
        "possible_causes": [
            "当前报错不在规则覆盖范围内",
            "报错文本过短或信息不足",
            "报错信息过于依赖上下文"
        ],
        "step_by_step": [
            {
                "step": "先保留完整报错原文，不要只截取其中一小段",
                "command": "（无固定命令）",
                "purpose": "保证后续分析时信息足够完整。",
                "look_for": "尽量保留报错前后几行上下文。",
                "next_action": "如果你能补充上下文，再重新分析。"
            },
            {
                "step": "查看原始日志或命令输出的上下文",
                "command": "tail -n 50 日志文件名",
                "purpose": "查看错误前后发生了什么。",
                "look_for": "重点看报错前后几行是否有更具体的异常信息。",
                "next_action": "如果找到更具体关键词，再把完整内容输入工具或使用 AI 分析。"
            },
            {
                "step": "尝试使用 AI 分析模式",
                "command": "在本工具中选择 4. AI 分析",
                "purpose": "让模型基于更灵活的理解方式分析未知报错。",
                "look_for": "观察 AI 是否给出更具体的排查命令和顺序。",
                "next_action": "如果 AI 仍然无法判断，说明原始信息可能还不够。"
            }
        ],
        "matched_keyword": ""
    }


def explain_command(command_text):
    text_lower = command_text.lower()

    for rule in COMMAND_RULES:
        for keyword in rule["keywords"]:
            if keyword in text_lower:
                    return {
                    "mode": "命令解释",
                    "recognized": True,
                    "input_text": command_text,
                    "command_name": rule["command_name"],
                    "purpose": rule["purpose"],
                    "common_options": rule["common_options"],
                    "usage_scenarios": rule["usage_scenarios"],
                    "tips": rule["tips"],
                    "beginner_steps": rule.get("beginner_steps", []),
                    "matched_keyword": keyword
                }

    return {
        "mode": "命令解释",
        "recognized": False,
        "input_text": command_text,
        "command_name": "未识别命令",
        "purpose": "当前规则库没有识别出该命令。",
        "common_options": [],
        "usage_scenarios": [],
        "tips": [
            "可以输入更完整的命令",
            "后续可以继续扩展命令规则库",
            "也可以尝试使用 AI 分析模式"
        ],
        "matched_keyword": ""
    }


def find_commands_by_scenario(scenario_text):
    text_lower = scenario_text.lower()

    for rule in SCENARIO_RULES:
        for keyword in rule["keywords"]:
            if keyword in text_lower:
                    return {
                    "mode": "场景命令检索",
                    "recognized": True,
                    "input_text": scenario_text,
                    "scenario": rule["scenario"],
                    "recommended_commands": rule["recommended_commands"],
                    "explanation": rule["explanation"],
                    "step_by_step": rule.get("step_by_step", []),
                    "matched_keyword": keyword
                }

    return {
        "mode": "场景命令检索",
        "recognized": False,
        "input_text": scenario_text,
        "scenario": "未识别场景",
        "recommended_commands": [],
        "explanation": "当前规则库没有识别出这个使用场景。",
        "matched_keyword": ""
    }


def print_error_result(result):
    print("\n========== 分析结果 ==========")
    print(f"分析模式：{result['mode']}")
    print(f"原始输入：{result['input_text']}")
    print(f"错误类型：{result['error_type']}")
    print(f"问题解释：{result['explanation']}")

    print("\n可能原因：")
    for i, cause in enumerate(result["possible_causes"], start=1):
        print(f"{i}. {cause}")

    if "step_by_step" in result and result["step_by_step"]:
        print("\n手把手排查步骤：")
        for i, item in enumerate(result["step_by_step"], start=1):
            print(f"\n步骤{i}：{item['step']}")
            print(f"命令：{item['command']}")
            print(f"说明：{item['purpose']}")
            print(f"你应该观察：{item['look_for']}")
            if item.get("next_action"):
                print(f"下一步判断：{item['next_action']}")

def print_command_result(result):
    print("\n========== 命令解释 ==========")
    print(f"原始输入：{result['input_text']}")
    print(f"命令名称：{result['command_name']}")
    print(f"命令用途：{result['purpose']}")

    if result["common_options"]:
        print("\n常见参数：")
        for i, option in enumerate(result["common_options"], start=1):
            print(f"{i}. {option}")

    if result["usage_scenarios"]:
        print("\n适用场景：")
        for i, scenario in enumerate(result["usage_scenarios"], start=1):
            print(f"{i}. {scenario}")

    print("\n新手提示：")
    for i, tip in enumerate(result["tips"], start=1):
        print(f"{i}. {tip}")

    if "beginner_steps" in result and result["beginner_steps"]:
        print("\n新手上手步骤：")
        for i, item in enumerate(result["beginner_steps"], start=1):
            print(f"\n步骤{i}：{item['step']}")
            print(f"命令：{item['command']}")
            print(f"说明：{item['purpose']}")
            print(f"你应该观察：{item['look_for']}")
            if item.get("next_action"):
                print(f"下一步判断：{item['next_action']}")

def print_scenario_result(result):
    print("\n========== 场景命令检索 ==========")
    print(f"原始输入：{result['input_text']}")
    print(f"识别场景：{result['scenario']}")
    print(f"说明：{result['explanation']}")

    if result["recommended_commands"]:
        print("\n推荐命令：")
        for i, cmd in enumerate(result["recommended_commands"], start=1):
            print(f"{i}. {cmd}")

    if "step_by_step" in result and result["step_by_step"]:
        print("\n推荐操作顺序：")
        for i, item in enumerate(result["step_by_step"], start=1):
            print(f"\n步骤{i}：{item['step']}")
            print(f"命令：{item['command']}")
            print(f"说明：{item['purpose']}")
            print(f"你应该观察：{item['look_for']}")
            if item.get("next_action"):
                print(f"下一步判断：{item['next_action']}")

def print_ai_result(input_text, ai_content):
    print("\n========== AI 分析结果 ==========")
    print(f"原始输入：{input_text}")
    print("\nAI 输出内容：")
    print(ai_content)


def save_result(result):
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join("outputs", f"analysis_{timestamp}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return file_path


def choose_function():
    print("请选择功能：")
    print("1. 报错分析")
    print("2. 命令解释")
    print("3. 场景命令检索")
    print("4. AI 分析")

    choice = input("> ").strip()
    return choice


def main():
    print("Linux 新手报错分析与命令解释助手\n")

    choice = choose_function()

    if choice not in {"1", "2", "3", "4"}:
        print("输入的功能编号无效，请重新运行程序。")
        return

    print("\n请输入内容：")
    user_input = input("> ").strip()

    if not user_input:
        print("输入为空，请重新运行程序。")
        return

    if choice == "1":
        result = analyze_by_rules(user_input)
        print_error_result(result)
        file_path = save_result(result)
        print(f"\n分析结果已保存到：{file_path}")
        return

    if choice == "2":
        result = explain_command(user_input)
        print_command_result(result)
        file_path = save_result(result)
        print(f"\n分析结果已保存到：{file_path}")
        return

    if choice == "3":
        result = find_commands_by_scenario(user_input)
        print_scenario_result(result)
        file_path = save_result(result)
        print(f"\n分析结果已保存到：{file_path}")
        return

    if choice == "4":
        ai_result = analyze_with_ai(user_input)
        print_ai_result(user_input, ai_result["content"])

        save_data = {
            "mode": "AI 分析",
            "input_text": user_input,
            "ai_result": ai_result["content"],
            "ai_success": ai_result["success"]
        }
        file_path = save_result(save_data)
        print(f"\n分析结果已保存到：{file_path}")


if __name__ == "__main__":
    main()