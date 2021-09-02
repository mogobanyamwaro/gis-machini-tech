from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom
import folium
# Create your views here.


def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    print(obj)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')
    ip = '14.137.168.0'
    # kisii = '41.89.196.0'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # initial folium map
    m = folium.Map(width=800, height=500,
                   location=get_center_coordinates(l_lat, l_lon), zoom_start=8)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        operation = form.cleaned_data.get('operation')
        description = form.cleaned_data.get('description')
        codeName = form.cleaned_data.get('codeName')
        serviceNumber = form.cleaned_data.get('serviceNumber')
        station = form.cleaned_data.get('station')
        destination = geolocator.geocode(destination_)
        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

 # folium map modification
        m = folium.Map(width=800, height=500, location=get_center_coordinates(
            l_lat, l_lon, d_lat, d_lon), zoom_start=get_zoom(distance))

        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                      icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        popup1 = "Operation : {} <br/> Code Name :{} <br> service No:{} <br> Station :{}".format(
            operation, codeName, serviceNumber, station)
        iframe = folium.IFrame(popup1,
                               width=300,
                               height=100)

        popup = folium.Popup(iframe,
                             max_width=300)

        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=popup,
                      icon=folium.Icon(color='red', icon='cloud')).add_to(m)

        instance.location = location
        instance.distance = 20
        instance.save()
    m = m._repr_html_()
    context = {
        # 'distance': distance,
        # 'destination': destination,
        'form': form,
        'map': m,
    }
    return render(request, 'measurements/main.html', context)
