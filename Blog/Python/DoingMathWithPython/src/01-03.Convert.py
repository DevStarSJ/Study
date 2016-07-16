def KilloMeterToMile(km):
    return km / 1.609

def MileToKilloMeter(mile):
    return mile * 1.609

def KilloGramToPound(kg):
    return kg * 2.20462

def PoundToKilloGram(pound):
    return pound / 2.20462

def CelsiusToFahrenheit(c):
    return c * 9 / 5 + 32

def FahrenheitToCelsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    try:
        order = int(input('Enter command (1.KilloMeterToMile, 2.MileToKilloMeter, 3.KilloGramToPound, 4.PoundToKilloGram, 5.CelsiusToFahrenheit, 6.FahrenheitToCelsius) : '))
        val = float(input('Enter value : '))
    except:
        print('Invalid command')

    task = [KilloMeterToMile, MileToKilloMeter, KilloGramToPound, PoundToKilloGram, CelsiusToFahrenheit, FahrenheitToCelsius]
    result = task[order-1](val)
    print('Result : ', result)  