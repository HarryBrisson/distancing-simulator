import datetime

import requests

def get_historical_data(country="all"):
	r = requests.get(f'https://corona.lmao.ninja/v2/historical/{country}')
	return r.json()

def get_date_from_today(offset=0,fmt='%-m/%-d/%y'):
  today = datetime.datetime.now()
  targetDay = today + datetime.timedelta(offset)
  targetDayString = datetime.datetime.strftime(targetDay,fmt)
  return targetDayString

def get_death_daily_increase_rate(country="all"):
	data = get_historical_data(country=country)
	yday = get_date_from_today(offset=-1)
	week_before_yday = get_date_from_today(offset=-8)
	print(country)
	if country != "all":
		data = data['timeline']
	daily_growth = (data['deaths'][yday]/data['deaths'][week_before_yday])**(1/7)
	return daily_growth

def get_yesterdays_deathcount(country="all"):
	data = get_historical_data(country=country)
	yday = get_date_from_today(offset=-1)
	if country != "all":
		data = data['timeline']
	return data['deaths'][yday]

if __name__ == "__main__":
	rate = get_death_daily_increase_rate()
	print(rate) 