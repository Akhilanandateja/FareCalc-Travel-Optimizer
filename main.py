rates={
    "Economy":10,
    "Premium":20,
    "SUV":25
}
def calculate_fare(km,type,hour):
    base=rates[type]*km
    if hour>=17 and hour<=20:
        base=base*1.5
    return round(base,2)
print("===== CAB FARE CALCULATOR =====")
try:
    km=float(input("Enter distance in km: "))
    type=input("Enter vehicle type as Economy/Premium/SUV: ")
    hour=int(input("Enter hour: "))
    if km<=0:
        print("Please enter a valid distance greater than 0 km")
        exit()
    if hour<0 or hour>23:
        print("Please enter a valid hour between 0-23")
        exit()
    type=type.capitalize()
    if type not in rates:
        print("Service not available for the selected vehicle type")
    else:
        base_fare=rates[type]*km
        total_fare=calculate_fare(km,type,hour)
        if km>20:
            print("Long distance discount is applied")
            total_fare=total_fare*0.9
        if total_fare<50:
            print("Minimum fare charges applied: Rs. 50")
            total_fare=50
        print("\n===== RECEIPT =====")
        print("Distance:",km,"km")
        print("Vehicle:",type)
        print("Time:",hour)
        print("Base Fare:",base_fare)
        if hour>=17 and hour<=20:
            print("Peak Hour Surcharge Applied: YES")
        else:
            print("Peak Hour Surcharge Applied: NO")
        print("Total Fare:",round(total_fare,2))
except ValueError:
    print("Invalid input, enter a numeric input")