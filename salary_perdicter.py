def predict_rub_salary(payment_from, payment_to): 
    if payment_to and payment_from:
        return (payment_from + payment_to)/2
    if payment_to:
        return payment_to*0.8
    if payment_from :
        return payment_from*1.2
    

