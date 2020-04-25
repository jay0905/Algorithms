# 출처: https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    play_cnt_by_genre = {}
    songs = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in play_cnt_by_genre:
            play_cnt_by_genre[genre] = play
        else:
            play_cnt_by_genre[genre] += play

        if genre not in songs:    
            songs[genre] = [[i, play]]
        else:
            songs[genre].append([i, play])

    play_sort = sorted(play_cnt_by_genre.items(), key = lambda item: item[1], reverse=True)

    answer = []
    
    for play in play_sort:
        genre = play[0]
        songs[genre].sort(key=lambda x:(-x[1], x[0]))
        answer.append(songs[genre][0][0])
        
        if len(songs[genre]) >= 2:
            answer.append(songs[genre][1][0])
    
    return answer



            
        
