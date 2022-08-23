from analysis import word_extraction
from nlptoolsjp.cloud import create_wordcloud


def youtube_cloud(video_data):
    result = word_extraction(video_data, nelogd=True)
    create_wordcloud(result, filename=f'static/images/{video_data["title"]}.png')


if __name__ == '__main__':
    from nlptoolsjp.file_system import file_load
    data = file_load('comment_data/3.json')
    youtube_cloud(data)
