## Energy Report — `mac` (raw)
> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05
### Instance Info
* **hostname**: `jerome-ThinkBook-14s-Yoga-ITL`
* **model**: `20WE`
* **os**: `Linux 6.8.0-40-generic`
* **machine**: `x86_64`
* **chip**: `11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz`
### Global Consumption
| Metric | With smell | Without smell |
| --- | --- | --- |
| **Execution Time** | 8.58 ms | 3.83 ms |
| **Average Power** | 6.355 W | 6.267 W |
| **Total Energy** | 16352.44 J | 7202.14 J |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.
### Mean Values
| Metric | Mean (with smell) | Mean (without smell) |
| --- | --- | --- |
| `cpu_mj` | 53.783 mJ | 23.598 mJ |
| `gpu_mj` | 0.272 mJ | 0.119 mJ |
| `ane_mj` | 0.000 mJ | 0.000 mJ |
| `dram_mj` | 0.649 mJ | 0.304 mJ |
| `time_s` | 0.009 s | 0.004 s |
### Statistical Analysis
Welch's test was undefined for: `ane_mj`.

| Metric | Δ mean | p-value | Cohen’s d | Effect | Sig. |
| --- | --- | --- | --- | --- | --- |
| `cpu_mj` | +127.92% | 9.00008334e-818295 (log-space) | +47.009 | large | ✅ |
| `gpu_mj` | +128.27% | 7.89156372e-609762 (log-space) | +21.744 | large | ✅ |
| `dram_mj` | +113.46% | 2.86035636e-563990 (log-space) | +29.664 | large | ✅ |
| `time_s` | +124.12% | 1.25303084e-798986 (log-space) | +73.988 | large | ✅ |
> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.
### Verdict
Removing the code smell leads to measurable energy differences:

* **`cpu_mj`**: 56.1% lower energy (Cohen’s d = +47.009, large)
* **`gpu_mj`**: 56.2% lower energy (Cohen’s d = +21.744, large)
* **`dram_mj`**: 53.2% lower energy (Cohen’s d = +29.664, large)
* **`time_s`**: 55.4% lower time (Cohen’s d = +73.988, large)

> Verdict percentages describe the change relative to the with-smell mean.
