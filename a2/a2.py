def validate_pin(pin):
    count = 0   
    if pin.isnumeric():
        for i in pin:   
            count += 1
        if count == 6 or count == 4:
            return True
        else:
            return False
    else:
        return False