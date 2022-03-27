def get_top_users(list_of_tweets):
    top = []

    # Users list format: [[user_id, user_name, user_tweet_count], ...]
    users = []

    for tweet in list_of_tweets:
        user_already_included = False

        if len(users) == 0:
            users.append([tweet['user']['id'], tweet['user']['username'], 1])

        else:
            for user in users:
                if tweet['user']['id'] == user[0]:
                    user_already_included = True
                    user[2] += 1
                    break

            if user_already_included == False:
                users.append([tweet['user']['id'], tweet['user']['username'], 1])


    for user in users:
        if len(top) == 0:
            top.append(user)

        elif len(top) > 0 and len(top) < 10:
            index = 0
            for element in top:
                if user[2] > element[2]:
                    top.insert(index, user)
                index += 1

        elif len(top) == 10:
            index = 0
            for element in top:
                if user[2] > element[2]:
                    top.insert(index, user)
                    top.pop()
                index += 1
    
    print(len(users))
    
    for element in top:
        print(element)