import sublist3r

domain = 'tiktok.com'
subdomains = sublist3r.main(domain, 40, 'output.txt', ports=None, silent=False, verbose=True, enable_bruteforce=False, engines=None)
print(subdomains)
