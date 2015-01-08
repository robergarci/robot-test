import glob
import datetime


def updateDates():
    countriesDir = glob.glob('requests/*')
    for countryDir in countriesDir:
        countryCreateOrderRequestsFiles = glob.glob("%s%s" % (countryDir,'/createOrder/*.request'))
        for req_file in countryCreateOrderRequestsFiles:
            old_file = open(req_file, 'rw')
            req_text = ""
            for line in old_file:
                if "collection_date" in line:
                    old_line_arr = line.split(":")
                    old_date = old_line_arr[1].replace(",","").rstrip()
                    if len(old_date) == 12:
                        date = getValidDate()
                        date = date.replace("-", "/")
                        line = "\t\t\t\t\t\"collection_date\":\"%s\",\n" % date
                req_text += line

            old_file.close()
            new_file = open(req_file, 'w+')
            new_file.write(req_text)
            new_file.close()



def getValidDate():
    date = datetime.date.today() + datetime.timedelta(days=2)
    week_day = date.weekday()
    while week_day == 5 or week_day == 6:
        date = date + datetime.timedelta(days=1)
        week_day = date.weekday()

    return str(date)
