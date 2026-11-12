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
| `dram_mj` | 34.165 mJ         | 1.767 mJ             |
| `time_s`  | 0.063 s           | 0.004 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions)

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 299999 | 0.9026      | 9.16e-49 | Rejected |
| `cpu_mj`  | Without smell | 290170 | 0.7029      | 2.67e-69 | Rejected |
| `gpu_mj`  | With smell    | 299999 | 0.9899      | 2.15e-18 | Rejected |
| `gpu_mj`  | Without smell | 290170 | 0.9012      | 5.23e-49 | Rejected |
| `dram_mj` | With smell    | 299999 | 0.8896      | 6.91e-51 | Rejected |
| `dram_mj` | Without smell | 290170 | 0.4937      | 2.03e-80 | Rejected |
| `time_s`  | With smell    | 299999 | 0.8941      | 3.55e-50 | Rejected |
| `time_s`  | Without smell | 290170 | 0.4762      | 3.69e-81 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value  | Cohen’s d | Effect | Sig. |
| --------- | ------- | -------- | --------- | ------ | ---- |
| `cpu_mj`  | +92.76% | 0.00e+00 | +21.419   | large  | ✅   |
| `gpu_mj`  | +93.14% | 0.00e+00 | +14.506   | large  | ✅   |
| `dram_mj` | +94.83% | 0.00e+00 | +22.059   | large  | ✅   |
| `time_s`  | +93.04% | 0.00e+00 | +21.578   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 92.8% lower energy (Cohen’s d = +21.419, large)
- **`gpu_mj`**: 93.1% lower energy (Cohen’s d = +14.506, large)
- **`dram_mj`**: 94.8% lower energy (Cohen’s d = +22.059, large)
- **`time_s`**: 93.0% lower time (Cohen’s d = +21.578, large)

> Verdict percentages describe the change relative to the with-smell mean.
