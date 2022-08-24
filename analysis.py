from nlptoolsjp.morpheme import morpheme
from nlptoolsjp.file_system import file_load
from nlptoolsjp.norm import clean_text


def word_extraction(video_data, nelogd = True):
    result = []
    ban_detail = ['副詞可能','数','非自立','代名詞','接尾']
    target_speech = ["名詞","形容詞","形容動詞"]
    ban_word = morpheme(clean_text(video_data["title"]),nelogd = nelogd)
    for comment in video_data['comment']:
        comment = comment.replace('\n','')
        comment = clean_text(comment)
        word_dict = morpheme(comment, kind = True, nelogd = nelogd)
        for w,s in word_dict.items():
            if s['speech'] in target_speech and s['reading'] != '*' and \
               s['detail_speech'][0] not in ban_detail and s["endform"] not in ban_word \
               and w not in ban_word:
                result.append(s['endform'])
    return ' '.join(result)

if __name__=='__main__':
    data = file_load('comment_data/12.json')
    result = word_extraction(data)
    print(result[:20])
    

        
        