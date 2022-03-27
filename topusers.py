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

    print('users list ready')

    for user in users:
        if len(top) < 10:
            top.append(user)
            top = sorted(top, key=lambda x: x[2], reverse=True)

        elif len(top) == 10:
            index = 0
            for element in top:
                if user[2] > element[2] and not user in top:
                    top.insert(index, user)
                    top.pop()
                index += 1
    
    for element in top:
        print(element)