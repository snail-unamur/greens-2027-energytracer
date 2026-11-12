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
| `dram_mj` | 2.009 mJ          | 2.041 mJ             |
| `time_s`  | 0.019 s           | 0.019 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions)

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 285495 | 0.9105      | 2.28e-47 | Rejected |
| `cpu_mj`  | Without smell | 285687 | 0.9151      | 1.71e-46 | Rejected |
| `gpu_mj`  | With smell    | 285956 | 0.9126      | 5.60e-47 | Rejected |
| `gpu_mj`  | Without smell | 285824 | 0.9116      | 3.76e-47 | Rejected |
| `dram_mj` | With smell    | 288322 | 0.8715      | 1.62e-53 | Rejected |
| `dram_mj` | Without smell | 291548 | 0.7963      | 6.18e-62 | Rejected |
| `time_s`  | With smell    | 285887 | 0.9149      | 1.53e-46 | Rejected |
| `time_s`  | Without smell | 285841 | 0.9096      | 1.58e-47 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean      | p-value   | Cohen’s d | Effect     | Sig. |
| --------- | ----------- | --------- | --------- | ---------- | ---- |
| `cpu_mj`  | -0.20%      | 4.32e-218 | -0.083    | negligible | ✅   |
| `gpu_mj`  | -0.10%      | 1.93e-52  | -0.040    | negligible | ✅   |
| `ane_mj`  | -325834.72% | 0.00e+00  | -0.476    | small      | ✅   |
| `dram_mj` | -1.58%      | 0.00e+00  | -0.373    | small      | ✅   |
| `time_s`  | -0.06%      | 2.63e-21  | -0.025    | negligible | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`ane_mj`**: 325834.7% higher energy (Cohen’s d = -0.476, small)
- **`dram_mj`**: 1.6% higher energy (Cohen’s d = -0.373, small)

> Verdict percentages describe the change relative to the with-smell mean.
