from tests.utils import TestUtils
from sites.jobshop import jobshopScraper
import pytest
import allure
import requests

company_name = 'jobshop'

@pytest.fixture(scope="module")
def get_job_details():
    """
    Fixture for scraping process from the career section.
    """
    scraper_data = jobshopScraper().return_data()
    testutils = TestUtils()
    scraped_jobs_data = testutils.scrape_jobs(scraper_data[0])
    peviitor_jobs_data = testutils.scrape_peviitor(scraper_data[1], 'România')
    return scraped_jobs_data, peviitor_jobs_data
    
# Test functions

@pytest.mark.regression
@pytest.mark.API
def test_jobshop_title_api(get_job_details):
    allure.dynamic.title(f"Test job titles from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job titles from the scraper"):
        job_titles_scraper = sorted(scraped_jobs_data[0])
    
    with allure.step("Step 2: Get job titles from the Peviitor API"):
        job_titles_peviitor = sorted(peviitor_jobs_data[0])

    with allure.step("Step 3: Compare job titles from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_titles_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_titles_peviitor}", name="Actual Results")
        TestUtils().check_job_titles(job_titles_scraper, job_titles_peviitor)

@pytest.mark.regression
@pytest.mark.API
def test_jobshop_city_api(get_job_details):
    allure.dynamic.title(f"Test job cities from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job cities and titles from the scraper"):
        job_cities_scraper = scraped_jobs_data[1]
        job_titles_scraper = scraped_jobs_data[0]
        
    with allure.step("Step 2: Get job cities and titles from the Peviitor API"):
        job_cities_peviitor = peviitor_jobs_data[1]
        job_titles_peviitor = peviitor_jobs_data[0]

    with allure.step("Step 3: Compare job cities from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_cities_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_cities_peviitor}", name="Actual Results")
        TestUtils().check_job_cities(job_cities_scraper, job_cities_peviitor, job_titles_scraper, job_titles_peviitor)


@pytest.mark.regression
@pytest.mark.API
def test_jobshop_country_api(get_job_details):
    allure.dynamic.title(f"Test job countries from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job countries and titles from the scraper"):
        job_countries_scraper = scraped_jobs_data[2]
        job_titles_scraper = scraped_jobs_data[0]
        
    with allure.step("Step 2: Get job countries and titles from the Peviitor API"):
        job_countries_peviitor = peviitor_jobs_data[2]
        job_titles_peviitor = peviitor_jobs_data[0]

    with allure.step("Step 3: Compare job countries from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_countries_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_countries_peviitor}", name="Actual Results")
        TestUtils().check_job_countries(job_countries_scraper, job_countries_peviitor, job_titles_scraper, job_titles_peviitor)
@pytest.mark.regression
@pytest.mark.API
def test_jobshop_link_api(get_job_details):
    allure.dynamic.title(f"Test job links from the {company_name} website against Peviitor API Response")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job links from the scraper"):
        job_links_scraper = sorted(scraped_jobs_data[3])
    with allure.step("Step 2: Get job links from the Peviitor API"):
        job_links_peviitor = sorted(peviitor_jobs_data[3])

    with allure.step("Step 3: Compare job links from scraper response against Peviitor API Response"):
        allure.attach(f"Expected Results: {job_links_scraper}", name="Expected Results")
        allure.attach(f"Actual Results: {job_links_peviitor}", name="Actual Results")
        TestUtils().check_job_links(job_links_scraper, job_links_peviitor)

@pytest.mark.regression
@pytest.mark.API
def test_jobshop_status_code_link_api(get_job_details):
    allure.dynamic.title(f"Test http code response on job links for {company_name} website")

    scraped_jobs_data, peviitor_jobs_data = get_job_details
    with allure.step("Step 1: Get job links from the scraper"):
        job_links_scraper = sorted(scraped_jobs_data[3])

    with allure.step("Step 2: Check job links for response code"):
        status_codes_expected_result = [200] * len(job_links_scraper)
        status_codes_actual_result = [requests.get(link).status_code for link in job_links_scraper]
        allure.attach(f"Expected Results: {status_codes_expected_result}", name="Expected Results")
        allure.attach(f"Actual Results: {status_codes_actual_result}", name="Actual Results")
        TestUtils().check_code_job_links(status_codes_expected_result, status_codes_actual_result)