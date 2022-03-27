def get_top_tweet_days(list_of_tweets):
    top = []

    # Days list format: [[day, day_count], ...]
    days = []

    for tweet in list_of_tweets:
        day_already_included = False
        date = tweet['date']
        depured_date = date[0:10]

        if len(days) == 0:
            days.append([depured_date, 1])

        else:
            for day in days:
                if tweet['date'][0:10] == day[0]:
                    day_already_included = True
                    day[1] += 1
                    break

            if day_already_included == False:
                days.append([tweet['date'][0:10], 1])

    for day in days:

        if len(top) < 10:
            top.append(day)
            top = sorted(top, key=lambda x: x[1], reverse=True)

        elif len(top) == 10:
            index = 0
            for element in top:
                if day[1] > element[1] and not day in top:
                    top.insert(index, day)
                    top.pop()
                index += 1

    for element in top:
        print(element)