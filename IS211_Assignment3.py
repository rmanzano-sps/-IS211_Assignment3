import urllib2
import argparse
import csv
import re

# type python IS211_Assignment3.py --help in terminal for assistance

def image_hits(csv_doc):
    total_images = 0
    total_jpg = 0
    total_png = 0
    total_gif = 0

    try:
        for image in csv_doc:
            total_images = total_images + 1
            found_image = re.search(r".jpg|.png|.gif", image[0])
            if found_image:
                if found_image.group(0) == '.jpg':
                    total_jpg = total_jpg + 1
                elif found_image.group(0) == '.png':
                    total_png = total_png + 1
                elif found_image.group(0) == '.gif':
                    total_gif = total_gif + 1
    except IndexError:
        pass

    found_images = (total_jpg + total_png +  total_gif)
    perecnet_of_total = (float(found_images)/float(total_images)) * 100

    return(perecnet_of_total)

def popular_browser(csv_doc):
    firefox = 0
    chrome = 0
    internet_explorer = 0
    safari = 0

    try:
        for browser in csv_doc:
            found_browser = re.search(r"Firefox|Chrome|Explorer|Safari", browser[2])
            if found_browser:
                if found_browser.group(0) == 'Firefox':
                    firefox = firefox + 1
                elif found_browser.group(0) == 'Chrome':
                    chrome = chrome + 1
                elif found_browser.group(0) == 'Explorer':
                    internet_explorer = internet_explorer + 1
                elif found_browser.group(0) == 'Safari':
                    safari = safari + 1
    except IndexError:
        pass

    browser_dict = {'safari': safari, 'chrome': chrome, 'internet_explorer': internet_explorer, 'firefox': firefox}
    name_result = max(browser_dict, key=browser_dict.get)

    return({name_result: browser_dict[name_result]})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="for results, type python 'name of file' and url as a string. A suggested link: 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'", type=str)
    args = parser.parse_args()
    req = urllib2.Request(args.url)
    response = urllib2.urlopen(req)
    decode_response = response.read().decode("utf-8")
    csv_doc = list(csv.reader(decode_response.split('\n')))
    image_hit_results = image_hits(csv_doc)
    popular_browser_results = popular_browser(csv_doc)
    print('Image requests account for %s%% of all requests.' % image_hit_results)
    print('The most popular browser is {0} with {1} users.'.format(popular_browser_results.keys(), popular_browser_results.values()))

if __name__ == '__main__':
    main()
