import os
from pprint import pprint as pp

import xlrd

from data_sources import IncomeTaxGenderRegionCountry
from extract import download_file
from interpret import identify_section_headers_and_subheaders


def transform(filepath: str):
    pass


def fetch_data(filepath: str):
    """
    this is the ugly bit :/
    numbers in thousands, amounts £ million
    """
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    headings = (
        "United Kingdom",
        "England",
        "North East",
        "North West",
        "Yorkshire and the Humber",
        "East Midlands",
        "West Midlands",
        "East of England",
        "London",
        "South East",
        "South West",
        "Wales",
        "Scotland",
        "Northern Ireland",
    )
    sub_headings = ("Total", "Male", "Female")
    column_names = (
        "self_employment_income_no_individuals",
        "self_employment_income_amount_gbp",
        "employment_income_no_individuals",
        "employment_income_amount_gbp",
        "pension_income_no_individuals",
        "pension_income_amount_gbp",
        "property_interest_dividend_and_other_income_no_individuals",
        "property_interest_dividend_and_other_income_amount_gbp",
    )
    offset_rows_from_subheading = 2
    headings = identify_section_headers_and_subheaders(sheet, headings, sub_headings, col_idx=0)
    # TODO check all headings were returned and return a nice error
    pp(headings)


def main():
    filepath = download_file(IncomeTaxGenderRegionCountry.data_url)
    fetch_data(filepath)


if __name__ == "__main__":
    # main()
    fetch_data(os.path.join(os.getcwd(), "income_tax_gender_region_country.xlsx"))
