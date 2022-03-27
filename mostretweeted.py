
def get_most_retweeted(list_of_tweets):
    top = []

    for tweet in list_of_tweets:

        if len(top) == 0:
            top.append([tweet['retweetCount'], tweet['content']])

        elif len(top) > 0 and len(top) < 10:
            index = 0
            for element in top:
                new_element = [tweet['retweetCount'], tweet['content']]
                if tweet['retweetCount'] > element[0] and new_element not in top:
                    top.insert(index, [tweet['retweetCount'], tweet['content']])
                index += 1

        elif len(top) == 10:
            index = 0
            for element in top:
                new_element = [tweet['retweetCount'], tweet['content']]
                if tweet['retweetCount'] > element[0] and new_element not in top:
                    top.insert(index, [tweet['retweetCount'], tweet['content']])
                    top.pop()
                index += 1


    for element in top:
        print(f"{element[0]} - {element[1]}")