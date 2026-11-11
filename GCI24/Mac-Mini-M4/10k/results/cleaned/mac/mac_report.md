## Energy Report — `mac` (cleaned)

> 299999 samples (with smell) vs 290170 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 63.20 ms    | 4.18 ms       |
| **Average Power**  | 6.139 W     | 6.131 W       |
| **Total Energy**   | 116389.38 J | 7437.22 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 348.356 mJ        | 24.782 mJ            |
| `gpu_mj`  | 5.445 mJ          | 0.370 mJ             |
| `ane_mj`  | 0.000 mJ          | 0.000 mJ             |
| `dram_mj` | 34.165 mJ         | 1.744 mJ             |
| `time_s`  | 0.063 s           | 0.004 s              |

### Statistical Analysis

Welch's test was undefined for: `ane_mj`.

| Metric    | Δ mean    | p-value                        | Cohen’s d | Effect | Sig. |
| --------- | --------- | ------------------------------ | --------- | ------ | ---- |
| `cpu_mj`  | +1305.69% | 2.89933329e-357141 (log-space) | +21.532   | large  | ✅   |
| `gpu_mj`  | +1372.21% | 1.78190911e-306872 (log-space) | +14.534   | large  | ✅   |
| `dram_mj` | +1859.10% | 7.50220620e-359189 (log-space) | +22.113   | large  | ✅   |
| `time_s`  | +1355.79% | 3.74881946e-357008 (log-space) | +21.667   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 92.9% lower energy (Cohen’s d = +21.532, large)
- **`gpu_mj`**: 93.2% lower energy (Cohen’s d = +14.534, large)
- **`dram_mj`**: 94.9% lower energy (Cohen’s d = +22.113, large)
- **`time_s`**: 93.1% lower time (Cohen’s d = +21.667, large)

> Verdict percentages describe the change relative to the with-smell mean.
