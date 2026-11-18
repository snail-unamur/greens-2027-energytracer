## Energy Report — `carbon` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-26-83.eu-west-1.compute.internal`
- **model**: `r8a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R45`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 95.87 ms    | 6.11 ms       |
| **Average Power**  | 11.416 W    | 11.584 W      |
| **Total Energy**   | 328338.42 J | 21224.32 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 165.196 mJ        | 10.908 mJ            |
| `gpu_mj`  | 0.000 mJ          | 0.000 mJ             |
| `co2_eq`  | 0.000 mg CO2eq    | 0.000 mg CO2eq       |
| `dram_mj` | 929.750 mJ        | 62.237 mJ            |
| `time_s`  | 0.096 s           | 0.006 s              |

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299857 | 0.9154      | 1.93e-46 | Rejected     |
| `cpu_mj`  | Without smell | 290167 | 0.4452      | 2.05e-82 | Rejected     |
| `gpu_mj`  | With smell    | 300000 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 300000 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299870 | 0.9124      | 5.15e-47 | Rejected     |
| `co2_eq`  | Without smell | 290167 | 0.3911      | 1.81e-84 | Rejected     |
| `dram_mj` | With smell    | 299869 | 0.9207      | 2.15e-45 | Rejected     |
| `dram_mj` | Without smell | 290167 | 0.3898      | 1.62e-84 | Rejected     |
| `time_s`  | With smell    | 299865 | 0.9125      | 5.43e-47 | Rejected     |
| `time_s`  | Without smell | 290167 | 0.3895      | 1.59e-84 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | ------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +93.40% | 0.00e+00                 | 1.000            | large  | ✅   |
| `co2_eq`  | +93.32% | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +93.31% | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.42% | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_with × 100. Positive → the smell consumes more energy. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`co2_eq`**: 93.3% lower energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 93.3% lower energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.4% lower time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell mean.
