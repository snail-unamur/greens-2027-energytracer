## Energy Report — `carbon` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-5-238.eu-west-1.compute.internal`
- **model**: `c8a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R45`

### Global Consumption

| Metric                    | With smell  | Without smell |
| ------------------------- | ----------- | ------------- |
| **Median Execution Time** | 94.87 ms    | 6.11 ms       |
| **Average Power**         | 11.401 W    | 11.585 W      |
| **Total Energy**          | 324548.01 J | 21169.71 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 163.564 mJ          | 28.697 mJ        | 10.610 mJ              | 0.304 mJ            |
| `gpu_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `co2_eq`  | 0.000 mg CO2eq      | 0.000 mg CO2eq   | 0.000 mg CO2eq         | 0.000 mg CO2eq      |
| `dram_mj` | 917.979 mJ          | 161.769 mJ       | 60.238 mJ              | 0.613 mJ            |
| `time_s`  | 0.095 s             | 0.017 s          | 0.006 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299852 | 0.9052      | 2.60e-48 | Rejected     |
| `cpu_mj`  | Without smell | 290199 | 0.4507      | 3.40e-82 | Rejected     |
| `gpu_mj`  | With smell    | 300000 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 300000 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299855 | 0.9058      | 3.30e-48 | Rejected     |
| `co2_eq`  | Without smell | 290199 | 0.3795      | 6.93e-85 | Rejected     |
| `dram_mj` | With smell    | 299857 | 0.9048      | 2.19e-48 | Rejected     |
| `dram_mj` | Without smell | 290199 | 0.3780      | 6.11e-85 | Rejected     |
| `time_s`  | With smell    | 299856 | 0.9075      | 6.58e-48 | Rejected     |
| `time_s`  | Without smell | 290199 | 0.3778      | 6.01e-85 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +93.51%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `co2_eq`  | +93.45%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +93.44%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.56%  | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`co2_eq`**: 93.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 93.4% lower median energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.6% lower median time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell median.
