from flask import Flask, render_template, request, send_from_directory, url_for, flash, redirect
import psycopg2
from flask import redirect


hostname = 'localhost'
database = 'telecom'
username = 'postgres'
pwd = '291627daniyaR'
port_id = 5432


conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id
)
cur = conn.cursor()


create_script = ''' create table if not exists register (
Email varchar(50),
Password varchar(50),
Position varchar(50)
) '''
cur.execute(create_script)
conn.commit()


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('index.html' )

@app.route('/admin', methods = ['GET', 'POST'])
def panel():
    txt = "Вы неправильно ввели данные!"
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        Position = 'Admin'
        select = 'SELECT Email, Password, Position FROM register'
        cur.execute(select)
        select_all = cur.fetchall()
        print(select_all)
        for i in select_all:
            if Email == i[0]:
                check_one = 1
            else:
                check_one = 0
        for i in select_all:
            if Password == i[1]:
                check_two = 1
            else:
                check_two = 0
        check_three = check_two + check_one
        if check_three == 2:
            for i in select_all:
                if Position == i[2]:
                    return render_template('admin.html')
                else:
                    return redirect(url_for("main_page"))
        else:
            return redirect(url_for('main', word=txt))
@app.route('/main', methods = ['GET', 'POST'])
def main_page():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True)