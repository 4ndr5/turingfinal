import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

@app.route("/")
def index():
  return render_template ('index.html')

@app.route("/register")
def register():
  return render_template("/register.html")
