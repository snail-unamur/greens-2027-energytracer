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
| `dram_mj` | 34.165 mJ         | 1.744 mJ             |
| `time_s`  | 0.063 s           | 0.004 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions)

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 299999 | 0.9026      | 9.16e-49 | Rejected |
| `cpu_mj`  | Without smell | 276181 | 0.8945      | 4.05e-50 | Rejected |
| `gpu_mj`  | With smell    | 299999 | 0.9899      | 2.15e-18 | Rejected |
| `gpu_mj`  | Without smell | 284628 | 0.9654      | 4.79e-33 | Rejected |
| `dram_mj` | With smell    | 299999 | 0.8896      | 6.91e-51 | Rejected |
| `dram_mj` | Without smell | 279636 | 0.6074      | 5.25e-75 | Rejected |
| `time_s`  | With smell    | 299999 | 0.8941      | 3.55e-50 | Rejected |
| `time_s`  | Without smell | 279442 | 0.5851      | 3.62e-76 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value  | Cohen’s d | Effect | Sig. |
| --------- | ------- | -------- | --------- | ------ | ---- |
| `cpu_mj`  | +92.89% | 0.00e+00 | +21.532   | large  | ✅   |
| `gpu_mj`  | +93.21% | 0.00e+00 | +14.534   | large  | ✅   |
| `dram_mj` | +94.90% | 0.00e+00 | +22.113   | large  | ✅   |
| `time_s`  | +93.13% | 0.00e+00 | +21.667   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 92.9% lower energy (Cohen’s d = +21.532, large)
- **`gpu_mj`**: 93.2% lower energy (Cohen’s d = +14.534, large)
- **`dram_mj`**: 94.9% lower energy (Cohen’s d = +22.113, large)
- **`time_s`**: 93.1% lower time (Cohen’s d = +21.667, large)

> Verdict percentages describe the change relative to the with-smell mean.
