from temperature import temperature_advisory

assert temperature_advisory(0,'C',40)=="Cold advisory"
assert temperature_advisory(40,'C',90)=="Heat alert"
assert temperature_advisory(32,'F',10)=="Cold advisory"
assert temperature_advisory(30,'X')=="Invalid unit"

print("temperature tests passed")
