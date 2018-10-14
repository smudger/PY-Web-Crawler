from urllib.parse import urlparse

# get last two of subdomain
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# get subdomain name
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
