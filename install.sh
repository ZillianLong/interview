#!/usr/bin/env bash
# 安装心理风险面试 Cursor Skills + Python 依赖
# 用法: ./install.sh           → 安装到 ~/.cursor/skills/
#       ./install.sh /path     → 安装到指定目录
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$HOME/.cursor/skills}"
SKILLS_SRC="$ROOT/.cursor/skills"

echo "==> 仓库根目录: $ROOT"
echo "==> Skill 目标: $DEST"

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "错误: 未找到 $SKILLS_SRC" >&2
  exit 1
fi

mkdir -p "$DEST"
SKILL_NAME="psych-interview-risk-recording"
d="$SKILLS_SRC/$SKILL_NAME"
if [[ ! -d "$d" ]]; then
  echo "错误: 未找到 $d" >&2
  exit 1
fi
rm -rf "$DEST/$SKILL_NAME"
cp -R "$d" "$DEST/$SKILL_NAME"
echo "installed skill: $DEST/$SKILL_NAME"

mkdir -p "$ROOT/效果验证/面试记录" "$ROOT/效果验证/专家材料反馈"

echo "==> 安装 Python 依赖 (openpyxl) ..."
if command -v python3 >/dev/null 2>&1; then
  python3 -m pip install --user openpyxl >/dev/null 2>&1 || python3 -m pip install openpyxl
  python3 -c "import openpyxl" && echo "openpyxl: ok"
else
  echo "警告: 未找到 python3，请手动执行: pip3 install openpyxl" >&2
fi

cat <<EOF

Done.

【重要】本仓库 Skill 依赖同目录下的数据文件（与 AI 素养 eval 纯 Skill 包不同）：
  - 面试观察.md
  - 效果验证/维度得分描述.xlsx
  - 效果验证/面试记录/ 等

请务必在 Cursor 中 **Open Folder → 打开本仓库根目录**：
  $ROOT

然后在新 Agent 对话输入: /psych-interview-risk-recording

若仅执行 install.sh 而未打开本仓库，脚本落盘路径会错误。

EOF
