import os
from flask import Flask,render_template, request
from dataset import comment_get
from create import youtube_cloud
from nlptoolsjp.file_system import file_load
import glob

app = Flask(__name__,static_folder='./static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=["POST"])
def create():
    return render_template('create.html')

@app.route('/result',methods=["POST"])
def success():
    url = request.form['url']  
    data = comment_get(url)
    if data == 0:
        return  render_template('result.html',flg = data)
    youtube_cloud(data)
    return render_template('result.html')

@app.route('/display',methods=['POST'])
def cloud_display():
    count = sum(os.path.isfile(os.path.join('comment_data',name)) for name in os.listdir('comment_data'))
    video_data = []
    for f in glob.glob('comment_data/*.json'):
        data = file_load(f)
        video_data.append(data)
    return render_template('display.html',array = video_data)

if __name__ == "__main__":
    app.run(debug=True)
