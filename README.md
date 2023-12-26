
# Test Job Scrapers for Peviitor.ro

This project is dedicated to testing the efficiency of job data extraction, for details such as job title, city, country, county, and link. Our primary objective is to ensure precise data extraction while concurrently confirming the presence of this information on the Peviitor.ro website.

## Features

The project incorporates the following key features:

- GitHub Actions: Enables automated test workflows directly from GitHub repositories, in this context, ensuring regular test reports for the scrapers
- Pytest: A testing framework for Python that facilitates efficient and scalable testing.
- API Testing: In-depth testing of APIs to guarantee data accuracy and reliability.
- Multiple Assertions: Rigorous validation of multiple data points to ensure comprehensive accuracy.
- Data Validation: The project emphasizes the importance of verifying scraped data against the information available on peviitor.ro.
- Allure Reporting: Comprehensive reports are generated regularly for detailed insights of the testing process execution
- Parallel Running: The ability to run multiple scraping processes concurrently for enhanced efficiency.

## API Test Run with parallel running

[https://github.com/peviitor-ro/JobsScrapers/assets/91252395/26dfbf52-d1c0-4213-8331-963ebd1dd94f](https://github-production-user-asset-6210df.s3.amazonaws.com/91252395/278391776-26dfbf52-d1c0-4213-8331-963ebd1dd94f.mp4)

## API Test Run without parallel running

[https://github.com/peviitor-ro/JobsScrapers/assets/91252395/8acaafb9-dff0-4f4f-ad7c-3f138e2daba8](https://github-production-user-asset-6210df.s3.amazonaws.com/91252395/277583302-8acaafb9-dff0-4f4f-ad7c-3f138e2daba8.mp4)

## Allure Report

For detailed insights into the test results, an Allure report is generated, providing a comprehensive overview of the scraping process.
The report is updated every day when github actions runs and it can be seen live at https://peviitor-ro.github.io/RaresTestHub/api_test_report.html 

![allure result 2](https://github.com/peviitor-ro/JobsScrapers/assets/91252395/fe1565c8-5ddd-481f-9211-c9fb41c02571)

## Setup

To get started with the project, follow these steps:

- Install and Configure Python 3: Ensure you have Python 3 installed and properly configured on your system.
- Set Up Your IDE: Prepare your preferred Integrated Development Environment (IDE) for working on this project.
- Import Cloned Repository as Project: Clone the repository and import it into your IDE as a new project.
- Add Folder Path to PYTHONPATH: Include the path of the project folder in the PYTHONPATH variable in your environment settings.
- Install Required Packages: Use the following command to install all the necessary packages: 
```bash
pip install -r requirements.txt
```
- Running Tests: Execute the tests by running the following command:
```bash
pytest
```
