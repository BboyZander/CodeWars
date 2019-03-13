import re


def domain_name(url):
    res = url.split('.')
    if url == '':
        return ''
    elif 'www' in url:
        return res[1]
    elif '-' in url:
        return re.findall('\w+?-\w+',url)[0]
    else:
        return re.findall('\w+',url)[1]




print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print((domain_name('https://www.yout-ube.com?r=http://google.com')))