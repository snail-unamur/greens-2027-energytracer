## Energy Report — `mac` (cleaned)

> 299999 samples (with smell) vs 290170 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric                    | With smell  | Without smell |
| ------------------------- | ----------- | ------------- |
| **Median Execution Time** | 62.90 ms    | 4.32 ms       |
| **Average Power**         | 6.139 W     | 6.131 W       |
| **Total Energy**          | 116389.38 J | 7437.22 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 346.712 mJ          | 46.166 mJ        | 24.317 mJ              | 2.197 mJ            |
| `gpu_mj`  | 5.435 mJ            | 0.678 mJ         | 0.370 mJ               | 0.054 mJ            |
| `ane_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `dram_mj` | 34.006 mJ           | 4.598 mJ         | 1.735 mJ               | 0.044 mJ            |
| `time_s`  | 0.063 s             | 0.008 s          | 0.004 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299999 | 0.9026      | 9.16e-49 | Rejected     |
| `cpu_mj`  | Without smell | 276181 | 0.8945      | 4.05e-50 | Rejected     |
| `gpu_mj`  | With smell    | 299999 | 0.9899      | 2.15e-18 | Rejected     |
| `gpu_mj`  | Without smell | 284628 | 0.9654      | 4.79e-33 | Rejected     |
| `ane_mj`  | With smell    | 299999 | 1.0000      | 1.0000   | Not rejected |
| `ane_mj`  | Without smell | 290170 | 1.0000      | 1.0000   | Not rejected |
| `dram_mj` | With smell    | 299999 | 0.8896      | 6.91e-51 | Rejected     |
| `dram_mj` | Without smell | 279636 | 0.6074      | 5.25e-75 | Rejected     |
| `time_s`  | With smell    | 299999 | 0.8941      | 3.55e-50 | Rejected     |
| `time_s`  | Without smell | 279442 | 0.5851      | 3.62e-76 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +92.99%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `gpu_mj`  | +93.20%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +94.90%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.14%  | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.0% lower median energy (Vargha-Delaney A = 1.000, large)
- **`gpu_mj`**: 93.2% lower median energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 94.9% lower median energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.1% lower median time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell median.
