weather = 'sunny'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella")
    case 'horse':
        print("holy shit wtf")
    case _:
        print("Lets stay inside")