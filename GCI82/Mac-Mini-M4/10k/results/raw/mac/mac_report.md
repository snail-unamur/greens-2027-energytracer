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
| `dram_mj` | 2.014 mJ          | 2.045 mJ             |
| `time_s`  | 0.019 s           | 0.019 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions)

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 292757 | 0.8563      | 1.68e-55 | Rejected |
| `cpu_mj`  | Without smell | 292795 | 0.8579      | 2.66e-55 | Rejected |
| `gpu_mj`  | With smell    | 293142 | 0.8525      | 5.66e-56 | Rejected |
| `gpu_mj`  | Without smell | 292910 | 0.8607      | 5.97e-55 | Rejected |
| `dram_mj` | With smell    | 295262 | 0.8558      | 1.44e-55 | Rejected |
| `dram_mj` | Without smell | 297499 | 0.7955      | 5.23e-62 | Rejected |
| `time_s`  | With smell    | 293012 | 0.8618      | 8.13e-55 | Rejected |
| `time_s`  | Without smell | 292926 | 0.8650      | 2.16e-54 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean      | p-value   | Cohen’s d | Effect     | Sig. |
| --------- | ----------- | --------- | --------- | ---------- | ---- |
| `cpu_mj`  | -0.19%      | 1.43e-145 | -0.067    | negligible | ✅   |
| `gpu_mj`  | -0.09%      | 2.07e-34  | -0.032    | negligible | ✅   |
| `ane_mj`  | -320758.99% | 0.00e+00  | -0.475    | small      | ✅   |
| `dram_mj` | -1.55%      | 0.00e+00  | -0.345    | small      | ✅   |
| `time_s`  | -0.06%      | 5.19e-14  | -0.020    | negligible | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`ane_mj`**: 320759.0% higher energy (Cohen’s d = -0.475, small)
- **`dram_mj`**: 1.6% higher energy (Cohen’s d = -0.345, small)

> Verdict percentages describe the change relative to the with-smell mean.
