## Energy Report — `mac` (cleaned)

> 295282 samples (with smell) vs 297176 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric                    | With smell | Without smell |
| ------------------------- | ---------- | ------------- |
| **Median Execution Time** | 8.61 ms    | 3.84 ms       |
| **Average Power**         | 6.356 W    | 6.323 W       |
| **Total Energy**          | 16120.71 J | 7138.71 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 53.687 mJ           | 0.876 mJ         | 23.895 mJ              | 1.257 mJ            |
| `gpu_mj`  | 0.273 mJ            | 0.010 mJ         | 0.120 mJ               | 0.010 mJ            |
| `ane_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `dram_mj` | 0.647 mJ            | 0.019 mJ         | 0.303 mJ               | 0.011 mJ            |
| `time_s`  | 0.009 s             | 0.000 s          | 0.004 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 294566 | 0.9773      | 1.57e-27 | Rejected     |
| `cpu_mj`  | Without smell | 297168 | 0.8825      | 5.71e-52 | Rejected     |
| `gpu_mj`  | With smell    | 294578 | 0.9848      | 9.11e-23 | Rejected     |
| `gpu_mj`  | Without smell | 297176 | 0.9335      | 1.34e-42 | Rejected     |
| `ane_mj`  | With smell    | 295282 | 1.0000      | 1.0000   | Not rejected |
| `ane_mj`  | Without smell | 297176 | 1.0000      | 1.0000   | Not rejected |
| `dram_mj` | With smell    | 294569 | 0.9928      | 3.05e-15 | Rejected     |
| `dram_mj` | Without smell | 287383 | 0.9905      | 8.46e-18 | Rejected     |
| `time_s`  | With smell    | 294566 | 0.9863      | 1.23e-21 | Rejected     |
| `time_s`  | Without smell | 293831 | 0.9976      | 3.47e-07 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +55.49%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `gpu_mj`  | +56.05%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +53.17%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +55.36%  | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 55.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`gpu_mj`**: 56.0% lower median energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 53.2% lower median energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 55.4% lower median time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell median.
