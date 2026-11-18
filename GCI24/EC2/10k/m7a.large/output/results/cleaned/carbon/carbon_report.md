## Energy Report — `carbon` (cleaned)

> 299624 samples (with smell) vs 290177 samples (without smell) — α = 0.05

### Instance Info

- **hostname**: `ip-172-31-42-236.eu-west-1.compute.internal`
- **model**: `m7a.large`
- **os**: `Linux 6.1.163-186.299.amzn2023.x86_64`
- **machine**: `x86_64`
- **chip**: `AMD EPYC 9R14`

### Global Consumption

| Metric             | With smell  | Without smell |
| ------------------ | ----------- | ------------- |
| **Execution Time** | 116.71 ms   | 7.14 ms       |
| **Average Power**  | 11.518 W    | 11.688 W      |
| **Total Energy**   | 402781.34 J | 24202.61 J    |

> The total energy is the sum of measurements across all iterations, converted to joules (J). If you ran the ./run_experiment.sh script, this reflects the cumulative energy of all 30 iterations of the process.

### Mean Values

| Metric    | Mean (with smell) | Mean (without smell) |
| --------- | ----------------- | -------------------- |
| `cpu_mj`  | 214.624 mJ        | 13.849 mJ            |
| `gpu_mj`  | 0.000 mJ          | 0.000 mJ             |
| `co2_eq`  | 0.000 mg CO2eq    | 0.000 mg CO2eq       |
| `dram_mj` | 1129.795 mJ       | 73.248 mJ            |
| `time_s`  | 0.117 s           | 0.007 s              |

### Normality (Shapiro-Wilk)

Normality rate: 20.0% (2 not rejected, 8 rejected out of 10 tested distributions).

| Metric    | Group         | N      | W statistic | p-value  | Result       |
| --------- | ------------- | ------ | ----------- | -------- | ------------ |
| `cpu_mj`  | With smell    | 299590 | 0.9285      | 9.75e-44 | Rejected     |
| `cpu_mj`  | Without smell | 278899 | 0.6956      | 8.66e-70 | Rejected     |
| `gpu_mj`  | With smell    | 299624 | 1.0000      | 1.0000   | Not rejected |
| `gpu_mj`  | Without smell | 290177 | 1.0000      | 1.0000   | Not rejected |
| `co2_eq`  | With smell    | 299600 | 0.9256      | 2.28e-44 | Rejected     |
| `co2_eq`  | Without smell | 277622 | 0.5037      | 5.45e-80 | Rejected     |
| `dram_mj` | With smell    | 299596 | 0.9230      | 6.37e-45 | Rejected     |
| `dram_mj` | Without smell | 277691 | 0.5028      | 4.99e-80 | Rejected     |
| `time_s`  | With smell    | 299597 | 0.9239      | 1.03e-44 | Rejected     |
| `time_s`  | Without smell | 277681 | 0.4990      | 3.42e-80 | Rejected     |

> At α = 0.05, 'Not rejected' means Shapiro-Wilk found no evidence against normality (H₀: the sample is normally distributed); it does not prove the data are normal. These results do not change which test is applied below — use them to judge how much to trust the Welch's t-test / Cohen’s d results for that metric.

### Statistical Analysis

| Metric    | Δ mean  | p-value  | Cohen’s d | Effect | Sig. |
| --------- | ------- | -------- | --------- | ------ | ---- |
| `cpu_mj`  | +93.55% | 0.00e+00 | +16.042   | large  | ✅   |
| `co2_eq`  | +93.52% | 0.00e+00 | +16.095   | large  | ✅   |
| `dram_mj` | +93.52% | 0.00e+00 | +16.098   | large  | ✅   |
| `time_s`  | +93.61% | 0.00e+00 | +16.109   | large  | ✅   |

> Δ mean = (mean_with − mean_without) / mean_without × 100. Positive → the smell consumes more energy.

### Verdict

Removing the code smell leads to measurable energy differences:

- **`cpu_mj`**: 93.5% lower energy (Cohen’s d = +16.042, large)
- **`co2_eq`**: 93.5% lower energy (Cohen’s d = +16.095, large)
- **`dram_mj`**: 93.5% lower energy (Cohen’s d = +16.098, large)
- **`time_s`**: 93.6% lower time (Cohen’s d = +16.109, large)

> Verdict percentages describe the change relative to the with-smell mean.
