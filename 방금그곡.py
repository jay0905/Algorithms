출처: https://programmers.co.kr/learn/courses/30/lessons/17683#

def convert_note(music):
    music = music.replace("C#", "c")
    music = music.replace("D#", "d")
    music = music.replace("F#", "f")
    music = music.replace("G#", "g")
    music = music.replace("A#", "a")

    return music

def solution(m, musicinfos):

    START = 0
    END = 1
    NAME = 2
    NOTE = 3
    candidate = []

    m = convert_note(m)

    for idx, musicinfo in enumerate(musicinfos):
        infos = musicinfo.split(",")

        if infos[START][:2] != infos[END][:2]:
            if infos[END][:2] == "00":
                play_time = 60 - int(infos[START][3:5])
            else:
                play_time = 60 - int(infos[START][3:5]) + int(infos[END][3:5])
        else:
            play_time = int(infos[END][3:5]) - int(infos[START][3:5])

        converted = convert_note(infos[NOTE])

        if play_time > len(converted):
            play_cnt = play_time // len(converted)
            play_left = play_time % len(converted)
            played_music = converted * play_cnt + converted[:play_left]
        else:
            played_music = converted[:play_time]
        
        if m in played_music:
            candidate.append([play_time, idx, infos[NAME]])

    if not candidate:
        return "`(None)`"
        
    candidate.sort(key=lambda x:(-x[0], x[1]))

    return candidate[0][2]
