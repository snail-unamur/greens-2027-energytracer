## Energy Report — `carbon` (raw)

> 300000 samples (with smell) vs 300000 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-42-236.eu-west-1.compute.internal`
- **model**: `m7a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R14`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 116.58 ms   | 7.34 ms       |
| **Average Power**  | 11.518 W    | 11.678 W      |
| **Total Energy**   | 402831.00 J | 25720.11 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 214.630 mJ        | 14.080 mJ            |
| `gpu_mj`  | 0.000 mJ          | 0.000 mJ             |
| `co2_eq`  | 0.000 mg CO2eq    | 0.000 mg CO2eq       |
| `dram_mj` | 1129.822 mJ       | 74.556 mJ            |
| `time_s`  | 0.117 s           | 0.008 s              |

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299623 | 0.9335      | 1.34e-42 | Rejected     |
| `cpu_mj`  | Without smell | 290175 | 0.5396      | 2.25e-78 | Rejected     |
| `gpu_mj`  | With smell    | 300000 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 300000 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299626 | 0.9268      | 4.21e-44 | Rejected     |
| `co2_eq`  | Without smell | 290177 | 0.4376      | 1.04e-82 | Rejected     |
| `dram_mj` | With smell    | 299625 | 0.9194      | 1.21e-45 | Rejected     |
| `dram_mj` | Without smell | 290177 | 0.4366      | 9.45e-83 | Rejected     |
| `time_s`  | With smell    | 299627 | 0.9243      | 1.22e-44 | Rejected     |
| `time_s`  | Without smell | 290177 | 0.4361      | 8.99e-83 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Mann-Whitney U / Vargha-Delaney A results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value (Mann-Whitney U) | Vargha-Delaney A | Effect | Sig. |
| --------- | ------- | ------------------------ | ---------------- | ------ | ---- |
| `cpu_mj`  | +93.44% | 0.00e+00                 | 1.000            | large  | ✅   |
| `co2_eq`  | +93.41% | 0.00e+00                 | 1.000            | large  | ✅   |
| `dram_mj` | +93.40% | 0.00e+00                 | 1.000            | large  | ✅   |
| `time_s`  | +93.50% | 0.00e+00                 | 1.000            | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_with × 100. Positive → the smell consumes more energy. A = P(with-smell value > without-smell value) + 0.5 × P(tie).

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`co2_eq`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`dram_mj`**: 93.4% lower energy (Vargha-Delaney A = 1.000, large)
- **`time_s`**: 93.5% lower time (Vargha-Delaney A = 1.000, large)

> Verdict percentages describe the change relative to the with-smell mean.
