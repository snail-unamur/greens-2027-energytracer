## Energy Report — `mac` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 63.20 ms    | 4.26 ms       |
| **Average Power**  | 6.139 W     | 6.217 W       |
| **Total Energy**   | 116389.38 J | 7936.30 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 348.356 mJ        | 25.210 mJ            |
| `gpu_mj`  | 5.445 mJ          | 0.373 mJ             |
| `ane_mj`  | 0.000 mJ          | 0.000 mJ             |
| `dram_mj` | 34.165 mJ         | 1.767 mJ             |
| `time_s`  | 0.063 s           | 0.004 s              |

### Statistical Analysis

Welch's test was undefined for: `ane_mj`.

| Metric    | Δ mean | p-value                        | Cohen’s d | Effect | Sig. |
| --------- | ------ | ------------------------------ | --------- | ------ | ---- |
| `cpu_mj`  | 92.8%  | 8.00195190e-361096 (log-space) | +21.419   | large  | ✅   |
| `gpu_mj`  | 93.1%  | 4.96421357e-307828 (log-space) | +14.506   | large  | ✅   |
| `dram_mj` | 94.8%  | 7.64171091e-360928 (log-space) | +22.059   | large  | ✅   |
| `time_s`  | 93.0%  | 1.78402264e-360171 (log-space) | +21.578   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_with × 100. Positive → the code without smells consumes less energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 92.8% lower energy (Cohen’s d = +21.419, large)
- **`gpu_mj`**: 93.1% lower energy (Cohen’s d = +14.506, large)
- **`dram_mj`**: 94.8% lower energy (Cohen’s d = +22.059, large)
- **`time_s`**: 93.0% lower time (Cohen’s d = +21.578, large)

> Verdict percentages describe the change relative to the with-smell mean.
