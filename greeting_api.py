#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, request

app = Flask(__name__)

api = Api(app)


# In[10]:


class Greet(Resource):
    def get(self):

        name = request.args.get('name')

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting)


# In[12]:


# assign endpoint
api.add_resource(Greet, '/greet',)


# In[14]:


if __name__ == '__main__':
    app.run(debug=True)

