from kaggle.api.kaggle_api_extended import KaggleApi

def extract_data():

    api = KaggleApi()
    api.authenticate()

    dataset = "tanishqjoshi16/ipl-2025-data-set"

    api.dataset_download_files(
        dataset,
        path="data/raw",
        unzip=True
    )

    print("Dataset Downloaded Successfully")


if __name__ == "__main__":
    extract_data()