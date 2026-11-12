# Replication package of "???"

This upload includes the energy measurements results collected using the EnergyTracer pipeline, supporting the paper **???**, submitted to the 11th International Workshop on Green and Sustainable Software (GREENS'27), co-located with ICSE 2027.

## Data directory structure

EnergyTracer stores the two code variants at the dataset root. Results are grouped by machine (`Mac-Mini-M4`), workload (`10k`), and profiler (`mac`, for the _zeus-apple-silicon_ profiler).

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
            │       ├── mac_report.md
            │       ├── with_smell.csv
            │       └── without_smell.csv
            └── cleaned/
                └── mac/
                    ├── mac_report.md
                    ├── with_smell.csv
                    └── without_smell.csv
```

The `mac` directory directly under `10k` contains the results of the individual measurement runs made with the _zeus-apple-silicon_ profiler. Each `measure-<N>` subdirectory represents one run and contains separate raw and cleaned CSV data and plots for the two code variants.
Within each run, `raw` contains the original measurements and `cleaned` contains the processed measurements. The CSV files record measurements by iteration for each code variant; the plots visualize comparisons and metric distributions.

The `results` directory contains data combined across measurement runs, separated by variant, along with a Markdown report for each profiler and data state.
