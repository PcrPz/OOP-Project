#rentcar
class Booking:
    def __init__(self,start_date,end_date,status):
        self.start_date=start_date
        self.end_date=end_date
        self.status = status
        
class Categorie:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
class CarGas:
    def __init__(self,seat,rating,fuel_type,show_price,door,insurance,fuel_used,photo_car,feature_car):
        self.seat=seat
        self.rating=rating
        self.fuel_type=fuel_type
        self.show_price = show_price
        self.door = door
        self.insurance=insurance
        self.fuel_used=fuel_used
        self.photo_car= photo_car
        self.feature_car={feature_car}
        
class CarEV:
    def __init__(self,seat,rating,fuel_type,show_price,door,insurance,photo_car):
        self.seat=seat
        self.rating=rating
        self.fuel_type=fuel_type
        self.show_price = show_price
        self.door = door
        self.insurance=insurance
        self.photo_car= photo_car
        
        
class Owner:
    def __init__(self,name,email,phone_num,photo,trip,veryfying,description,parkingdetails,guidline):
        self.trip = trip
        self.veryfying = veryfying
        self.name=name
        self.email=email
        self.phone_num=phone_num
        self.photo=photo
        
class Renter:
    def __init__(self,age,name,email,phone_num,photo,driver_license_status):
        self.age=age
        self.name=name
        self.email=email
        self.phone_num=phone_num
        self.photo=photo
        self.driver_license_status=driver_license_status
        
class Payment:
    def __init__(self,amount,transaction_id,payment_status,time):
        self.amount = amount
        self.created_on = time
        self.transaction_id = transaction_id
        self.status = payment_status
        
class Rating:
    def __init__(self,rating,name,date,description):
        self.rating = rating
        self.name = name
        self.date = date
        self.description = description
        
class Avgfeedback:
    def __init__(self,avgrating,avgcomment):
        self.avgrate = avgrating
        self.avgcomment = avgcomment
        
class Rentlocation:
    def __init__(self,address):
        self.address = address
        

        

        
        