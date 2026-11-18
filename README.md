# Replication package of EnergyTracer

This upload includes the energy measurement results collected using the EnergyTracer pipeline, supporting the paper submitted to the 11th International Workshop on Green and Sustainable Software (GREENS'27), co-located with ICSE 2027.

## Data directory structure

For each GCI rule, EnergyTracer stores the two code variants at the root of the corresponding directory (`GCIxx/`). Results are grouped by machine (`Mac-Mini-M4` or `EC2`), workload (`10k`), and profiler (`mac`, for the _zeus-apple-silicon_ profiler and `carbon` for the _CodeCarbon_ profiler). In the case of `EC2` representing an AWS service allowing to use virtual machine, three instances were used: `c8a.large`, `m7a.large` and `r8a.large` (see `<AWS-instance>`).

```text
GCIxx/
├── GCIxx_code_with_smell.py
├── GCIxx_code_without_smell.py
├── Mac-Mini-M4/
│   └── 10k/
│       ├── mac/
│       │   └── measure-<N>/
│       │       ├── raw/
│       │       │   ├── csv/
│       │       │   │   ├── history_with_smell.csv
│       │       │   │   └── history_without_smell.csv
│       │       │   └── plots/
│       │       │       ├── comparisons/
│       │       │       ├── moustaches/
│       │       │       ├── time/
│       │       │       └── violins/
│       │       └── cleaned/
│       │           ├── csv/
│       │           └── plots/
│       └── results/
│           ├── raw/
│           │   └── mac/
│           │       ├── mac_report.md
│           │       ├── with_smell.csv
│           │       └── without_smell.csv
│           └── cleaned/
│               └── mac/
│                   ├── mac_report.md
│                   ├── with_smell.csv
│                   └── without_smell.csv
└── EC2
    └── 10k/
        └── <AWS-instance>/output
            └── carbon
                ├── measure-<N>/
                │   ├── raw/
                │   │   ├── csv/
                │   │   │   ├── history_with_smell.csv
                │   │   │   └── history_without_smell.csv
                │   │   └── plots/
                │   │       ├── comparisons/
                │   │       ├── moustaches/
                │   │       ├── time/
                │   │       └── violins/
                │   └── cleaned/
                │       ├── csv/
                │       └── plots/
                └── results/
                    ├── raw/
                    │   └── mac/
                    │       ├── mac_report.md
                    │       ├── with_smell.csv
                    │       └── without_smell.csv
                    └── cleaned/
                        └── mac/
                            ├── mac_report.md
                            ├── with_smell.csv
                            └── without_smell.csv
```

The `mac` directory directly under `10k` contains the results of the individual measurement runs made with the _zeus-apple-silicon_ profiler (see, for example, [GCI24/Mac-Mini-M4](/GCI24/Mac-Mini-M4/10k/mac)). The `carbon` directory under `<AWS-instance>/output` contains the results of the individual measurement runs made with the _CodeCarbon_ profiler (see, for example, [GCI24/EC2/10k/c8a.large](/GCI24/EC2/10k/c8a.large/output/carbon/)).

Each `measure-<N>` subdirectory represents one run and contains separate raw and cleaned CSV data and plots for the two code variants. Within each run, `raw` contains the original measurements and `cleaned` contains the processed measurements. The CSV files record measurements by iteration for each code variant; the plots visualize comparisons and metric distributions.

The `results` directory contains data combined across measurement runs, separated by variant, along with a Markdown report for each profiler and data state (see, for example, [GCI24 cleaned](/GCI24/Mac-Mini-M4/10k/results/cleaned/mac/mac_report.md) and [GCI24 raw](/GCI24/Mac-Mini-M4/10k/results/raw/mac/mac_report.md)).
