import requests 
import lxml.etree as ET
import json
import re
import csv
import sys
import sys, getopt


def main(argv):
    pages = 2
    per_page = 5
    org = "sparkfun"

    try:
        opts, args = getopt.getopt(argv,"hp:c:o:",["page=","count_per_page=", "organization="])
    except getopt.GetoptError:
        print ('main.py -o <organization> -c <count_per_page> -p <page>')
        sys.exit(2)
    for opt, arg in opts:
        print(opt)
        print(arg)
        if opt == '-h':
            print ('main.py -c <count_per_page> -p <page> -o <organization>')
            sys.exit()
        elif opt in ("-p", "--page"):
            pages = arg
        elif opt in ("-c", "--count_per_page"):
            per_page = arg
        elif opt in ("-o", "--organization"):
            org = arg

    parser = ET.XMLParser(recover=True,  encoding='utf-8')

    with open('parts.csv', 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['library', 'deviceset', 'device', 'value']
        parts_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        parts_writer.writeheader()
        for page in range(1,int(pages)+1):
            try:
                print("Parsing page #"+str(page))
                url = "https://api.github.com/search/code?q=org:"+org+"+extension:sch&per_page="+str(per_page)+"&sort=indexed&order=dsc&page="+ str(page)
                data = json.loads(requests.get(url).text)
                for e in data['items']:
                    link = e["html_url"].replace("https://github.com", "https://raw.githubusercontent.com").replace("/blob","")
                    print("Parsing ==>:"+link)
                    root = ET.fromstring(requests.get(link).text.encode('utf-8'), parser) 
                    for p in root.find('drawing').find('schematic').find('parts'):
                        parts_writer.writerow({'library':p.get('library'), 'deviceset':p.get('deviceset'), 'device':p.get('device'), 'value': p.get('value')})
            except:
                print("\n\nError\n\n")
                pass
                

if __name__ == "__main__":
   main(sys.argv[1:])