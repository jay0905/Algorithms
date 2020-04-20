# 출처: https://programmers.co.kr/learn/courses/30/lessons/42893
# 아직 틀린 풀이

import re

def solution(word, pages):
    basic_regex = r"[^a-zA-Z]" + re.escape(word.lower()) + r"[^a-zA-Z]"
    basic_scores = {}
    link_scores = {}
    page_dict = {}
    matching_scores = []

    for idx, page in enumerate(pages):
        page = page.lower()
        basic = len(re.findall(basic_regex, page))
        url = re.search('<meta property="og:url" content="(.*)"/>', page).group(1)
        linked_url = re.findall('<a href="(.*)">', page)

        page_dict[idx] = {'url': url, 'basic_score': basic, 'linked_url': linked_url}
        basic_scores[url] = basic
        link_scores[url] = basic / len(linked_url)

    for i in page_dict.keys():
        link_score = 0
        
        for j in page_dict.keys():
            if page_dict[i]['url'] in page_dict[j]['linked_url']:
                link_score += link_scores[page_dict[j]['url']]

        matching_score = page_dict[i]['basic_score'] + link_score
        matching_scores.append([i, matching_score])

    matching_scores.sort(key=lambda x:(-x[1], x[0]))

    return matching_scores[0][0]

