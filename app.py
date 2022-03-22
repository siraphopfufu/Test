from flask import request,jsonify
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
@app.route('/')
def home():
  return '<h1>Hello from Flask<h1>'

@app.route('/greeting')
def greeting():
  name=request.args.get('name') 
  return '<h3>Hello '+name+'<h3>'

@app.route('/insert')
def insert():
  id=request.args.get('id')
  q1=request.args.get('q1')
  q2=request.args.get('q2')
  client=MongoClient("mongodb+srv://6238220521:fufu@cluster0.bgstt.mongodb.net/<dbname>?retryWrites=true&w=majority")
  db=client.all_score
  db.score.insert_one({'id':id,'q1':int(q1),'q2':int(q2)})
  return '<h3>Finished!<h3>'

@app.route('/get')
def get():
  ret=dict()
  ret['data']=[{'id':'6238220021','q1':8,'q2':9},{'id':'6238222221','q1':7,'q2':6}]
  return jsonify(ret)

@app.route('/findscore')
def findscore():
  id = int(request.args.get('id'))
  client=MongoClient("mongodb+srv://6238220521:fufu@cluster0.bgstt.mongodb.net/<dbname>?retryWrites=true&w=majority")
  db=client.all_score
  st=db.score.find_one({'id':id})
  try:
    st.pop('_id')
    return  jsonify({'data':st})
  except:
    return 'Invalid ID'

app.run()
