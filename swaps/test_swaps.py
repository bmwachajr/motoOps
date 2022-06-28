
from decimal import Decimal
from batteries.models import Batteries, BatteryTelematics
from drivers.models import Drivers
import pytest
from django.test import TestCase

from stations.models import Stations
from swaps.models import Swaps

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestSwap:
    def setup_method(self):
        battery_1_data = {
            "serial": "test 1",
            "state_of_charge": "100.00",
            "state_of_health": "100.00",
            "gross_capacity": Decimal(35.00),
            "net_capacity": Decimal(31.00),
            "status": "INACTIVE"
        }
        battery_2_data = {
            "serial": "test 2",
            "state_of_charge": "100.00",
            "state_of_health": "100.00",
            "gross_capacity": Decimal(35.00),
            "net_capacity": Decimal(31.00),
            "status": "ACTIVE"
        }
        battery_3_data = {
            "serial": "test 3",
            "state_of_charge": "100.00",
            "state_of_health": "100.00",
            "gross_capacity": Decimal(35.00),
            "net_capacity": Decimal(31.00),
            "status": "ACTIVE"
        }
        station_data = {
            "name": "Area 51",
            "longitude": "32.582520",
            "latitude": "0.347596",
            "contact": "+256709987980",
            "status": "ACTIVE"
        }
        driver_data = {
            "fullname": "Ben H",
            "emoto_license": "KR 123W",
            "contact": "+1 987 897 8909",
            "energy_consumption_rate": Decimal(0.32),
            "status": "ACTIVE"
        }
        self.driver = Drivers.objects.create(**driver_data)
        self.station = Stations.objects.create(**station_data)
        self.battery_1 = Batteries.objects.create(**battery_1_data)
        self.battery_2 = Batteries.objects.create(**battery_2_data)
        self.battery_3 = Batteries.objects.create(**battery_3_data)
        battery_telematics_data = {
            "current_charge": Decimal(5.00),
            "longitude": "1223333",
            "latitude": "123444",
            "external_temperature": "32.00",
            "battery": self.battery_3,
            "driver": self.driver
        }
        self.telematics = BatteryTelematics.objects.create(**battery_telematics_data)

    def test_create_swap_unmoved_emoto(self):
        payload = {
            "battery_swapped_in": self.battery_1,
            "battery_swapped_out": self.battery_2,
            "driver": self.driver,
            "station": self.station,
            "status": "COMPLETED"
        }

        swap = Swaps.objects.create(**payload)

        # assertions 
        assert self.battery_1.status == 'ACTIVE'
        assert self.battery_2.status == 'INACTIVE'

        assert swap.charge_used == 0
        assert swap.amount_payable == 0
        assert swap.distance_traveled == 0


    def test_create_swap_moved_emoto(self):        
        payload = {
            "battery_swapped_in": self.battery_1,
            "battery_swapped_out": self.battery_3,
            "driver": self.driver,
            "station": self.station,
            "status": "COMPLETED"
        }

        swap = Swaps.objects.create(**payload)

        # assertions 
        assert self.battery_1.status == 'ACTIVE'
        assert self.battery_3.status == 'INACTIVE'

        assert swap.charge_used == Decimal(31.00) -  Decimal(5.00)
        assert swap.amount_payable == Decimal(0.2) * swap.charge_used # assuming each unit of energy costs 2 cents
        assert swap.distance_traveled == swap.charge_used / self.driver.energy_consumption_rate

