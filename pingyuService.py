import json
import openai
import os
from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS
app = Flask(__name__)
##r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      print(1)
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      print(2)
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/push',methods = ['GET'])
def push():
    ##43.155.168.85
    keyword = request.args.get('kw')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_engine = "gpt-3.5-turbo"
    # model_engine = "text-davinci-003"
    # prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段评语，关键词是上课爱讲话、体育比较差"
    prompt = "小学班主任每个学期都要给学生写评语。请你帮忙给某个小学生写一段不少于100个汉字的评语，关键词是%s." % (keyword)
    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message.content

    returnMSG=json.dumps({"code":200,"msg":'',"data":result})
    return (returnMSG)


if __name__ == '__main__':

    app.run(host="0.0.0.0",port=5002)

    print("come on ")
