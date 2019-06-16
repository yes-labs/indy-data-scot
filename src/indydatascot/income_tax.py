import xlrd

from data_sources import IncomeTaxGenderRegionCountry
from extract import download_file


def transform(filepath: str):
    pass


def fetch_data(filepath: str):
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    start_points = ["United Kingdom"]
    offset_rows = 4
    num_cols = 19


def main():
    filepath = download_file(IncomeTaxGenderRegionCountry.data_url)
    fetch_data(filepath)


if __name__ == "__main__":
    main()
