from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.6pe7g.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']

    doc = {'nickname': nickname_receive, 'comment': comment_receive}
    db.fanscomment.insert_one(doc)

    return jsonify({'msg':'응원 남기기 성공!!'})

@app.route("/homework", methods=["GET"])
def homework_get():

    comment_list = list(db.fanscomment.find({}, {'_id': False}))

    return jsonify({'comments': comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)