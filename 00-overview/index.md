# 00 · 仓库总览与使用说明

这一页解释仓库的两层结构、source of truth、generated files 与内容更新边界。

## 1. 两层结构

### Knowledge Layer
用于系统学习与研究推理：

```text
fundamentals
→ Scientific ML
→ observation / inverse / DA / UQ
→ spatiotemporal / multimodal
→ Earth Observation / Carbon / Weather
→ Foundation Models
→ HPC / Evaluation
```

入口：[Scientific / Physical / Earth AI Knowledge Base](../01-knowledge-base/index.md)。

### Evidence / Resource Layer
用于保存可追溯的论文、代码、数据集、benchmark 与 case-study resources：

- [Paper Library](../02-paper-library/index.md)
- [Code Library](../03-code-library/index.md)
- [Dataset Library](../04-dataset-library/index.md)
- [Benchmarks](../05-benchmarks-and-evaluation/index.md)
- [Case Studies](../06-case-studies/index.md)

---

## 2. Source of Truth

`metadata/` 下的 canonical records 是 paper/code/dataset/benchmark resource layer 的 source of truth。

由脚本生成的 index/card/view：
- 不手工修改；
- 应修改 canonical metadata 后重新生成；
- generated-file drift 由仓库检查发现。

详细规则见 [AGENTS.md](../AGENTS.md) 与 [CONTRIBUTING.md](../CONTRIBUTING.md)。

---

## 3. Human-authored Knowledge Pages

`01-knowledge-base/` 主要是 human-authored knowledge synthesis，可以更新结构和解释，但必须：

- 不伪造 citation；
- fast-moving claim 使用 original/official source；
- 明确 `Official / Peer-reviewed / Preprint`；
- 不把 repository synthesis 写成 paper 原话；
- 避免破坏现有链接；
- 修改后通过 repository checks。

---

## 4. 当前知识基线

Fast-moving cutoff：**2026-08-20**。

当前版本状态统一维护在：[2026-08-20 Snapshot](../01-knowledge-base/13-2026-snapshot/index.md)。

稳定数学/物理概念不会因为新模型发布而反复改写。

---

## 5. 推荐入口

如果是第一次使用仓库：

1. [Root README](../README.md)
2. [Knowledge Base](../01-knowledge-base/index.md)
3. [Learning Paths](../01-knowledge-base/learning-paths/index.md)
4. [Detailed Knowledge Index](../01-knowledge-base/DETAILED_INDEX.md)
5. 再进入 paper/code/dataset evidence layer。
