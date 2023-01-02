from abc import ABC, abstractmethod

from serviceable import Serviceable
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire


    @abstractmethod
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()

class CarFactory(ABC):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

