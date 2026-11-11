## Energy Report — `mac` (cleaned)
> 295282 samples (with smell) vs 297176 samples (without smell) — α = 0.05
### Instance Info
* **hostname**: `jerome-ThinkBook-14s-Yoga-ITL`
* **model**: `20WE`
* **os**: `Linux 6.8.0-40-generic`
* **machine**: `x86_64`
* **chip**: `11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz`
### Global Consumption
| Metric | With smell | Without smell |
| --- | --- | --- |
| **Execution Time** | 8.59 ms | 3.80 ms |
| **Average Power** | 6.356 W | 6.323 W |
| **Total Energy** | 16120.71 J | 7138.71 J |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.
### Mean Values
| Metric | Mean (with smell) | Mean (without smell) |
| --- | --- | --- |
| `cpu_mj` | 53.806 mJ | 23.609 mJ |
| `gpu_mj` | 0.272 mJ | 0.119 mJ |
| `ane_mj` | 0.000 mJ | 0.000 mJ |
| `dram_mj` | 0.649 mJ | 0.304 mJ |
| `time_s` | 0.009 s | 0.004 s |
### Statistical Analysis
Welch's test was undefined for: `ane_mj`.

| Metric | Δ mean | p-value | Cohen’s d | Effect | Sig. |
| --- | --- | --- | --- | --- | --- |
| `cpu_mj` | +127.90% | 1.29589017e-813690 (log-space) | +48.875 | large | ✅ |
| `gpu_mj` | +128.31% | 8.13594550e-602727 (log-space) | +21.811 | large | ✅ |
| `dram_mj` | +113.50% | 4.90872830e-559781 (log-space) | +30.158 | large | ✅ |
| `time_s` | +124.09% | 4.10889935e-802019 (log-space) | +80.983 | large | ✅ |
> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.
### Verdict
Removing the code smell leads to measurable energy differences:

* **`cpu_mj`**: 56.1% lower energy (Cohen’s d = +48.875, large)
* **`gpu_mj`**: 56.2% lower energy (Cohen’s d = +21.811, large)
* **`dram_mj`**: 53.2% lower energy (Cohen’s d = +30.158, large)
* **`time_s`**: 55.4% lower time (Cohen’s d = +80.983, large)

> Verdict percentages describe the change relative to the with-smell mean.
