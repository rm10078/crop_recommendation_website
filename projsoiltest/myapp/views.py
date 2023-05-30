from django.shortcuts import render,HttpResponse,redirect
from myapp import finalproject_random_forrest,help

# all_emo={
#     "rice":"🌾",
#     "maize":"🌽",
#     "chickpea":"🌱",
#     "kidney beans":"🥫",
#     "pigeonpea":"🕊️",
#     "mothbean":"🌱",
#     "mungbean":"🌱",
#     "blackgram":"🌱",
#     "barley":"🌾",
#     "jute":"🌾",
#     "mango":"🥭",
#     "banana":"🍌",
#     "grapes":"🍇",
#     "pomegrante":"🍎",
#     "watermelon":"🍉",
#     "muskmelon":"🍈",
#     "apple":"🍏",
#     "orange":"🍊",
#     "papaya":"🍑",
#     "cotton":"🌾"
# }

all_emo={
    "rice":"static/all_crop_img/rice.jpg",
    "maize":"static/all_crop_img/maize.png",
    "chickpea":"static/all_crop_img/chickpea.png",
    "kidney beans":"static/all_crop_img/kidney_beans.png",
    "pigeonpea":"static/all_crop_img/pigeonpea.png",
    "mothbean":"static/all_crop_img/mothbean.png",
    "mungbean":"static/all_crop_img/mungbean.png",
    "blackgram":"static/all_crop_img/blackgram.png",
    "barley":"static/all_crop_img/barley.png",
    "jute":"static/all_crop_img/jute.png",
    "mango":"static/all_crop_img/mango.png",
    "banana":"static/all_crop_img/banana.png",
    "grapes":"static/all_crop_img/grapes.png",
    "pomegrante":"static/all_crop_img/pomegrante.png",
    "watermelon":"static/all_crop_img/watermelon.png",
    "muskmelon":"static/all_crop_img/muskmelon.png",
    "apple":"static/all_crop_img/apple.png",
    "orange":"static/all_crop_img/orange.png",
    "papaya":"static/all_crop_img/papaya.png",
    "cotton":"static/all_crop_img/cotton.png",
    "error":"static/all_crop_img/error.png"
}



# Create your views here.
def mainPage(request):
    if request.method=='POST':
        n=request.POST.get('n')
        p=request.POST.get('p')
        k=request.POST.get('k')
        tem=request.POST.get('tem')
        hum=request.POST.get('hum')
        ph=request.POST.get('ph')
        rain=request.POST.get('rain')
        if n=='' or p=='' or k=='' or tem=='' or hum=='' or ph=='' or rain=='':
            return redirect(mainPage)
        if help.data_valid(n, p, k, tem, hum, ph, rain):
            crop_result=finalproject_random_forrest.predict_with_random_forest(n, p, k, tem, hum, ph, rain)
            return render(request, 'result.html',{'n':n,'p':p,'k':k,'tem':tem,'hum':hum,'ph':ph,'rain':rain,'rec':crop_result,'img':all_emo[crop_result]}) #N,P,K,temperature,humidity,ph,rainfall     nitrogen, phosphorus, and potassium
        else:
            return render(request, 'result.html',{'n':n,'p':p,'k':k,'tem':tem,'hum':hum,'ph':ph,'rain':rain,'rec':"to take no action because your input data is out of range.",'img':all_emo["error"]})
    else:
        return render(request, 'main.html') #N,P,K,temperature,humidity,ph,rainfall     nitrogen, phosphorus, and potassium