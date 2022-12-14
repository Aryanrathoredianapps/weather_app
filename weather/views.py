
import requests
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class WeatherView(APIView):
    def get(self, request, *args, **kwargs):
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=02d05140590bc627007f1a0c6cbab13d"
        city_name= self.request.GET.get("city")
        if city_name is not None:
            city_weather = requests.get(url.format(city_name)).json()
            if city_weather.get("cod") == "404":
                return Response(
                    {"message": city_weather.get("message")}, status.HTTP_404_NOT_FOUND
                )

            weather = {
                "city": city_name,
                "temperature": city_weather["main"]["temp"],    
                "description": city_weather["weather"][0]["description"],
                "icon": city_weather["weather"][0]["icon"],
            }
            return Response(weather, status=status.HTTP_201_CREATED)






