import datetime
from dataclasses import dataclass


@dataclass
class SourcePublication:
    org_name: str
    publication_name: str
    publication_version: str  # e.g. '2016-2017 release'
    data_url: str  # where to get the actual data file(s)
    reference_url: str  # where to find supplementary information
    description: str
    publish_date: datetime.date
    license: str


class HMRCPublication(SourcePublication):
    org_name = "HM Revenue & Customs"
    license = (
        "Contains public sector information licensed under the Open Government Licence "
        "v3.0. https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
    )


class IncomeTaxGenderRegionCountry(HMRCPublication):
    publication_name = "Income and tax, by gender, region and country"
    publication_version = "2016 to 2017"
    data_url = (
        "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/"
        "attachment_data/file/782862/NS_Table_3_11_1617.xlsx"
    )
    reference_url = (
        "https://www.gov.uk/government/statistics/income-and-tax-by-gender-region-"
        "and-country-2010-to-2011"
    )
    description = (
        "These tables give distributions of total income and tax for the "
        "United Kingdom, England, Wales, Scotland and Northern Ireland."
    )
    publish_date = datetime.date(year=2019, month=3, day=6)
