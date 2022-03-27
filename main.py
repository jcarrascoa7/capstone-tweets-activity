import json

import mostretweeted
import topdays
import topusers
import tophashtags

def main():

    tweets  = []

    # open the file
    for line in open('tweets.json', 'r'):
        tweets.append(json.loads(line))
    
    option = int(input("1-. Most Retweeted\n2-. Top Days\n3-. Top Users\n4-. Top Hashtags\n"))

    # print(tweets[0])

    # call the selected function
    if option == 1:
        mostretweeted.get_most_retweeted(tweets)
    elif option == 2:
        topdays.get_top_tweet_days(tweets)
    elif option == 3:
        topusers.get_top_users(tweets)
    elif option == 4:
        tophashtags.get_top_hashtags(tweets)

main()