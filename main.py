rates={
    "Economy":10,
    "Premium":20,
    "SUV":25
}
def calculate_fare(km,type,hour):
    base=rates[type]*km
    surge_charge=0
    if hour>=17 and hour<=20:
        surge_charge=base*0.5
        base=base+surge_charge
    return round(base,2),round(surge_charge,2)
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
    type=type.strip().lower()
    if type=="economy":
        type="Economy"
    elif type=="premium":
        type="Premium"
    elif type=="suv":
        type="SUV"
    if type not in rates:
        print("Service not available for the selected vehicle type")
    else:
        base_fare=rates[type]*km
        total_fare,surge_charge=calculate_fare(km,type,hour)
        discount=0
        discount_applied=False
        if km>=20:
            discount=total_fare*0.1
            total_fare=total_fare-discount
            discount_applied=True
        min_fare=False
        if total_fare<50:
            total_fare=50
            min_fare=True
        print("\n===== RECEIPT =====")
        print("Distance:",km,"km")
        print("Vehicle:",type)
        print("Time:",hour)
        print("Base Fare: Rs.",base_fare)
        if discount_applied:
            print("--Long distance discount is applied: - Rs.",round(discount,2))
        if min_fare:
            print("--Minimum fare charges applied")
        if surge_charge>0:
            print("--Peak Hour Surcharge Applied: + Rs.",round(surge_charge,2))
        print("Total Fare: Rs.",round(total_fare,2))
except ValueError:
    print("Invalid input, enter a numeric input")