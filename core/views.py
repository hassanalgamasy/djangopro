from django.shortcuts import render
# Create your views here.
def home_view(request):

    cards = [
     { 'image': 'img/1c.jpeg',
       'alt': 'شحن سريع',
       'title': 'شحن فوري',
       'text': 'اختر شركه الشحن المناسبه , واطلب شحنتك فى دقائ'
        
     },
     {   'image': 'img/2c.jpeg',
         'alt': 'شحن سريع',
         'title': 'شحن فوري',
         'text': 'اختر شركه الشحن المناسبه , واطلب شحنتك فى دقائ'
     },
     {  'image': 'img/3c.jpeg',
        'alt': 'شحن سريع',
        'title': 'شحن فوري',
        'text': 'اختر شركه الشحن المناسبه , واطلب شحنتك فى دقائ'
     },
     {  'image': 'img/1c.jpeg',
        'alt': 'شحن سريع',
        'title': 'شحن فوري',
        'text': 'اختر شركه الشحن المناسبه , واطلب شحنتك فى دقائ'
   
     },
    ]


    features = [
        {'icon':'fa-shipping-fast', 
         'title':'توصيل سريع', 
         'desc':'توصيل خلال 24 يوميا', 
         'color':'text-primary'},


        {'icon':'fa-credit-card', 
         'title':'طرق دفع متعدده', 
         'desc':'شوف الطريقه اللى تعجبك وادفع بيها ندعم فورى - محافظ الكترونيه - فيزا- تحويل بنكى', 
         'color':'text-success'
        },


        {'icon':'fa-map-marked-alt', 
         'title':'تحديد وتتبع الموقع ', 
         'desc':'حدد موقع وشوف شحنتك فى اى لحظه', 
         'color':'text-danger'
         },

        
        {'icon':'fa-hand-holding-usd', 
        'title':'حصل فلوسك بشكل فورى ', 
        'desc':'ندعم تحصيل الاموال وتصلكم خلال ساعه من التسليم',
        'color':'text-warning'
        },
    ]

    return render(request, 'home.html', {'cards':cards,'features':features})