from data_sources import IncomeTaxGenderRegionCountry
from extract import download_file


def transform(filepath: str):
    pass


def main():
    path = download_file(IncomeTaxGenderRegionCountry.data_url)


if __name__ == "__main__":
    main()
