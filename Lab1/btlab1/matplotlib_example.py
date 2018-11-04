from matplotlib import pyplot
machine_count = [18, 4, 2]
machine_names = [ "PC", "MAC", "LINUX"]
pyplot.pie(machine_count, labels= machine_names, autopct = "%.1f%%", shadow=True, explode=[0,0.1,0.1])
pyplot.title("PC vs MAC vs LINUX")
pyplot.axis("equal")
pyplot.show()