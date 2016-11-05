# -*-coding:utf-8-*-
from flask import Flask
from flask import render_template
from flask import request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import config


def send(message='', subject=''):
    """发送邮件"""
    try:
        mail_server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        mail_server.login(config['sender'], config['password'])
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = config['sender']
        # msg['CC'] = config['receivers']
        part = MIMEText(message, 'html', _charset='utf-8')
        msg.attach(part)
        mail_server.sendmail(config['sender'], config['receivers'], msg.as_string())
        print "Successfully sent email"
        mail_server.quit()
    except smtplib.SMTPException as e:
        print e
        print "Error: unable to send email"


app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/svn_copy")
def svn_copy():
    version = request.form['version']
    return "branch_url"


@app.route("/launch", methods=['POST'])
def launch():
    version = request.form['version']
    revision = request.form['revision']
    branch_url = request.form['branch_url']
    mysql = request.form['mysql']
    redis = request.form['redis']
    preheat = request.form['preheat']
    other = request.form['other']
    # function = request.form['function']
    message = u'''
    【revision】{revision}<br/>
    【tag】{branch_url}<br/>
    【mysql修改】{mysql}<br/>
    【redis修改】{redis}<br/>
    【预热接口】{preheat}<br/>
    【其他注意事项】{other}<br/>
    '''.format(revision=revision, branch_url=branch_url, mysql=mysql, redis=redis, preheat=preheat, other=other)
    print message
    send(message, u'【上线】' + version)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
