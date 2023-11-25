def main():
  """Creates a text file named `load.txt`"""
  montlyLightingLoad = 941
  dailyLightingLoad = montlyLightingLoad / 30.5 # carga diária em kWh

  montlyGateLoad = 330
  dailyGateLoad = montlyGateLoad / 30.5 # carga diária em kWh
  hourlyGateLoad = dailyGateLoad / 24.0

  # carga por hora (considerando iluminação ligada das 19h às 6h - 11 horas)
  lightingLoadPerHour = dailyLightingLoad / 10.0
  print("Carga de iluminiação média por hora = {}".format(lightingLoadPerHour))


  with open("load3.txt", "w") as f:
    f.write("Exported Data (8760)\n") # cabeçalho
    for d in range(365):
      for h in range(24):
        lightInstPower = 0 # pot. instantânea de iluminação pública
        if (h in range(0, 6)) or (h in range(19, 23)):
            # considera-se a iluminação ligada das 6h às 19h
            lightInstPower = lightingLoadPerHour
        # f.write("{:.6f}\n".format(h, lightInstPower))
        f.write("{:.6f}\n".format(lightInstPower + hourlyGateLoad))
if __name__ == "__main__":
  main()