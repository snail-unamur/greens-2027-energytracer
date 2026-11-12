## Energy Report — `mac` (cleaned)

> 295282 samples (with smell) vs 297176 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric             | With smell | Without smell |
| ------------------ | ---------- | ------------- |
| **Execution Time** | 8.59 ms    | 3.80 ms       |
| **Average Power**  | 6.356 W    | 6.323 W       |
| **Total Energy**   | 16120.71 J | 7138.71 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 53.806 mJ         | 23.609 mJ            |
| `gpu_mj`  | 0.272 mJ          | 0.119 mJ             |
| `dram_mj` | 0.649 mJ          | 0.304 mJ             |
| `time_s`  | 0.009 s           | 0.004 s              |

### Normality (Shapiro-Wilk)

Normality rate: 0% (0 not rejected, 8 rejected out of 8 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 294566 | 0.9773      | 1.57e-27 | Rejected |
| `cpu_mj`  | Without smell | 297168 | 0.8825      | 5.71e-52 | Rejected |
| `gpu_mj`  | With smell    | 294578 | 0.9848      | 9.11e-23 | Rejected |
| `gpu_mj`  | Without smell | 297176 | 0.9335      | 1.34e-42 | Rejected |
| `dram_mj` | With smell    | 294569 | 0.9928      | 3.05e-15 | Rejected |
| `dram_mj` | Without smell | 287383 | 0.9905      | 8.46e-18 | Rejected |
| `time_s`  | With smell    | 294566 | 0.9863      | 1.23e-21 | Rejected |
| `time_s`  | Without smell | 293831 | 0.9976      | 3.47e-07 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value  | Cohen’s d | Effect | Sig. |
| --------- | ------- | -------- | --------- | ------ | ---- |
| `cpu_mj`  | +56.12% | 0.00e+00 | +48.875   | large  | ✅   |
| `gpu_mj`  | +56.20% | 0.00e+00 | +21.811   | large  | ✅   |
| `dram_mj` | +53.16% | 0.00e+00 | +30.158   | large  | ✅   |
| `time_s`  | +55.38% | 0.00e+00 | +80.983   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 56.1% lower energy (Cohen’s d = +48.875, large)
- **`gpu_mj`**: 56.2% lower energy (Cohen’s d = +21.811, large)
- **`dram_mj`**: 53.2% lower energy (Cohen’s d = +30.158, large)
- **`time_s`**: 55.4% lower time (Cohen’s d = +80.983, large)

> Verdict percentages describe the change relative to the with-smell mean.
