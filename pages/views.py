from django.shortcuts import render
from specialLivestockSale.models import SpecialLivestockSale


def index(request, *args, **kwargs):
    return render(request, "home.html", {})


def contactRep_view(request, *args, **kwargs):
    return render(request, "contactRep.html", {})


def salesInfo_view(request, *args, **kwargs):
    specialSale = SpecialLivestockSale.objects.order_by('-sale_date').filter(is_published=True)

    content = {
        'specialSale': specialSale
    }

    return render(request, "salesInfo.html", content)


def otherMarket_view(request, *args, **kwargs):
    return render(request, "otherMarkets.html", {})


def contactUs_view(request, *args, **kwargs):
    return render(request, "contactUs.html", {})


def facility_view(request, *args, **kwargs):
    return render(request, "facility.html", {})


def info_view(request, *args, **kwargs):
    return render(request, "info.html", {})
