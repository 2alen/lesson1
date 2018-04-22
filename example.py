def get_vat(payment, percent=18):
    try:
        payment = float(payment)
        vat = payment / 100 * percent
        vat = round(vat,2)
        return "VAT summ is {}".format(vat )
    except (TypeError, ValueError):
        return "Incorrect input type!"

result = get_vat(76)
print(result)

result = get_vat(76,12)
print(result)