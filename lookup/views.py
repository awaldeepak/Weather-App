from django.shortcuts import render

def home(request):
	import json
	import requests
	
	if request.method == "POST":
		zipcode = request.POST['zipcode'] #This is getting from base.html file i.e input form zipcode
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=5EFE6D5C-B4A5-4E6A-AB61-864146C896BA")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error Getting Data..."

		category = api[0]['Category']['Name']

		if category == "Good":
			category_desc = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif category == "Moderate":
			category_desc = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif category == "Unhealthy for Sensitive Groups":
			category_desc = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			category_color = "usg"
		elif category == "Unhealthy":
			category_desc = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif category == "Very Unhealthy":
			category_desc = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif category == "Hazardous":
			category_desc = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api':api,
			'category': category,
			'category_desc': category_desc,
			'category_color': category_color
			})
		#return render(request, 'home.html', {'zipcode': zipcode}) #This zipcode, we're passing above value to the home.html file in zipcode paramter
	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=5EFE6D5C-B4A5-4E6A-AB61-864146C896BA")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error Getting Data..."

		category = api[0]['Category']['Name']

		if category == "Good":
			category_desc = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif category == "Moderate":
			category_desc = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif category == "Unhealthy for Sensitive Groups":
			category_desc = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
			category_color = "usg"
		elif category == "Unhealthy":
			category_desc = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif category == "Very Unhealthy":
			category_desc = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"
		elif category == "Hazardous":
			category_desc = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api':api,
			'category': category,
			'category_desc': category_desc,
			'category_color': category_color
			})

def about(request):
	return render(request, 'about.html', {})