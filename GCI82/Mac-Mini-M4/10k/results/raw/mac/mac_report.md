## Energy Report — `mac` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric             | With smell | Without smell |
| ------------------ | ---------- | ------------- |
| **Execution Time** | 18.41 ms   | 18.42 ms      |
| **Average Power**  | 6.839 W    | 6.856 W       |
| **Total Energy**   | 37776.88 J | 37882.55 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 125.630 mJ        | 125.866 mJ           |
| `gpu_mj`  | 1.375 mJ          | 1.377 mJ             |
| `ane_mj`  | 0.000 mJ          | 0.062 mJ             |
| `dram_mj` | 2.014 mJ          | 2.045 mJ             |
| `time_s`  | 0.019 s           | 0.019 s              |

### Statistical Analysis

| Metric    | Δ mean  | p-value                      | Cohen’s d | Effect     | Sig. |
| --------- | ------- | ---------------------------- | --------- | ---------- | ---- |
| `cpu_mj`  | -0.19%  | 1.42678644e-145              | -0.067    | negligible | ✅   |
| `gpu_mj`  | -0.09%  | 2.06970283e-34               | -0.032    | negligible | ✅   |
| `ane_mj`  | -99.97% | 1.58044531e-6732 (log-space) | -0.475    | small      | ✅   |
| `dram_mj` | -1.53%  | 2.19387540e-3782 (log-space) | -0.345    | small      | ✅   |
| `time_s`  | -0.06%  | 5.19385936e-14               | -0.020    | negligible | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`ane_mj`**: 320759.0% higher energy (Cohen’s d = -0.475, small)
- **`dram_mj`**: 1.6% higher energy (Cohen’s d = -0.345, small)

> Verdict percentages describe the change relative to the with-smell mean.
