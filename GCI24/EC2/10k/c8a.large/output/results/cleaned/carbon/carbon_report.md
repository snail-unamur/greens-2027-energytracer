## Energy Report — `carbon` (cleaned)

> 299857 samples (with smell) vs 290199 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-5-238.eu-west-1.compute.internal`
- **model**: `c8a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R45`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 94.93 ms    | 5.96 ms       |
| **Average Power**  | 11.401 W    | 11.585 W      |
| **Total Energy**   | 324533.79 J | 20025.77 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 163.681 mJ        | 10.707 mJ            |
| `gpu_mj`  | 0.000 mJ          | 0.000 mJ             |
| `co2_eq`  | 0.000 mg CO2eq    | 0.000 mg CO2eq       |
| `dram_mj` | 918.655 mJ        | 61.014 mJ            |
| `time_s`  | 0.095 s           | 0.006 s              |

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299844 | 0.9073      | 6.14e-48 | Rejected     |
| `cpu_mj`  | Without smell | 279263 | 0.5619      | 2.57e-77 | Rejected     |
| `gpu_mj`  | With smell    | 299857 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 290199 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299846 | 0.9049      | 2.28e-48 | Rejected     |
| `co2_eq`  | Without smell | 279172 | 0.4068      | 6.90e-84 | Rejected     |
| `dram_mj` | With smell    | 299846 | 0.9049      | 2.26e-48 | Rejected     |
| `dram_mj` | Without smell | 279211 | 0.4128      | 1.16e-83 | Rejected     |
| `time_s`  | With smell    | 299846 | 0.9049      | 2.27e-48 | Rejected     |
| `time_s`  | Without smell | 279210 | 0.4169      | 1.65e-83 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | ------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +93.46% | 0.00e+00                 | 1.000            | large  | ✅   |
| `co2_eq`  | +93.37% | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +93.36% | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.48% | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_with × 100. Positive → the smell consumes more energy. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.5% lower energy (Vargha-Delaney A = 1.000, large)
- **`co2_eq`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.5% lower time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell mean.
