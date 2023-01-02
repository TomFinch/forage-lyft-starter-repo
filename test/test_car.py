from car import CarFactory
from datetime import datetime

def create_test():
    test_calliope_no_service()
    test_calliope_service()
    test_glissade_no_service()
    test_glissade_service()
    test_palindrome_no_service()
    test_palindrome_service()
    test_rorschach_no_service()
    test_rorschach_service()
    test_thovex_no_service()
    test_thovex_service()


def test_calliope_no_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 1)
    current_mileage = 30000
    last_service_mileage = 0

    Car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_calliope_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 5)
    current_mileage = 35000
    last_service_mileage = 0

    Car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_glissade_no_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 1)
    current_mileage = 60000
    last_service_mileage = 0

    Car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_glissade_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 5)
    current_mileage = 65000
    last_service_mileage = 0

    Car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_palindrome_no_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 1)
    warning_light_on = False

    Car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
    print(Car.need_service()) 

def test_palindrome_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 5)
    warning_light_on = True

    Car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
    print(Car.need_service()) 

def test_rorschach_no_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 1)
    current_mileage = 60000
    last_service_mileage = 0

    Car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_rorschach_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 5)
    current_mileage = 65000
    last_service_mileage = 0

    Car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_thovex_no_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 1)
    current_mileage = 60000
    last_service_mileage = 0

    Car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

def test_thovex_service():
    current_date = datetime.datetime.now()
    last_service_date = current_date.replace(year = current_date.year - 5)
    current_mileage = 65000
    last_service_mileage = 0

    Car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print(Car.need_service()) 

