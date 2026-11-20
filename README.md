# Replication package of EnergyTracer

This upload includes the energy measurement results collected using the EnergyTracer pipeline, supporting the paper "_From Consensus to Evidence: Towards Empirical Validation of Eco-Code Design Rules_" submitted to the 11th International Workshop on Green and Sustainable Software (GREENS'27), co-located with ICSE 2027. Additionally, it contains the _EnergyTracer_ used for the experimental procedures, provided as a compressed Zip archive.

## Data directory structure

Each GCI directory contains the two code variants and the measurements collected for that rule. The Mac Mini M4 data is available for each GCI directory. EC2 measurements are available only for GCI24.

```text
GCIxx/
├── GCIxx_code_with_smell.py
├── GCIxx_code_without_smell.py
└── Mac-Mini-M4/
    └── 10k/
        ├── mac/
        │   └── measure-<N>/
        │       ├── raw/
        │       │   ├── csv/
        │       │   │   ├── history_with_smell.csv
        │       │   │   └── history_without_smell.csv
        │       │   └── plots/
        │       │       ├── comparisons/
        │       │       ├── moustaches/
        │       │       ├── time/
        │       │       └── violins/
        │       └── cleaned/
        │           ├── csv/
        │           └── plots/
        └── results/
            ├── raw/
            │   └── mac/
            │       ├── distributions/
            │       ├── mac_report.md
            │       ├── with_smell.csv
            │       └── without_smell.csv
            └── cleaned/
                └── mac/
                    ├── distributions/
                    ├── mac_report.md
                    ├── with_smell.csv
                    └── without_smell.csv
```

EC2 measurements are stored under `GCI24/`, grouped by AWS instance type:

```text
GCI24/
├── GCIxx_code_with_smell.py
├── GCIxx_code_without_smell.py
├── Mac-Mini-M4/
└── EC2/
    └── 10k/
        └── <AWS-instance>/
            └── output/
                ├── carbon/
                │   └── measure-<N>/
                │       ├── raw/
                │       │   ├── csv/
                │       │   └── plots/
                │       └── cleaned/
                │           ├── csv/
                │           └── plots/
                └── results/
                    ├── raw/
                    │   └── carbon/
                    │       ├── distributions/
                    │       ├── carbon_report.md
                    │       ├── with_smell.csv
                    │       └── without_smell.csv
                    └── cleaned/
                        └── carbon/
                            ├── distributions/
                            ├── carbon_report.md
                            ├── with_smell.csv
                            └── without_smell.csv
```

The `mac` directory contains individual runs made with the _zeus-apple-silicon_ profiler (see [GCI24 Mac measurements](GCI24/Mac-Mini-M4/10k/mac/)). For EC2, `carbon` contains individual runs made with the _CodeCarbon_ profiler. The available EC2 instance types in GCI24 are `c8a.large`, `m7a.large`, and `r8a.large` (see [GCI24 EC2 measurements](GCI24/EC2/10k/)).

Each `measure-<N>` subdirectory represents one run and contains separate raw and cleaned CSV data and plots for the two code variants. Within each run, `raw` contains the original measurements and `cleaned` contains the processed measurements. The CSV files record measurements by iteration for each code variant; the plots visualize comparisons and metric distributions.

Each `results` directory contains data combined across measurement runs, separated by variant, along with a Markdown report and distribution plots for each profiler and data state. For example, see the [GCI24 Mac cleaned report](GCI24/Mac-Mini-M4/10k/results/cleaned/mac/mac_report.md), [GCI24 Mac raw report](GCI24/Mac-Mini-M4/10k/results/raw/mac/mac_report.md), or [GCI24 EC2 cleaned report](GCI24/EC2/10k/c8a.large/output/results/cleaned/carbon/carbon_report.md).
