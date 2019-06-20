import logging

import xlrd

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(name)s:%(levelname)s::%(message)s")
logger = logging.getLogger(__name__)


def identify_section_headers_and_subheaders(
    sheet: xlrd.sheet.Sheet, headings: iter, sub_headings: iter, col_idx: int
):
    """
    where a sheet is arranged like this with all the headings and sub headings in the same column
    ```
    heading
        sub heading
            data
        sub heading
            data
    heading
        sub heading
            data
    ```

    Will return a tuple of the locations of the sub headings, matched up with headings.
    Assumes that all data sections are under a sub heading.
    :return:
        list of headers and their location in the format
        [
            ('heading value', 'sub heading value', (row index, column index)),
        ]
    """
    found_headers = []
    for row_idx in range(0, sheet.nrows):
        coords = (row_idx, col_idx)
        # print(coords, sheet.cell_value(*coords))
        test_text = sheet.cell_value(*coords)
        if test_text in headings:
            logger.debug("FOUND HEADING", coords, sheet.cell(*coords))
            heading_value = test_text
        elif test_text in sub_headings:
            logger.debug("FOUND SUBHEADING", coords, sheet.cell(*coords))
            sub_heading_value = test_text
            found_headers.append((heading_value, sub_heading_value, coords))
    return found_headers
