from flask import Flask,request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/temperature",methods=['POST','GET'])
def temperature():

    if request.method=='POST':
        name= request.form['city']


    from requests_html import HTMLSession

    s= HTMLSession()
    # city = input("Enter City Name: ")
    url = f'https://www.google.com/search?q=weather+{name}'

    r = s.get(url)

    #temperature and unit
    temp = r.html.find("span#wob_tm", first=True).text
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
    # print(temp,unit)

    #humidity
    humidity = r.html.find("span#wob_hm", first=True).text
    # print(humidity)

    #infoabout how was the day
    desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text
    # print(desc)

    #perception
    perception = r.html.find("span#wob_pp", first=True).text
    # print(perception)

    #wind flow rate
    wind = r.html.find("span#wob_ws", first=True).text
    # print(wind)

    #Air Quality index
    from requests_html import HTMLSession

    s2= HTMLSession()

    url2 = f'https://www.accuweather.com/en/in/{name}/189287/air-quality-index/189287'

    r2 = s2.get(url2)

    #air_pollution
    Air_polution = r2.html.find("div.aq-number-container", first=True).find("div.aq-number", first=True).text
    Air_polution_unit = r2.html.find("div.aq-number-container", first=True).find("div.aq-unit", first=True).text
    # print(Air_polution, Air_polution_unit)


    #pollutants
    PM10 = r2.html.find("div.air-quality-pollutant", first=True).find("h3.column", first=True).text
    # print("Partculate Matter :", PM10)

    pollutant_index = r2.html.find("div.column.mobile-middle", first=True).find("div.pollutant-index", first=True).text
    pollutant_concent = r2.html.find("div.column.mobile-middle", first=True).find("div.pollutant-concentration", first=True).text
    # print(pollutant_index)
    # print(pollutant_concent)
    return render_template("Temperature.html",variable1=temp,variable2=unit,variable3=humidity,variable4=desc,variable5=perception,variable6=wind,variable7=Air_polution,variable8=Air_polution_unit,variable9=PM10,variable11=pollutant_index,variable12=pollutant_concent)


if __name__=='__main__':
    app.run(debug=True)




    