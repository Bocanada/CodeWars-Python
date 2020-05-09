def domain_name(url):
    # your code here
    return url.split('//')[-1].split('www.')[-1].split('.')[0]
