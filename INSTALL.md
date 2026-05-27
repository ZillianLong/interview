# 心理风险面试 Skill · 他人安装说明（HTTPS）

与他人给你的 **AI 素养 eval** 仓库安装方式**同一套逻辑**：`git clone` → `cd` → `chmod +x install.sh` → `./install.sh`。

> 仓库：`https://github.com/ZillianLong/interview.git`  
> 说明：面试观察记录工具，**非临床诊断**。

---

## 一键安装（推荐，与对方仓库一致）

```bash
git clone https://github.com/ZillianLong/interview.git
cd interview
chmod +x install.sh
./install.sh
```

`install.sh` 会：

1. 将 `.cursor/skills/` 下 Skill 复制到 `~/.cursor/skills/`（全局可用）
2. 安装 Python 依赖 `openpyxl`
3. 创建 `效果验证/面试记录`、`效果验证/专家材料反馈` 目录（若不存在）

安装完成后：

1. **重启 Cursor** 或新开 Agent 对话  
2. 在 Cursor 中 **File → Open Folder**，打开刚克隆的 **`interview` 仓库根目录**（必做，见下节「与 AI 素养仓库的差异」）  
3. 对话输入：`/psych-interview-risk-recording`

### 安装到自定义路径（可选）

```bash
./install.sh /path/to/your/skills
```

---

## 与 `cursor-skills-ai-literacy-eval` 的对比

| 步骤 | AI 素养 eval 仓库 | 本仓库（interview） |
|------|-------------------|---------------------|
| 克隆 | `git clone https://github.com/.../cursor-skills-ai-literacy-eval.git` | `git clone https://github.com/ZillianLong/interview.git` |
| 进入目录 | `cd cursor-skills-ai-literacy-eval` | `cd interview` |
| 可执行权限 | `chmod +x install.sh` | 相同 |
| 安装 | `./install.sh` | 相同 |
| 使用 Skill | 任意项目里都可调用；数据另放 `AI素养-结果评分评测集` | **必须打开本仓库根目录**，题本与 xlsx 在仓库内 |

**逻辑一样：** 都是把 `skills` 装进 `~/.cursor/skills/`，让 Cursor Agent 能发现 Skill。

**差别一点：** AI 素养仓库是 **纯 Skill 包**，评测数据在你自己的工作区；本仓库是 **Skill + 题本 + 等级描述 + 落盘目录** 一体，Python 脚本按**仓库根目录**写 Excel。所以别人 clone 后除了 `./install.sh`，还要用 Cursor **打开这个仓库文件夹** 再面试，不能只装在全局就去别的空项目里用。

---

## 环境要求

| 项目 | 要求 |
|------|------|
| Cursor | 最新稳定版 |
| Python | 3.9+ |
| Git | 能 `git clone` HTTPS；私有库需 PAT 与读权限 |

---

## HTTPS 克隆说明

```bash
git clone https://github.com/ZillianLong/interview.git
```

私有仓库：GitHub 账号需被邀请；密码处用 **Personal Access Token**，不是登录密码。

更新：

```bash
cd interview && git pull
```

---

## 其他安装方式

### 方式 B：不跑 install.sh，仅打开项目（协作者）

clone 后直接用 Cursor 打开仓库根目录。项目内已有 `.cursor/skills/`，无需复制到全局。

### 方式 C：仅当前项目复制 Skill

```bash
mkdir -p .cursor/skills
cp -R .cursor/skills/psych-interview-risk-recording .cursor/skills/
# 或从他人仓库复制整个 skills 子目录
```

---

## 使用与产出

**开始面试：** `/psych-interview-risk-recording` 或说明「开始心理风险面试记录」

**产出：**

| 文件 | 路径 |
|------|------|
| 面试记录 | `效果验证/面试记录/面试记录_{标识}.xlsx` |
| 专家反馈 | `效果验证/专家材料反馈/专家材料反馈_{标识}.md` |
| 题本 | `面试观察.md` |
| 等级描述 | `效果验证/维度得分描述.xlsx` |

**手动校验：**

```bash
python3 .cursor/skills/psych-interview-risk-recording/scripts/write_record.py \
  效果验证/面试记录/面试记录_{标识}.xlsx
```

---

## 仓库内 Skill

| Skill | 用途 |
|-------|------|
| `psych-interview-risk-recording` | HR 互动面试、低/中/高、落盘（常用） |
| `psych-interview-observation` | 撰写/维护题本（维护者用） |

---

## 常见问题

**`Permission denied: ./install.sh`**  
→ 先执行 `chmod +x install.sh`

**Cursor 里找不到 Skill**  
→ 是否执行过 `./install.sh`；重启 Cursor；Skill 名 `/psych-interview-risk-recording`

**Excel 写到错误位置 / 找不到题本**  
→ 是否用 Cursor 打开了 **interview 仓库根目录**（含 `面试观察.md` 的目录）

**`ModuleNotFoundError: openpyxl`**  
→ `pip3 install openpyxl` 或重新 `./install.sh`

---

## 发给同事（可复制）

```text
git clone https://github.com/ZillianLong/interview.git
cd interview
chmod +x install.sh
./install.sh
# Cursor 打开 interview 文件夹，对话输入：/psych-interview-risk-recording
```

---

## 地址对照

| 方式 | URL |
|------|-----|
| HTTPS | `https://github.com/ZillianLong/interview.git` |
| SSH | `git@github.com:ZillianLong/interview.git` |
