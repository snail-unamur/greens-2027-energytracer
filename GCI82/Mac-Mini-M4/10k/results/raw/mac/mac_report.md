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
| **Median Execution Time** | 18.77 ms   | 18.80 ms      |
| **Average Power**         | 6.839 W    | 6.856 W       |
| **Total Energy**          | 37776.88 J | 37882.55 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 125.022 mJ          | 2.994 mJ         | 125.179 mJ             | 3.173 mJ            |
| `gpu_mj`  | 1.369 mJ            | 0.033 mJ         | 1.370 mJ               | 0.032 mJ            |
| `ane_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `dram_mj` | 2.001 mJ            | 0.052 mJ         | 2.006 mJ               | 0.089 mJ            |
| `time_s`  | 0.019 s             | 0.000 s          | 0.019 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 0.0% (0 not rejected, 10 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result   |
| --------- | ------------- | ------ | ----------- | -------- | -------- |
| `cpu_mj`  | With smell    | 292757 | 0.8563      | 1.68e-55 | Rejected |
| `cpu_mj`  | Without smell | 292795 | 0.8579      | 2.66e-55 | Rejected |
| `gpu_mj`  | With smell    | 293142 | 0.8525      | 5.66e-56 | Rejected |
| `gpu_mj`  | Without smell | 292910 | 0.8607      | 5.97e-55 | Rejected |
| `ane_mj`  | With smell    | 290000 | 0.1721      | 1.98e-91 | Rejected |
| `ane_mj`  | Without smell | 289962 | 0.3554      | 9.77e-86 | Rejected |
| `dram_mj` | With smell    | 295262 | 0.8558      | 1.44e-55 | Rejected |
| `dram_mj` | Without smell | 297499 | 0.7955      | 5.23e-62 | Rejected |
| `time_s`  | With smell    | 293012 | 0.8618      | 8.13e-55 | Rejected |
| `time_s`  | Without smell | 292926 | 0.8650      | 2.16e-54 | Rejected |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | -0.13%   | 4.15e-275                | 0.473            | small  | ✅   |
| `gpu_mj`  | -0.06%   | 1.42e-58                 | 0.488            | small  | ✅   |
| `ane_mj`  | N/A      | 0.00e+00                 | 0.430            | small  | ✅   |
| `dram_mj` | -0.24%   | 0.00e+00                 | 0.446            | small  | ✅   |
| `time_s`  | -0.15%   | 3.79e-27                 | 0.492            | small  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 0.1% higher median energy (Vargha-Delaney A = 0.473, small)
- **`gpu_mj`**: 0.1% higher median energy (Vargha-Delaney A = 0.488, small)
- **`ane_mj`**: no change in median energy (Vargha-Delaney A = 0.430, small)
- **`dram_mj`**: 0.2% higher median energy (Vargha-Delaney A = 0.446, small)
- **`time_s`**: 0.2% higher median time (Vargha-Delaney A = 0.492, small)

> Verdict percentages describe the change relative to the with-smell median.
