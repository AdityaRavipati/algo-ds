def strings(keywords, sentences):
    sen_list = []
    res_dict = {}
    res_keywords = []

    for sen in sentences:
        sen_list.append(sen.split())

    for key in keywords:
        count = 0
        for sen in sen_list:
            for i in range(len(sen)):
                if key==sen[i]:
                    count+=1
        res_dict[key] = count

    res_keys = sorted(res_dict.values())
    max_value1 = max(res_keys)
    res_keys.pop()
    max_value2 = max(res_keys)

    for key, value in res_dict.items():
        if value == max_value1 or value == max_value2:
            res_keywords.append(key)
    return res_keywords




# driver code

keywords = ['accept', 'lazy', 'poor']
sentences = ["I am aditya I accept my name",
             "I am a very lazy fellow lazy lazy lazy",
             "I am poor in coding I accept my poor poor"]

print(strings(keywords, sentences))