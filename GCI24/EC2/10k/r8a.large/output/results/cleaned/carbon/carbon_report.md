## Energy Report — `carbon` (cleaned)

> 299867 samples (with smell) vs 290167 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-26-83.eu-west-1.compute.internal`
- **model**: `r8a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R45`

### Global Consumption

| Metric                    | With smell  | Without smell |
| ------------------------- | ----------- | ------------- |
| **Median Execution Time** | 95.97 ms    | 6.12 ms       |
| **Average Power**         | 11.416 W    | 11.580 W      |
| **Total Energy**          | 328323.84 J | 20065.72 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Median Values and IQR

| Metric    | Median (with smell) | IQR (with smell) | Median (without smell) | IQR (without smell) |
| --------- | ------------------- | ---------------- | ---------------------- | ------------------- |
| `cpu_mj`  | 165.278 mJ          | 28.679 mJ        | 10.607 mJ              | 0.212 mJ            |
| `gpu_mj`  | 0.000 mJ            | 0.000 mJ         | 0.000 mJ               | 0.000 mJ            |
| `co2_eq`  | 0.000 mg CO2eq      | 0.000 mg CO2eq   | 0.000 mg CO2eq         | 0.000 mg CO2eq      |
| `dram_mj` | 929.883 mJ          | 160.968 mJ       | 60.289 mJ              | 0.739 mJ            |
| `time_s`  | 0.096 s             | 0.017 s          | 0.006 s                | 0.000 s             |

> IQR = 75th percentile − 25th percentile (linear interpolation).

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299848 | 0.9164      | 3.09e-46 | Rejected     |
| `cpu_mj`  | Without smell | 278684 | 0.5517      | 8.27e-78 | Rejected     |
| `gpu_mj`  | With smell    | 299867 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 290167 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299857 | 0.9225      | 5.20e-45 | Rejected     |
| `co2_eq`  | Without smell | 278987 | 0.4141      | 1.29e-83 | Rejected     |
| `dram_mj` | With smell    | 299858 | 0.9161      | 2.68e-46 | Rejected     |
| `dram_mj` | Without smell | 279063 | 0.4094      | 8.64e-84 | Rejected     |
| `time_s`  | With smell    | 299854 | 0.9106      | 2.45e-47 | Rejected     |
| `time_s`  | Without smell | 279065 | 0.3999      | 3.81e-84 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ median | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | -------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +93.58%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `co2_eq`  | +93.53%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +93.52%  | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.63%  | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ median = (median_with − median_without) / median_with × 100. For a positive with-smell median, positive → it is higher. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.6% lower median energy (Vargha-Delaney A = 1.000, large)
- **`co2_eq`**: 93.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 93.5% lower median energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.6% lower median time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell median.
