


def data_valid(n, p, k, tem, hum, ph, rain):
    if((float(n)>=0 and float(n)<=255) and (float(p)>=0 and float(p)<=255) and (float(k)>=0 and float(k)<=255) and (float(rain)>=0 and float(rain)<=300) and (float(tem)>=-5 and float(tem)<=55) and (float(hum)>=0 and float(hum)<=100) and (float(ph)>=5 and float(ph)<=9)):
        return True
    else:
        return False
