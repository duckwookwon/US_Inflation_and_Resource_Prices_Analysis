# U.S. Inflation and Natural Resource Prices Analysis
This project looks at how U.S. inflation and natural resource prices changed between January 2008 and July 2021. I focused on WTI crude oil, Brent crude oil, and natural gas prices.

I used Python and Pandas to clean and combine two datasets from Kaggle, then used Matplotlib to compare the trends and relationships.


## Data sources

Historical Prices of Major Natural Resources:
https://www.kaggle.com/datasets/albertobircoci/historical-prices-of-major-natural-resource

U.S. Inflation Data:
https://www.kaggle.com/datasets/varpit94/us-inflation-data-updated-till-may-2021

**Analysis period:** January 2008 – July 2021 (163 months). The CPI file ends in July 2021, even though the resource prices continue into 2025. The analysis only uses overlapping months.

## Tools

Python, Pandas, Matplotlib, pathlib, Kagglehub

## Project structure

```text
US_Inflation_and_Resource_Prices_Analysis/
├── data/
│   ├── raw/
│   │   ├── Resources_Dataset.csv
│   │   └── US CPI.csv
│   └── processed/
│       ├── cpi_monthly.csv
│       ├── resource_prices_monthly.csv
│       └── inflation_resource_monthly.csv
├── src/
│   └── download_data.py
├── figures/
├── notebooks/
│   ├── 01_clean_data.ipynb
│   └── 02_analysis.ipynb
├── requirements.txt
└── README.md
```

## How to run

1. Open the project folder in VS Code or a terminal.
2. Install the libraries:

   ```
   pip install -r requirements.txt
   ```

3. Download the two CSV files from Kaggle by running:

   ```
   python src/download_data.py
   ```

   Kagglehub downloads the files from the two Kaggle dataset pages. It may require Kaggle authentication depending on your local setup.

4. Open **`notebooks/01_clean_data.ipynb`** and run all cells. It loads the raw files, calculates inflation and monthly resource prices, merges them, and saves the three processed CSV files in `data/processed/`.

5. Open **`notebooks/02_analysis.ipynb`** and run all cells. It loads `data/processed/inflation_resource_monthly.csv` and creates the charts in `figures/`.

Open the notebooks from VS Code or Jupyter. The notebooks detect the project folder whether the working directory is the project root or `notebooks/`.

## Notebook workflow

- `notebooks/01_clean_data.ipynb`: inspect raw CSVs → clean CPI → convert daily resource prices to monthly averages → merge and save cleaned CSVs
- `notebooks/02_analysis.ipynb`: load cleaned monthly CSV → inspect the table → visualize and compare inflation and resource prices

## What I analyzed

1. U.S. year-over-year inflation and oil prices over time
2. Monthly CPI and WTI price changes
3. Correlations between inflation, oil, and natural gas changes
4. Scatter plots of monthly changes
5. 12-month rolling correlation
6. Brent–WTI price spread
7. Average monthly inflation in 2019, 2020, and January–July 2021
8. Distribution of monthly inflation

## Main findings

- Monthly inflation had a positive correlation with WTI and Brent monthly price changes. The relationship with natural gas price changes was weaker.
- Oil price changes were much larger than monthly CPI changes.
- The correlation between inflation and WTI changes varied across the sample.
- The difference between Brent and WTI prices was especially large in some months of 2011–2012.

## Limitations

The charts show associations, not causation. CPI and commodity prices are different measures with different units. Daily futures prices were averaged within each month. The CPI data ends in July 2021, and the 2021 period comparisons cover only seven months. The results are not forecasts.
