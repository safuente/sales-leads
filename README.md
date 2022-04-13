# Sales Leads APP
Sales Leads app using Scrapy, Selenium and Streamlit. The purpose of this project is to scrap the website
https://trends.builtwith.com/ to get stores data from different urls and different urls that could be configured.


## Settings file for buildwith spider
In the path salesleads/spiders/settings.ini the following parameters could be configured
    
    # Urls from trends.builtwith.com to do the scraping process
    URLS=https://trends.builtwith.com/websitelist/Shopify/, https://trends.builtwith.com/websitelist/Shopify-Plus/,https://trends.builtwith.com/websitelist/Magento/,https://trends.builtwith.com/websitelist/WooCommerce-Checkout/
    # Countries to be included in the scraping process
    COUNTRIES =Spain, France, United Kingdom, Germany, Italy

## Launch the environment
Please follow the next steps using command line:

    git clone git@github.com:safuente/sales-leads.git
    cd sales-leads
    pip install virtualenv (if you don't already have virtualenv installed)
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

* Note: This repo has been tested with Python 3.9 version.

## Run the spider
The following command must be executed:
    
    scrapy runspider salesleads/spiders/builtwith.py

The scraping result is stored in salesleads/data/stores.json

## Results deployment
The results are deployed in the following streamlit app:
https://share.streamlit.io/safuente/sales-leads/main/main.py


