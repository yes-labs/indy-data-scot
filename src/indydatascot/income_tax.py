import logging
import os
import re
from pprint import pprint as pp

import xlrd

import errors
from data_sources import IncomeTaxGenderRegionCountry
from extract import download_file
from interpret import identify_section_headers_and_subheaders

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(name)s:%(levelname)s::%(message)s")
logger = logging.getLogger(__name__)


def transform(filepath: str):
    pass


def fetch_data(filepath: str):
    """
    this is the ugly bit :/
    numbers in thousands, amounts £ million
    """
    wb = xlrd.open_workbook(filename=filepath)
    sheet = wb.sheet_by_index(0)
    getval = sheet.cell_value
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
    columns = {
        "self_employment_income_no_individuals": 2,
        "self_employment_income_amount_gbp": 3,
        "employment_income_no_individuals": 5,
        "employment_income_amount_gbp": 6,
        "pension_income_no_individuals": 8,
        "pension_income_amount_gbp": 9,
        "property_interest_dividend_and_other_income_no_individuals": 11,
        "property_interest_dividend_and_other_income_amount_gbp": 12,
    }
    offset_rows_from_subheading = 2
    heading_locns = identify_section_headers_and_subheaders(
        sheet, headings, sub_headings, col_idx=0
    )
    if len(heading_locns) != len(headings) * len(sub_headings):
        raise errors.DataFormatDoesntMatchExpectedError(
            "Did not find an entry for all of the expected headings and sub headings, "
            "could the layout of this publication have changed?"
        )
    # pp(heading_locns)
    # for colname, col_idx in columns.items():
    #     print("expected: ", colname, ", found: ", sheet.cell_value(10, col_idx))
    for heading, subheading, coords in heading_locns:
        if subheading == "Total":
            offset_all_ranges = 17
        else:
            offset_all_ranges = 16

        row_idx, col_idx = coords
        logger.info(f"heading={heading}, subheading={subheading}, coords={coords}")
        if (
            getval(row_idx + 2, col_idx) != 11000
            or getval(row_idx + offset_all_ranges, col_idx) != "All Ranges"
        ):
            raise errors.DataFormatDoesntMatchExpectedError(
                "Did not find row labels in the expected format. "
                "Expected to find labels from 11000 to 1000000 then an 'All Ranges' row."
                "Could the layout of this publication have changed?"
            )


def main():
    filepath = download_file(IncomeTaxGenderRegionCountry.data_url)
    fetch_data(filepath)


if __name__ == "__main__":
    # main()
    fetch_data(os.path.join(os.getcwd(), "income_tax_gender_region_country.xlsx"))
