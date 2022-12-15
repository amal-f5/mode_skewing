#!/usr/bin/env python3.6
from SpamClassifier import SpamClassifier
from flask import Flask, request, render_template
import flask
app = Flask(__name__)

@app.route("/predict1")
def hello():
    return render_template('user.html')
@app.route("/update_model1")
def hello1():
    return render_template('user_update.html')


@app.route('/update_model', methods=['POST'])
def update_model():
    sms = request.form['SMS']
    # not spam = 0
    label = 0
    classifier.record_feedback(sms, label)
    if len(classifier.new_data) >= 2:
        classifier.re_train()
        classifier.new_data = []
    return render_template('user_update.html', sms_pred="sms marked as NOT SPAM")


@app.route("/predict", methods=['POST'])
def predict(): 
    sms = request.form['SMS']
    print('[+] printing sms: '+sms)
    sms_pred = ''
    if classifier.classify(str(sms)) == 0:
        sms_pred = 'Not spam'
    else:
        sms_pred = 'Spam'

    return render_template('user.html', sms_pred=sms_pred)

def main():
    global classifier 
    classifier = SpamClassifier()
    
#     if __name__ == '__main__':
#         app.run(debug=True)

main()
