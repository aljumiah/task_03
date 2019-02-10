from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
           { "restaurant_name" : "burger", "food_type" : "fast_food"  },
           { "restaurant_name" : "pizza", "food_type" : "fast_food"  },
           { "restaurant_name" : "sub", "food_type" : "fast_food"  }
        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object" : {
            "restaurant_name" : "burger" ,
            "food_type" : "fast_food"
        }
    }
    return render(request, 'detail.html', context)
