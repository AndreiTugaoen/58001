class DistanceConversion:
    def __init__(self, meter):
        self._meter = meter

class CentimeterConveter(DistanceConversion):
    def converter(self):
        return(self._meter * 100)

class KilometerConverter(DistanceConversion):
    def converter(self):
        return(self._meter / 1000)

class InchesConverter(DistanceConversion):
    def converter(self):
        return(self._meter * 39.37)

def main():
    centimeter = float(input("Enter a Number to convert it to Centimeter: "))
    kilometer = float(input("Enter a Number to convert it to Kilometer: "))
    inches = float(input("Enter a Number to convert it to Inches: "))

    #Meter to kilometer
    convert = KilometerConverter(kilometer)
    print(str(convert.converter()), " kilometer")

    #Meter to centimeter
    convert = CentimeterConveter(centimeter)
    print(str(convert.converter()), " centimeter")

    #Meter to Inches
    convert = InchesConverter(inches)
    print(str(convert.converter()),  " inches")

if __name__ == '__main__':
    main()