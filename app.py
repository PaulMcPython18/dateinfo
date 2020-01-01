from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/date-time-birthday-calculator')
def date_time_birthday_calculator():
    return render_template('Date-Info-Birthday-Calculator.html')
@app.route('/what-day-of-the-week-am-i-born')
def whatdayoftheweekwasiborn():
    current_time = datetime.datetime.now()
    print(current_time)
    current_time = str(current_time)
    current_year = current_time[0:4]
    current_month = current_time[5:7]
    current_day = current_time[8:10]
    current_time = str(current_month) + "/" + str(current_day) + "/" + str(current_year)
    print(current_time)
    return render_template('what-day-of-the-week-was-i-born.html', current_time=current_time)
@app.route('/what-day-of-the-week-am-i-born', methods=['POST'])
def one():
    day = request.form['namequery1']
    try:
        if day[0] == 0:
            day = day[1]
            print(day)
        if len(day) > 2:
            return render_template('what-day-of-the-week-was-i-born.html', message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('what-day-of-the-week-was-i-born.html', message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('what-day-of-the-week-was-i-born.html', message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    try:
        date = datetime.datetime(year, month, day)
        classes = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        print(date)
        print(classes[date.weekday()])
        return render_template('what-day-of-the-week-was-i-born.html', output=classes[date.weekday()], day = day, month=month, year=year)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *', day = day, month=month, year=year)
@app.route('/how-many-days-have-i-been-alive')
def how_many_days_have_i_been_alive():
    return render_template('how-many-days-have-i-been-alive.html')
@app.route('/how-many-days-have-i-been-alive', methods=['POST'])
def how_many_days_have_i_lived():
    day = request.form['namequery1']
    try:
        if day[0] == 0:
            day = day[1]
            print(day)
        if len(day) > 2:
            return render_template('what-day-of-the-week-was-i-born.html', message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('what-day-of-the-week-was-i-born.html', message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('what-day-of-the-week-was-i-born.html', message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    try:
        today = datetime.date.today()
        bday = datetime.date(year, month, day)
        output = today-bday
        output = output.days
        output = str(output) + " days!"
        return render_template('how-many-days-have-i-been-alive.html', output=output, day = day, month=month, year=year)
    except:
        return render_template('how-many-days-have-i-been-alive.html', message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *', day = day, month=month, year=year)
@app.route('/how-many-minutes-have-i-been-alive')
def how_many_minutes_have_i_been_alive():
    return render_template('how-many-minutes-have-i-been-alive.html')
@app.route('/how-many-minutes-have-i-been-alive', methods=['POST'])
def how_many_minutes_have_i_lived():
    day = request.form['namequery1']
    try:
        if day[0] == 0:
            day = day[1]
            print(day)
        if len(day) > 2:
            return render_template('how-many-minutes-have-i-been-alive.html', message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-minutes-have-i-been-alive.html', message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-minutes-have-i-been-alive.html', message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    # try:
    today = datetime.date.today()
    bday = datetime.date(year, month, day)
    output = today-bday
    output = output.days
    output = output * 1440
    output = str(output) + " minutes!"
    return render_template('how-many-minutes-have-i-been-alive.html', output=output,day =day, month=month, year=year)
    # except:
    #     return render_template('how-many-minutes-have-i-been-alive.html', message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *', day = day, month=month, year=year)
@app.route('/how-many-seconds-have-i-been-alive')
def how_many_seconds_have_i_been_alive():
    return render_template('how-many-seconds-have-i-been-alive.html')
@app.route('/how-many-seconds-have-i-been-alive', methods=['POST'])
def how_many_seconds_have_i_lived():
    day = request.form['namequery1']
    try:
        if day[0] == 0:
            day = day[1]
            print(day)
        if len(day) > 2:
            return render_template('how-many-seconds-have-i-been-alive.html', message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-seconds-have-i-been-alive.html', message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-seconds-have-i-been-alive.html', message="* Year must be less than 5000 and greater than 1000*", day=day, month=month, year=year)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    # try:
    today = datetime.date.today()
    bday = datetime.date(year, month, day)
    output = today-bday
    output = output.days
    output = output * 84600
    output = str(output) + " seconds!"
    return render_template('how-many-seconds-have-i-been-alive.html', output=output,day =day, month=month, year=year)
@app.route('/how-many-times-your-heart-has-beaten')
def how_many_times_your_heart_has_beaten():
    return render_template('how-many-times-your-heart-has-beaten.html')
@app.route('/how-many-times-your-heart-has-beaten', methods=['POST'])
def how_many_times_your_heart_has_beat():
    day = request.form['namequery1']
    try:
        if day[0] == 0:
            day = day[1]
            print(day)
        if len(day) > 2:
            return render_template('how-many-times-your-heart-has-beaten.html', message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-times-your-heart-has-beaten.html', message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-times-your-heart-has-beaten.html', message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")

    try:
        today = datetime.date.today()
        bday = datetime.date(year, month, day)
        output = today-bday
        output = output.days
        output = output * 1440
        output = output * 70
        output = str(output) + " times!"
        return render_template('how-many-times-your-heart-has-beaten.html', output=output,day =day, month=month, year=year)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', day=day, month=month, year=year, message='* An error occured, make sure that the date you have inputted actually exists! *')
@app.route('/sitemap)
def sitemap():
    return render_template('sitemap.xml')
if __name__ == "__main__":
    app.run(debug=True)
