from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
arquivo_bd = os.path.join(path, 'personagens.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivo_bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
