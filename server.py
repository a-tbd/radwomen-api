from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///radwomen.db')
app = Flask(__name__)
api = Api(app)


class Radwomen(Resource):
    def get(self):
        conn = db_connect.connect() # with db connect as conn to make sure the db closes
        print(conn)
        #query = conn.execute("select * from radwomen;")
        #names = {'names': [i[0].encode('utf-8') for i in query.cursor.fetchall()]}
        #conn.close()
        return jsonify({'hi':1})


api.add_resource(Radwomen, '/radwomen')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
