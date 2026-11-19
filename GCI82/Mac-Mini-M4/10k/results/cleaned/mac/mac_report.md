## Energy Report — `mac` (cleaned)

> 293868 samples (with smell) vs 293823 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `mac-mini-server`
- **model**: `Mac16,10`
- **os**: `Darwin 25.3.0`
- **machine**: `arm64`
- **chip**: `Apple M4`

### Global Consumption

| Metric                    | With smell | Without smell |
| ------------------------- | ---------- | ------------- |
| **Median Execution Time** | 18.75 ms   | 18.78 ms      |
| **Average Power**         | 6.835 W    | 6.856 W       |
| **Total Energy**          | 36748.70 J | 36876.79 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 124.959 mJ          | 2.878 mJ         | 125.113 mJ             | 3.078 mJ            |
| `gpu_mj`  | 1.368 mJ            | 0.032 mJ         | 1.369 mJ               | 0.031 mJ            |
| `ane_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `dram_mj` | 1.999 mJ            | 0.048 mJ         | 2.005 mJ               | 0.079 mJ            |
| `time_s`  | 0.019 s             | 0.000 s          | 0.019 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 0.0% (0 not rejected, 10 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 285495 | 0.9105      | 2.28e-47 | Rejected |
| `cpu_mj`  | Without smell | 285687 | 0.9151      | 1.71e-46 | Rejected |
| `gpu_mj`  | With smell    | 285956 | 0.9126      | 5.60e-47 | Rejected |
| `gpu_mj`  | Without smell | 285824 | 0.9116      | 3.76e-47 | Rejected |
| `ane_mj`  | With smell    | 284091 | 0.1720      | 1.96e-91 | Rejected |
| `ane_mj`  | Without smell | 284032 | 0.3552      | 9.57e-86 | Rejected |
| `dram_mj` | With smell    | 288322 | 0.8715      | 1.62e-53 | Rejected |
| `dram_mj` | Without smell | 291548 | 0.7963      | 6.18e-62 | Rejected |
| `time_s`  | With smell    | 285887 | 0.9149      | 1.53e-46 | Rejected |
| `time_s`  | Without smell | 285841 | 0.9096      | 1.58e-47 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | -0.12%   | 1.57e-301                | 0.472            | small  | ✅   |
| `gpu_mj`  | -0.07%   | 1.47e-64                 | 0.487            | small  | ✅   |
| `ane_mj`  | N/A      | 0.00e+00                 | 0.430            | small  | ✅   |
| `dram_mj` | -0.30%   | 0.00e+00                 | 0.444            | small  | ✅   |
| `time_s`  | -0.14%   | 1.24e-29                 | 0.491            | small  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 0.1% higher median energy (Vargha-Delaney A = 0.472, small)
- **`gpu_mj`**: 0.1% higher median energy (Vargha-Delaney A = 0.487, small)
- **`ane_mj`**: no change in median energy (Vargha-Delaney A = 0.430, small)
- **`dram_mj`**: 0.3% higher median energy (Vargha-Delaney A = 0.444, small)
- **`time_s`**: 0.1% higher median time (Vargha-Delaney A = 0.491, small)

> Verdict percentages describe the change relative to the with-smell median.
