from django.shortcuts import render
from .models import Coord
import json
from django.contrib.gis.geos import Point

def index(request):
    return render(request, "index.html")

def saveCoord(request):
    if request.method == "POST":
        coord = request.body
        nostring = str(coord[8:-2])
        nospace = nostring.replace(' ', '')
        points = nospace.split(',')
        point1 = points[0]
        point2 = points[1]
        coord1 = point1[2:]
        coord2 = point2[:-1]
        coords = Coord()
        coords.point = "POINT({0} {1})".format(coord1, coord2)
        coords.save()
    return render(request, "index.html")

def showCoord(request):
    coords = Coord.objects.all().values()
    points = []
    for value in coords:
        points.append(str(value['point']))
    #pointsCoord = dict(enumerate(points))
    #for k in pointsCoord:
        #pointsCoord[str(k)] = pointsCoord.pop(k)
    return render(request, "show.html", context={"points": points})
