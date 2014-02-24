#SKumar
#This is to demonstrate the twitterSearch Library from python

from TwitterSearch import *
import pymongo
DB = pymongo.MongoClient().test


def getTSO(keywords,*args, **kwargs):
    """This will accept the keywords and another set of optional keywords
    """
    tso = TwitterSearchOrder()    
    tso.setKeywords(keywords if isinstance(keywords,list) else [keywords])
    lang = kwargs.get('language','en')
    tso.setLanguage(lang)
    #to do try to set language
    
if __name__ == '__main__':

    try:
        tso = TwitterSearchOrder()
        my_keywords = ['#YourWishMyApp']
        tso.setKeywords(my_keywords)
        tso.setLanguage('en')
        #tso.setCount(5)
        ts = TwitterSearch(
                consumer_key = 'v4QIotR4SY1QDMb8MLw',
                consumer_secret = 'Y1ntI8nYJwV1lTA9AKwZ3bl3XH7yAvPLLBSugt5uaw',
                access_token = '1178633347-BaWKZeeiFqdmSQpVZaSVbLRbAvQSub5aG6RCwzV',
                access_token_secret = 'AyRercpIY8e74sGSm29jigrCAWehT0Jncsy7w'
            )
        for tweet in ts.searchTweetsIterable(tso):
            #print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
            tweet['keywords'] = my_keywords
            DB.twitter_search.insert(tweet)
            print 'Inserted the tweet from user %s'%tweet['user']['screen_name']

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

