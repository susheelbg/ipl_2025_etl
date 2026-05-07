from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def extract_data():

    # Get credentials from .env
    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")

    # Set environment variables
    os.environ["KAGGLE_USERNAME"] = username
    os.environ["KAGGLE_KEY"] = key

    # Authenticate Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Dataset name
    dataset = "tanishqjoshi16/ipl-2025-data-set"

    # Download dataset
    api.dataset_download_files(
        dataset,
        path="data/raw",
        unzip=True
    )

    print("Dataset Downloaded Successfully")


if __name__ == "__main__":
    extract_data()