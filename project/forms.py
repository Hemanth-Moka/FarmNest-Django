from urllib import request


class PaymentForm:
    pass


form = PaymentForm(request.POST)
if form.is_valid():
    form.save()  # This should save the data
else:
    print(form.errors)  # This will show any validation errors
