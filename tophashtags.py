import re

def get_top_hashtags(list_of_tweets):
    top = []

    # Hashtags list format: [[hashtag_content, hashtag_count], ...]
    all_hashtags = []

    for tweet in list_of_tweets:
        hashtag_already_included = False
        text_list = re.findall(r'#\S+', tweet['content'])
        # print(text_list)

        for word in text_list:
            # print(word)
            
            if "#" in word:

                for hashtag in all_hashtags:
                    if word == hashtag[0]:
                        hashtag[1] += 1
                        hashtag_already_included = True
                        break

                if hashtag_already_included == False:
                    all_hashtags.append([word, 1])

        # print(all_hashtags)
    
    for hashtag in all_hashtags:

        if len(top) < 10:
            top.append(hashtag)
            top = sorted(top, key=lambda x: x[1], reverse=True)
            print(top)

        elif len(top) == 10:
            index = 0
            for element in top:
                if hashtag[1] > element[1] and not hashtag in top:
                    top.insert(index, hashtag)
                    top.pop()
                index += 1

    for element in top:
        print(element)
