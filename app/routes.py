from app import app
from flask import render_template, redirect, url_for
from Autocoder.Autocoder import Autocoder
from app.forms import MainForm
from app.forms import ParametersForm
from app.parsing import get_img


a = Autocoder(8, 5)
i = 8
o = 5


@app.route('/', methods=['GET', 'POST'])
def start():
    global a
    global i
    global o
    form = MainForm()
    params = ParametersForm()
    answer = ''
    if params.validate_on_submit():
        i = int(params.inp.data)
        o = int(params.out.data)
        a = Autocoder(i, o)
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
                a = Autocoder(i, o)
                answer = 'I know nothing :)'
    except Exception as e:
        if str(e) == 'incorrect size!':
            answer = 'Incorrect size! >_<'
        else:
            answer = 'I can\'t :('
    img = get_img()
    return render_template('main_page.html', form=form, params=params, ans=answer, i=i, o=o, img=img)


@app.route('/learn/<string:string>')
def learn(string):
    a.learn(string)
    return redirect('/')
