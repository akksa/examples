#SKumar
#This will extract the tweet info from saved twitter search results

import sys,csv
from BeautifulSoup import BeautifulSoup
from utils import stripHtml
from datetime import datetime

def write_to_csv(pages, fname):
    f=open(fname, 'wb')
    fields = []
    for each in pages:
        fields.extend(each.keys())
    w = csv.DictWriter(f,fieldnames = list(set(fields)))
    #w.writeheader()
    #w.writeheader()
    fields = list(set(fields))
    header_dict = dict([(x,x) for x in fields])
    w.writerow(header_dict)
    for page in pages:
        try:
            #w.writerow({k:v.encode('utf8') for k,v in page.items()})
            #w.writerow({k:v.encode('utf8') for k,v in page.items()})
            w.writerow(dict([(k,v.encode('utf8',errors='ignore') if not (isinstance(v,bool) or  isinstance(v, int) or isinstance(v,dict)  or isinstance(v,list))   else str(v)) for k,v in page.items()]))
        except:
            print traceback.format_exc()
            print page
    f.close()
    print 'data written in the file %s'%fname
    
    
if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        print 'Please pass the saved html twitter search results in args'
        sys.exit(0)
    f = open(sys.argv[1])
    soup = BeautifulSoup(f.read())
    f.close()
    tweets = soup.findAll('li','js-stream-item stream-item stream-item expanding-stream-item')
    pages = []
    for tweet in tweets[:]:
        try:
            page = {}
            page['Author ID'] = stripHtml(tweet.find('span','username js-action-profile-name').renderContents()).lstrip('@').strip()
            page['Author Name'] = stripHtml(tweet.find('strong','fullname js-action-profile-name show-popup-with-id').renderContents())
            #page['Date'] =  str(tweet.find('small').a['data-original-title'])
            page['Date'] = datetime.strftime(datetime.fromtimestamp(1393140832),'%Y-%m-%d %H:%M:%S')
            page['Tweet'] = stripHtml(tweet.find('p','js-tweet-text tweet-text').renderContents())
            pages.append(page)
        except:
            print 'error'
            import traceback
            #print traceback.format_exc()
            #print stripHtml(tweet.renderContents())
        
    write_to_csv(pages,'/tmp/test.csv')
    print 'Done'
    