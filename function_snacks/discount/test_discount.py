from discount import apply_discount

assert apply_discount("Book",100,"SAVE10")==90
assert apply_discount("Shoes",200,"HALFOFF")==100
assert apply_discount("Bag",150,"UNKNOWN")==150
assert apply_discount("Phone",1000,"save10")==900

