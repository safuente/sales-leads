from decouple import config, Csv


def get_start_urls():
    """Get urls to scrap from settings"""
    countries = config('COUNTRIES', cast=Csv())
    start_urls = []
    for url in config('URLS', cast=Csv()):
        for country in countries:
            start_urls.append(f"{url}{country}")
    return start_urls