from pathlib import Path
import shutil
import kagglehub

# Project folder
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Download commodity prices
resource_path = Path(kagglehub.dataset_download(
    "albertobircoci/historical-prices-of-major-natural-resource"
))
resource_file = resource_path / "Resources_Dataset.csv"
shutil.copy(resource_file, RAW_DIR / "Resources_Dataset.csv")
print("Downloaded resource prices")

# Download U.S. CPI
cpi_path = Path(kagglehub.dataset_download(
    "varpit94/us-inflation-data-updated-till-may-2021"
))
cpi_file = cpi_path / "US CPI.csv"
shutil.copy(cpi_file, RAW_DIR / "US CPI.csv")
print("Downloaded U.S. CPI")
