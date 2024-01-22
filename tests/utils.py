import requests
from unidecode import unidecode

class TestUtils:

    def scrape_jobs(self, scraper_data):
        """
        Get the job details from the scrapped page
        """
        title = [title['job_title'] for title in scraper_data]
        job_country = [self.remove_diacritics(country['country']) for country in scraper_data]
        job_link = [job_link['job_link'] for job_link in scraper_data]
        
        # Check if the cities list is a nested list
        job_city = [self.remove_diacritics(city['city']) if isinstance(city['city'], list) else [self.remove_diacritics(city['city'])] for city in scraper_data]
            
        return title, job_city, job_country, job_link

    @staticmethod
    def _set_params(company_name, page, country):
        """
        Setting params for peviitor jobs request
        """
        params = {
            'company': company_name,
            'country': country,
            'page': page,
        }
        return params
    
    @staticmethod
    def _get_request(params):
        """
        Send a get request to get the jobs from future
        """
        response = requests.get('https://api.peviitor.ro/v3/search/', params=params).json()
        if 'response' in response and 'docs' in response['response']:
            response_data = response['response']['docs']
            return response_data
        else:
            return []

    def scrape_peviitor(self, company_name, country):
        """
        Get the job details from the peviitor
        """
        all_future_title, all_future_job_city, all_future_job_country, all_future_job_link = [], [], [], []

        page = 1
        params = TestUtils._set_params(company_name, page, country)
        response_data = TestUtils._get_request(params)
        while response_data:
            all_future_title.extend([title['job_title'][0] for title in response_data])
            all_future_job_country.extend([self.remove_diacritics(country['country'][0]) for country in response_data])
            all_future_job_link.extend([job_link['job_link'][0] for job_link in response_data])
            
            city_list = [self.remove_diacritics(city['city']) for city in response_data]
            is_nested = all(isinstance(item, list) for item in city_list)
            
            if is_nested:
                all_future_job_city.extend(city_list)
            else:
                all_future_job_city.extend([self.remove_diacritics(city['city'][0]) for city in response_data])

            page += 1
            params = TestUtils._set_params(company_name, page, country)
            response_data = TestUtils._get_request(params)

        return all_future_title, all_future_job_city, all_future_job_country, all_future_job_link
    
    # Remove diacritics from input recursive
    def remove_diacritics(self, item):
        
        # If instance of list remove diacritics recursive
        if isinstance(item, list):
            return [self.remove_diacritics(subitem) for subitem in item]
        else:
            # Remove diacritics from string
            return unidecode(item)