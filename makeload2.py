def main():
  """Creates a text file named `load3inc.txt`"""

  DAYS_PER_MONTH = 365.0 / 12.0

  # carga de iluminação pública (das 19h às 6h = 11 horas)
  montlyLightingLoad = 941
  dailyLightingLoad = montlyLightingLoad / 30.5 # carga diária em kWh
  lightingLoadPerHour = dailyLightingLoad / 11.0
  print("Carga de iluminiação média por hora = {:.3f}kWh".format(lightingLoadPerHour))

  # carga da guarita (consumo distribuído nas 24h)
  montlyGateLoad = 360.0
  dailyGateLoad = montlyGateLoad / DAYS_PER_MONTH # carga diária em kWh
  hourlyGateLoad = dailyGateLoad / 24.0
  print("Carga horária atual da guarita = {:.3f}kWh".format(hourlyGateLoad))

  # carga estimada das novas câmeras e segurança no perímetro (24h)
  montlySecutityInc = 747.0
  daylySecutityInc = montlySecutityInc / DAYS_PER_MONTH # carga diária em kWh
  hourlySecutityInc = daylySecutityInc / 24.0
  print("Carga horária estimada das novas câmeras e sist. segurança = {:.3f}kWh".format(hourlySecutityInc))

  # carga estimada para os novos sistemas de ar-condicionado
  # Considera-se que serão usados de 01/01 a 15/50, e depois de 01/08 a 31/12
  qtdAirCond = 2 # serão dois ar condicionados de 12.000 BTUs
  hourlyAirCond = 0.9 * qtdAirCond # kWh por hora de utilização
  print("Carga de ar condicionado por hora = {:.3f}kWh".format(hourlyAirCond))
  
  daysInterval1 = 31 + 28 + 31 + 30 + 15 # dias de 1º de jan. a 15 de maio
  daysInterval2 = 31 + 30 + 31 + 30 + 31 # dias de 1º de ago. a 31/12
  dayAirOff = daysInterval1 # depois desse nº de dias supõe-se que o ar é desligado
  dayAirOn = (365 - daysInterval2) # a partir de 01/08 estima-se que o ar passe a ser
                                    # usado novamente

  with open("load3inc.txt", "w") as f:
    f.write("Exported Data (8760)\n") # cabeçalho
    for d in range(365):      
      for h in range(24):
        InstHourlyPower = hourlyGateLoad + hourlySecutityInc

        # ILUMINAÇÃO PÚBLICA - todos os dias das 19h às 6h
        if (h in range(0, 6)) or (h in range(19, 24)):
            # considera-se a iluminação ligada das 6h às 19h
            InstHourlyPower += lightingLoadPerHour
      
        # AR CONDICIONADO GUARITA
        yDay = d % 365 # dia do ano
        if ((yDay <= dayAirOff) or (yDay >= dayAirOn)) and (d % 6):
          # segunda a sabado, excluindo dias do ano sem uso de ar

          if (d % 5) == 0: # sabados (note que d começa em zero, não 1)
            if (h in range(8,12)):
              InstHourlyPower += hourlyAirCond
          else:
            if (h in range(8,18)):
              InstHourlyPower += hourlyAirCond
    
        f.write("{:.6f}\n".format(InstHourlyPower))
if __name__ == "__main__":
  main()