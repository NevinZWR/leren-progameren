while True:
    try:
        x = int(input("Hoe vaak wil je hem uitvoeren? "))
        def fibonacci(x :int)-> list:
            begin_getal = [0, 1]
            for i in range(2, x): 
                volgendegetal = begin_getal[-1] + begin_getal[-2]
                begin_getal.append(volgendegetal)
            return begin_getal


        fib_herhaling = fibonacci(x)
        print("De Fibonacci-reeks tot", x, "getallen is:", fib_herhaling)
        break
    except ValueError:
        print("voor een getal in " )