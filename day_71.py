# Day 71: Website blocker

from datetime import datetime

host_path = 'here goes your path'
websites = ['www.facebook.com', 'www.instagram.com', 'www.twitter.com']
redirect = '127.0.0.1'

start_date = datetime(2022, 3, 23)
end_date = datetime(2022, 4, 24)
today_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_path, 'r+') as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site + '\n')
        print('All sites are blocked')
        break
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
        print('All sites are unblocked')
        break


