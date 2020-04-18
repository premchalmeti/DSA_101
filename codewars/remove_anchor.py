def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url

if __name__ == '__main__':
    print(remove_url_anchor('www.codewars.com?page=1'))

