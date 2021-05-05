from app import app
from flask import render_template, redirect, url_for
from Autocoder.Autocoder import Autocoder
from app.forms import MainForm
from app.forms import ParametersForm

a = Autocoder(8, 5)


@app.route('/', methods=['GET', 'POST'])
def start():
    global a
    form = MainForm()
    params = ParametersForm()
    answer = ''
    if params.validate_on_submit():
        a = Autocoder(int(params.inp.data), int(params.out.data))
    try:
        if form.validate_on_submit():
            if form.remember.data:
                a.learn(form.text.data)
                answer = 'Yup'
            if form.ask.data:
                answer = a.decode(a.encode(form.text.data))
            if form.code.data:
                answer = a.encode(form.text.data)
            if form.forget.data:
                a = Autocoder(8, 5)
                answer = 'I know nothing :)'
    except Exception as e:
        if str(e) == 'incorrect size!':
            answer = 'Incorrect size! >_<'
        else:
            answer = 'I can\'t :('

    return render_template('main_page.html', form=form, params=params, ans=answer)


@app.route('/learn/<string:string>')
def learn(string):
    a.learn(string)
    return redirect('/')
