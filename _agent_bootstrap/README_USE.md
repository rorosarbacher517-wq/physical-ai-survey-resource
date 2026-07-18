# Physical AI Survey Resource — Autonomous Build Prompt Pack

本指令包用于让 Codex、Claude Code、Gemini CLI、Cursor Agent 或其他具备文件系统、终端和联网检索能力的代码智能体，从空仓库开始构建并维护 `physical-ai-survey-resource`。

## 重要原则

“完全自主”不等于“允许猜测”。本流程采用 **fail-closed** 策略：

- 无法验证的事实不得写成确定结论；
- 无法确认的链接、许可证、指标和论文信息必须留空并进入待核验队列；
- 任何阶段的结构校验、测试或链接校验失败时，必须先修复，不能继续扩展内容；
- 自动生成的研究性内容必须保留来源、证据级别和最后核验日期；
- 不下载或提交未明确允许再分发的论文 PDF；
- 不把大体量原始数据提交进 Git；
- 不公开用户未授权的未发表研究、密钥、个人信息或受限数据。

## 推荐运行顺序

1. 将本指令包复制到一个空 Git 仓库的 `_agent_bootstrap/` 目录。
2. 把 `AGENTS.md` 复制到仓库根目录。
3. 把 `EXECPLAN.md` 复制到仓库根目录。
4. 向智能体发送 `MASTER_ORCHESTRATOR_PROMPT.md` 的完整内容。
5. 智能体必须依次执行 `prompts/00` 至 `prompts/12`。
6. 每阶段结束后必须运行该阶段规定的验收命令并生成审计报告。
7. 只有状态为 `PASS` 的阶段才能进入下一阶段。
8. 最终发布前执行 `prompts/12_final_release_audit.md`。

## 推荐工作模式

- 每个阶段独立提交一次 Git commit。
- 不允许直接在默认分支进行大规模生成；使用 `build/v1-autonomous` 分支。
- 并行智能体只能操作独立 worktree 或独立分支。
- 一个“研究智能体”负责找资料，一个“实现智能体”负责脚本与站点，一个“审计智能体”只做检查，不参与原始生成。
- 审计智能体不能默认相信生成智能体的自述，必须重新运行测试和抽样核验。

## 完成标准

仓库只有同时满足以下条件才算 v1 完成：

- 目录、命名、元数据和交叉引用全部通过自动校验；
- 所有索引均由结构化元数据自动生成，而不是手工维护多份；
- 所有外部事实都能追踪到来源；
- 无重复论文、孤立 ID、断裂内部链接或未知分类标签；
- 无付费论文 PDF、无大数据文件、无密钥；
- 至少完成一条端到端资源链：论文 → 方法 → 代码 → 数据集 → benchmark → 综述章节；
- 地学遥感专题形成独立导航；
- CI 在干净环境中通过；
- 发布审计报告列出已知限制，不能声称“零错误”。

## 人工输入入口

用户特有内容统一放在：

```text
inputs/
├── survey-manuscript/
├── user-materials/
├── approved-figures/
└── private-not-for-publication/
```

智能体只能使用 `inputs/user-materials/` 和 `inputs/survey-manuscript/` 中明确允许使用的材料。`private-not-for-publication/` 默认禁止进入公开输出。
