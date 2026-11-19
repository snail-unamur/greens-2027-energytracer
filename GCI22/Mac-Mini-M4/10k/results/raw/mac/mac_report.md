## Energy Report — `mac` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

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
| **Average Power**         | 6.355 W    | 6.267 W       |
| **Total Energy**          | 16352.44 J | 7202.14 J     |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 53.678 mJ           | 0.882 mJ         | 23.886 mJ              | 1.262 mJ            |
| `gpu_mj`  | 0.273 mJ            | 0.010 mJ         | 0.120 mJ               | 0.010 mJ            |
| `ane_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `dram_mj` | 0.647 mJ            | 0.019 mJ         | 0.303 mJ               | 0.011 mJ            |
| `time_s`  | 0.009 s             | 0.000 s          | 0.004 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 298928 | 0.9780      | 3.68e-27 | Rejected     |
| `cpu_mj`  | Without smell | 299958 | 0.8969      | 1.01e-49 | Rejected     |
| `gpu_mj`  | With smell    | 298947 | 0.9858      | 5.27e-22 | Rejected     |
| `gpu_mj`  | Without smell | 299984 | 0.9345      | 2.28e-42 | Rejected     |
| `ane_mj`  | With smell    | 300000 | 1.0000      | 1.0000   | Not rejected |
| `ane_mj`  | Without smell | 300000 | 1.0000      | 1.0000   | Not rejected |
| `dram_mj` | With smell    | 298933 | 0.9942      | 2.65e-13 | Rejected     |
| `dram_mj` | Without smell | 289984 | 0.9926      | 1.65e-15 | Rejected     |
| `time_s`  | With smell    | 298931 | 0.9531      | 2.59e-37 | Rejected     |
| `time_s`  | Without smell | 299252 | 0.9819      | 8.57e-25 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +55.50%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `gpu_mj`  | +56.03%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +53.16%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +55.37%  | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 55.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`gpu_mj`**: 56.0% lower median energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 53.2% lower median energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 55.4% lower median time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell median.
