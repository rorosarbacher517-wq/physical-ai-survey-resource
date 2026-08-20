# Weather / Earth-system Foundation Models

## 1. Forecast model 与 Foundation Model 的区别

一个 weather neural network 能做 10-day forecast，不自动等于 foundation model。

Foundation route 更强调：
- heterogeneous large-scale pretraining；
- multiple resolutions/data sources；
- multiple downstream tasks；
- adaptation with limited task-specific data。

---

## 2. Aurora

Nature 2025 `Aurora`：
- 预训练超过 1 million hours heterogeneous geophysical data；
- adaptation 到 weather、air quality、ocean wave、tropical-cyclone/high-resolution tasks。

2026-07-09 `Aurora 1.5` official extension：
- open model release；
- additional weather variables；
- hourly temporal resolution；
- probabilistic ensemble forecasting capability。

Sources:
- https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/
- https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/

---

## 3. WeatherNext 2

WeatherNext 2 更适合看作 current probabilistic weather-model family，而不是“跨所有 Earth tasks 的 FM”。

其 FGN route 通过 function-space noise 生成 coherent forecast scenarios。

截至 2026-08-20 已开放 model code/weights。

Official: https://deepmind.google/science/weathernext/

---

## 4. Pretraining axes

Earth-system FM 可沿：
- variables；
- pressure levels；
- resolutions；
- reanalyses；
- forecast tasks；
- chemistry/ocean/waves；
- observation modalities；
- regions

扩展。

---

## 5. Adaptation

```text
pretrained backbone
→ task-specific input/output adapters
→ fine-tune
```

需要报告：
- frozen vs full fine-tune；
- target resolution；
- adaptation data size；
- task-specific head；
- compute。

---

## 6. Failure modes

- pretraining overlap 造成 benchmark advantage；
- coarse pretraining 无法保留 local extreme；
- new variable/unit mapping error；
- future climate shift；
- operational observation distribution change。

---

## 7. 与 EO FM 的区别

EO FM 主要学习**observations/representations**；
weather FM 主要学习**state dynamics / forecasting**；
未来 Earth-system models 会逐渐连接 observation encoder、state estimator 与 dynamical foundation model。
