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
| **Execution Time** | 8.58 ms    | 3.83 ms       |
| **Average Power**  | 6.355 W    | 6.267 W       |
| **Total Energy**   | 16352.44 J | 7202.14 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 53.783 mJ         | 23.598 mJ            |
| `gpu_mj`  | 0.272 mJ          | 0.119 mJ             |
| `dram_mj` | 0.649 mJ          | 0.304 mJ             |
| `time_s`  | 0.009 s           | 0.004 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 298928 | 0.9780      | 3.68e-27 | Rejected |
| `cpu_mj`  | Without smell | 299958 | 0.8969      | 1.01e-49 | Rejected |
| `gpu_mj`  | With smell    | 298947 | 0.9858      | 5.27e-22 | Rejected |
| `gpu_mj`  | Without smell | 299984 | 0.9345      | 2.28e-42 | Rejected |
| `dram_mj` | With smell    | 298933 | 0.9942      | 2.65e-13 | Rejected |
| `dram_mj` | Without smell | 289984 | 0.9926      | 1.65e-15 | Rejected |
| `time_s`  | With smell    | 298931 | 0.9531      | 2.59e-37 | Rejected |
| `time_s`  | Without smell | 299252 | 0.9819      | 8.57e-25 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value  | Cohen’s d | Effect | Sig. |
| --------- | ------- | -------- | --------- | ------ | ---- |
| `cpu_mj`  | +56.12% | 0.00e+00 | +47.009   | large  | ✅   |
| `gpu_mj`  | +56.19% | 0.00e+00 | +21.744   | large  | ✅   |
| `dram_mj` | +53.15% | 0.00e+00 | +29.664   | large  | ✅   |
| `time_s`  | +55.38% | 0.00e+00 | +73.988   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 56.1% lower energy (Cohen’s d = +47.009, large)
- **`gpu_mj`**: 56.2% lower energy (Cohen’s d = +21.744, large)
- **`dram_mj`**: 53.2% lower energy (Cohen’s d = +29.664, large)
- **`time_s`**: 55.4% lower time (Cohen’s d = +73.988, large)

> Verdict percentages describe the change relative to the with-smell mean.
