from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = "Cox-Bazar"
    dest1.desc = "This beach is bangladesh heart"
    dest1.img='destination_1.jpg'
    dest1.price = "From 700 Tk"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Kuakata"
    dest2.desc = "This beach is bangladesh Mind"
    dest2.img='destination_2.jpg'
    dest2.price = "From 900 Tk"
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Kuakata"
    dest3.desc = "This beach is bangladesh Mind"
    dest3.img='destination_3.jpg'
    dest3.price = "From 500 Tk"
    dest3.offer = False


    dests = [dest1,dest2,dest3]



    return render(request, "index.html", {'dests': dests})
