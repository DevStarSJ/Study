#-*- coding: utf-8 -*-
import urllib.request
from datetime import datetime
import pytz
from bs4 import BeautifulSoup


class Weather():

    @staticmethod
    def get_text():
        url = "http://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=09230109"
        page = urllib.request.urlopen(url)
        weather = BeautifulSoup(page, "html.parser")

        today = datetime.now(pytz.timezone('Asia/Seoul')).strftime("%Y년 %m월 %d일")
        text = "{} 오늘 날씨\n".format(today)

        for cell in weather.find_all("div", "cell", limit=2):
            when = cell.find("b").string # 오전, 오후
            temperature = cell.find("span", "temp").string
            weather = cell.img['alt']
            rain = cell.find("strong").string
            text += "{}: {}℃, {}, 강수 확률 {}%\n".format(when, temperature, weather, rain)

        return text

if __name__ == "__main__":
    w = Weather()
    print(w.get_text())
