# -*- coding: utf-8 -*-
import tweepy, random

def main():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    tack_tweets = api.search(q="tack", lang="sv", count=2, result_type="recent")

    try:
        tack_tweets_answers = [
            'Varsågod!',
            'Varsågod',
            'varsågod :)',
            'Varsågod :)',
            'varsågod'
        ]

        for tack_tweet in tack_tweets:
            tack_tweet_username = tack_tweet.user.screen_name
            tack_tweet_answer = ".@%s %s" % (tack_tweet_username, random.choice(tack_tweets_answers).decode("utf8"))
            api.update_status(status=tack_tweet_answer, in_reply_to_status_id=tack_tweet.id)
            print "Posted reply to: %s" % tack_tweet.id
    except:
        print "Tweet failed"

if __name__ == '__main__':
    main()