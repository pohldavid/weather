input('--------ATTENTION! This is fake bme280 -----------')

""" for debugging purpose when running on pc rather than raspberry pi """


def load_calibration_params(bus,address):
    pass
    

class sample:
    
    def __init__(self, bus = 0, address =0):
        self.bus = bus
        self.address = address
    
    temperature = 'Fake 98.6'

    humidity = 'Fake 100'

    pressure = 'Fake 29.92'
    
    
