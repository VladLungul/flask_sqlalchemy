from flask import Flask, render_template, request, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   text = db.Column(db.Text, nullable=False)

   
@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      pass
   posts = Post.query.all()
   return render_template('index.html', posts=posts)

   
if __name__ == '__main__':
   app.run(debug=True)
