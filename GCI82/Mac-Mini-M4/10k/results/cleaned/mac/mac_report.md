## Energy Report — `mac` (cleaned)

> 293868 samples (with smell) vs 293823 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric             | With smell | Without smell |
| ------------------ | ---------- | ------------- |
| **Execution Time** | 18.30 ms   | 18.31 ms      |
| **Average Power**  | 6.835 W    | 6.856 W       |
| **Total Energy**   | 36748.70 J | 36876.79 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 125.316 mJ        | 125.563 mJ           |
| `gpu_mj`  | 1.372 mJ          | 1.373 mJ             |
| `ane_mj`  | 0.000 mJ          | 0.062 mJ             |
| `dram_mj` | 2.009 mJ          | 2.041 mJ             |
| `time_s`  | 0.019 s           | 0.019 s              |

### Statistical Analysis

| Metric    | Δ mean  | p-value                      | Cohen’s d | Effect     | Sig. |
| --------- | ------- | ---------------------------- | --------- | ---------- | ---- |
| `cpu_mj`  | -0.20%  | 4.31918125e-218              | -0.083    | negligible | ✅   |
| `gpu_mj`  | -0.10%  | 1.92942560e-52               | -0.040    | negligible | ✅   |
| `ane_mj`  | -99.97% | 4.47506067e-6620 (log-space) | -0.476    | small      | ✅   |
| `dram_mj` | -1.56%  | 8.48990261e-4299 (log-space) | -0.373    | small      | ✅   |
| `time_s`  | -0.06%  | 2.62674392e-21               | -0.025    | negligible | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`ane_mj`**: 325834.7% higher energy (Cohen’s d = -0.476, small)
- **`dram_mj`**: 1.6% higher energy (Cohen’s d = -0.373, small)

> Verdict percentages describe the change relative to the with-smell mean.
