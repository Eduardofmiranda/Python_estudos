segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

dias = horas // 24
horas_final = horas % 24

print(dias, "dias,", horas_final, "horas," , minutos , "minutos e" , segs_restantes_final, "segundos.")

