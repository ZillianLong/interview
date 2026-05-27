# Cursor Skill · 心理风险面试记录

HR 按专家题本逐题互动面试，对照考察点给出 **低/中/高** 风险等级，收集候选人自我报告与对题反馈，落盘 Excel 与专家材料反馈。**非临床诊断。**

## 仓库内容（仅本 Skill 所需）

```text
.cursor/skills/psych-interview-risk-recording/   # Skill、脚本、reference
面试观察.md                                      # 专家题本
效果验证/维度得分描述.xlsx                        # 等级描述
效果验证/面试记录/                               # 产出目录（.gitkeep）
效果验证/专家材料反馈/                           # 产出目录（含一份模拟样例）
install.sh / INSTALL.md
```

## 安装（Cursor）

```bash
git clone https://github.com/ZillianLong/interview.git
cd interview
chmod +x install.sh
./install.sh
```

用 Cursor **打开本仓库根目录**，对话输入：`/psych-interview-risk-recording`

详见 [INSTALL.md](INSTALL.md)。

## 使用要点

- 对候选人**不呈现**心理维度名称（见 `SKILL.md` 盲维规则）
- 须在本仓库根目录运行，脚本才能正确读写 `效果验证/`

## 许可与免责

面试观察线索，不作医学或心理诊断结论。
