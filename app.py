from flask import Flask, render_template, request
import datetime
from datetime import date
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
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Year must be less than 5000 and greater than 1000*")
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
        return render_template('what-day-of-the-week-was-i-born.html', output=classes[date.weekday()], day=day,
                               month=month, year=year)
    except:
        return render_template('what-day-of-the-week-was-i-born.html',
                               message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *',
                               day=day, month=month, year=year)


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
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Length of month/day must be less than 3 *")
        month = int(month)

    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('what-day-of-the-week-was-i-born.html',
                                   message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('what-day-of-the-week-was-i-born.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    try:
        today = datetime.date.today()
        bday = datetime.date(year, month, day)
        output = today - bday
        output = output.days
        output = str(output) + " days!"
        return render_template('how-many-days-have-i-been-alive.html', output=output, day=day, month=month, year=year)
    except:
        return render_template('how-many-days-have-i-been-alive.html',
                               message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *',
                               day=day, month=month, year=year)


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
            return render_template('how-many-minutes-have-i-been-alive.html',
                                   message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-minutes-have-i-been-alive.html',
                                   message="* Length of month/day must be less than 3 *")
        month = int(month)

    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-minutes-have-i-been-alive.html',
                                   message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('how-many-minutes-have-i-been-alive.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    try:
        today = datetime.date.today()
        bday = datetime.date(year, month, day)
        output = today - bday
        output = output.days
        output = output * 1440
        output = str(output) + " minutes!"
        return render_template('how-many-minutes-have-i-been-alive.html', output=output, day=day, month=month,
                               year=year)
    except:
        return render_template('how-many-minutes-have-i-been-alive.html',
                               message='* An error occured! Make sure that you have not inputted a non-existant month, day or year number! *',
                               day=day, month=month, year=year)


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
            return render_template('how-many-seconds-have-i-been-alive.html',
                                   message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-seconds-have-i-been-alive.html',
                                   message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-seconds-have-i-been-alive.html',
                                   message="* Year must be less than 5000 and greater than 1000*", day=day, month=month,
                                   year=year)
    except:
        return render_template('how-many-seconds-have-i-been-alive.html', message="* Do not input words *")
    print(day)
    print(month)
    print(year)
    # try:
    today = datetime.date.today()
    bday = datetime.date(year, month, day)
    output = today - bday
    output = output.days
    output = output * 84600
    output = str(output) + " seconds!"
    return render_template('how-many-seconds-have-i-been-alive.html', output=output, day=day, month=month, year=year)


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
            return render_template('how-many-times-your-heart-has-beaten.html',
                                   message="* Length of month/day must be less than 3 *")
        day = int(day)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")
    month = request.form['namequery2']
    try:
        if month[0] == 0:
            month = month[1]
            print(month)
        if len(month) > 2:
            return render_template('how-many-times-your-heart-has-beaten.html',
                                   message="* Length of month/day must be less than 3 *")
        month = int(month)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")
    year = request.form['namequery3']
    try:
        year = int(year)
        if int(year) >= 5000 or year < 1000:
            print('Er')
            return render_template('how-many-times-your-heart-has-beaten.html',
                                   message="* Year must be less than 5000 and greater than 1000*")
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', message="* Do not input words *")

    try:
        today = datetime.date.today()
        bday = datetime.date(year, month, day)
        output = today - bday
        output = output.days
        output = output * 1440
        output = output * 70
        output = str(output) + " times!"
        return render_template('how-many-times-your-heart-has-beaten.html', output=output, day=day, month=month,
                               year=year)
    except:
        return render_template('how-many-times-your-heart-has-beaten.html', day=day, month=month, year=year,
                               message='* An error occured, make sure that the date you have inputted actually exists! *')

@app.route('/how-much-food-have-i-eaten-in-my-life-calculator')
def routeit():
    return render_template('how-much-food-have-i-eaten-in-my-life.html')
@app.route('/how-much-food-have-i-eaten-in-my-life-calculator', methods=['POST'])
def routeit2():
    difference = 1
    if 1 == 1:
        # date1 = day date2 = month date3 = year
        # format = (year, month, day)
        date1 = request.form['date1']
        date2 = request.form['date2']
        date3 = request.form['date3']
        if len(date1) > 10 or len(date2) > 10 or len(date3) > 10:
            return render_template('how-much-food-have-i-eaten-in-my-life.html', message='Whoops! You entered a date that does not exist!')

        difference = datetime.date.today() - datetime.date(int(date3), int(date2), int(date1))

        difference = str(difference)
        final_difference = ""
        for char in difference:
            if char == " ":
                break
            else:
                final_difference += char
        print(final_difference)
        difference = int(final_difference) * 4
        difference = str(difference) + " food pounds."
        return render_template('how-much-food-have-i-eaten-in-my-life.html', difference = difference, day = date1, month = date2, year = date3)
    else:
        return render_template('how-much-food-have-i-eaten-in-my-life.html', message='Whoops! Make sure the date you entered actually exists!')
@app.route('/how-many-pounds-of-food-does-a-dog-eat-in-its-life')
def howmanypoundsoffooddoesadogeatinitslifetime():
    return render_template('howmanypoundsoffooddoesadogeatinitslife.html')
@app.route('/how-many-pounds-of-food-does-a-dog-eat-in-its-life', methods=['POST'])
def howmanypoundsoffooddoesadogeatinitslifetime2():
    try:
        dogday = request.form['date1']
        dogmonth = request.form['date2']
        dogyear = request.form['date3']
        if len(dogday) > 10 or len(dogmonth) > 10 or len(dogyear) > 10:
            return render_template('howmanypoundsoffooddoesadogeatinitslife.html',
                               message='Whoops! You entered a date that does not exist!')
        difference = datetime.date.today() - datetime.date(int(dogyear), int(dogmonth), int(dogday))
        difference = str(difference)
        print(difference)
        final_difference = ""
        for char2 in difference:
            if char2 == " ":
                break
            final_difference += char2
        if int(final_difference) >= 35:
            alternative_suprise = "Woah! This dog has lived for a long time!"
        final_difference = int(final_difference) * 2
        final_difference = str(final_difference) + " food pounds"
        print(final_difference)
        return render_template('howmanypoundsoffooddoesadogeatinitslife.html', difference2 = final_difference, day = dogday, month = dogmonth, year = dogyear, alternative_suprise = alternative_suprise)
    except:
        return render_template('howmanypoundsoffooddoesadogeatinitslife.html', usermessage = "The date you inputted is either invalid or does not exist. Sorry!")
@app.route('/how-much-food-does-a-horse-eat-in-its-lifetime')
def howmuchfooddoesahorseeatinitslifetime():
    return render_template('howmanypoundsoffooddoesahorseeatinitslifetimecalculator.html')
@app.route('/how-much-food-does-a-horse-eat-in-its-lifetime', methods=['POST'])
def howmuchfooddoesahorseeatinitslifetime2():
    if 1 == 1:
        horseday = request.form['date1']
        horsemonth = request.form['date2']
        horseyear = request.form['date3']
        if len(horseday) > 10 or len(horsemonth) > 10 or len(horseyear) > 10:
            return render_template('howmanypoundsoffooddoesahorseeatinitslifetimecalculator.html',
                                   usermessage='Whoops! You entered a date that does not exist!')
        horsediff = datetime.date.today() - datetime.date(int(horseyear), int(horsemonth), int(horseday))
        horsefinaldiff = ""
        for char3 in str(horsediff):
            if char3 == " ":
                break
            horsefinaldiff += char3
        if int(horsefinaldiff) > 7000:
            funny_message = "Woah! That horse is old! Scroll down for more information!"
        else:
            funny_message = ""
        horsefinaldiff = int(horsefinaldiff) * 16
        return render_template('howmanypoundsoffooddoesahorseeatinitslifetimecalculator.html', final_result = str(horsefinaldiff) + " food pounds!", day = horseday, month = horsemonth, year = horseyear, alternative_suprise = funny_message)
    else:
        return render_template('howmanypoundsoffooddoesahorseeatinitslifetimecalculator.html',
                        usermessage='Whoops! You entered a date that does not exist!')
@app.route('/how-much-food-does-a-cat-eat-in-its-lifetime')
def howmuchfooddoesacateatinitslifetime():
    return render_template('howmanypoundsoffooddoesacateatinitslifetime.html')
@app.route('/how-much-food-does-a-cat-eat-in-its-lifetime', methods=['POST'])
def howmuchfooddoesacateatinitslifetime2():
    catday = request.form['date1']
    catmonth = request.form['date2']
    catyear = request.form['date3']
    if len(catmonth) > 10 or len(catday) > 10 or len(catyear) > 10:
        return render_template('howmanypoundsoffooddoesacateatinitslifetime.html',
                               usermessage='Whoops! You entered a date that does not exist!')
    catdiff = datetime.date.today() - datetime.date(int(catyear), int(catmonth), int(catday))
    print(catdiff)
    catdiff = str(catdiff)
    finalcatdiff = ""
    for char5 in catdiff:
        if char5 == " ":
            break
        finalcatdiff += char5
    finalcatdiff = str(finalcatdiff) + " food pounds!"
    return render_template('howmanypoundsoffooddoesacateatinitslifetime.html', day = catday, month= catmonth, year = catyear, final_result = finalcatdiff)
@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.xml')


if __name__ == "__main__":
    app.run(debug=True)
