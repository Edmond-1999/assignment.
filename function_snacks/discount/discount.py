def apply_discount(item_name, original_price, promo_code):
    promo_code=promo_code.upper()
    if promo_code=="SAVE10":
        discount=original_price*0.10
    elif promo_code=="HALFOFF":
        discount=original_price*0.50
    else:
        discount=0
    return original_price-discount
