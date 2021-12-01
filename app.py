from flask import Flask,jsonify,render_template
app = Flask(__name__)
import requests
import  bs4
def get_html_deta(url):
    deta=requests.get(url)
    return deta

@app.route('/')
def get_corona():
    url = "https://www.mohfw.gov.in/"
    htmo_deta=get_html_deta(url)
    bs=bs4.BeautifulSoup(htmo_deta.text,'html.parser')
    info_div=bs.find("div",class_="col-xs-8 site-stats-count").find_all("span",class_="mob-show")
    b=info_div[2]
    count=b.find("strong").get_text()
    b=info_div[5]
    count2=b.find("strong").get_text()
    b=info_div[8]
    count3=b.find("strong").get_text()
    return render_template("index.html",count=count,count2=count2,count3=count3)
@app.route('/covid')
def method_name():
    url = "https://www.mohfw.gov.in/"
    htmo_deta=get_html_deta(url)
    bs=bs4.BeautifulSoup(htmo_deta.text,'html.parser')
    info_div=bs.find("div",class_="col-xs-8 site-stats-count").find_all("span",class_="mob-show")
    b=info_div[2]
    count=b.find("strong").get_text()
    b=info_div[5]
    count2=b.find("strong").get_text()
    b=info_div[8]
    count3=b.find("strong").get_text()
    return jsonify(
        active=count,
        discharge=count2,
        death=count3
    )
if __name__ == '__main__':
    app.run(debug=True,port=7000)