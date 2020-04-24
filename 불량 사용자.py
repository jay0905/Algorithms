# 출처: https://programmers.co.kr/learn/courses/30/lessons/64064#

import re
from itertools import product

def solution(user_id, banned_id):
    candidates_id = []

    for ban in banned_id:
        candidates = []
        ban_re = re.compile(ban.replace("*", "\w"))

        for user in user_id:
            if len(user) == len(ban) and ban_re.match(user) is not None:
                candidates.append(user)

        candidates_id.append(candidates)

    candidates_product = list(product(*candidates_id))
    new_candidates = []

    for candidate_tuple in candidates_product:
        if len(candidate_tuple) == len(set(candidate_tuple)):
            new_candidates.append(candidate_tuple)

    answer_set = set()
    for candidate in new_candidates:
        candidate_list = sorted(list(candidate))
        answer_set.add(tuple(candidate_list))
        
    return len(answer_set)
        
