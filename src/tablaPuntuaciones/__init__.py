import time

def sumar_puntos(kills, asistencias, muertes):
    puntos = (kills * 3) + asistencias - muertes
    return puntos


def tabla_de_puntuaciones(rondas):
    puntuacion = {}
    estadisticas_totales = {}
    mvps = {}
    i = 1
    for clave in rondas[0].keys():
        puntuacion[clave] = 0
        estadisticas_totales[clave] = {"kills" : 0, "assists": 0, "deaths": 0, "puntos": 0}
        mvps[clave] = 0
    for ronda in rondas:
        print(f"Ronda {i}")
        i += 1
        puntaje_ronda = {}
        for clave, valor in ronda.items():
            kills = valor["kills"]
            asistencias = valor["assists"]
            muertes = 1 if valor["deaths"] else 0
            puntaje = sumar_puntos(kills, asistencias, muertes)
            puntaje_ronda[clave] = puntaje
            puntuacion[clave] += puntaje
            estadisticas_totales[clave]["kills"] += kills
            estadisticas_totales[clave]["assists"] += asistencias
            estadisticas_totales[clave]["deaths"] += muertes
        mvp = max(puntaje_ronda, key=puntaje_ronda.get)
        mvps[mvp] += 1
        print("Jugador  Kills  Assists  Deaths  Puntaje  MVP")
        print("-" * 50)
        ranking = sorted(puntuacion.items(), key=lambda item: item[1], reverse=True)
        for jugador, puntaje_total in ranking:
            print(jugador,"   ", estadisticas_totales[jugador]["kills"],"    ", estadisticas_totales[jugador]["assists"],"       ", estadisticas_totales[jugador]["deaths"],"     ", puntaje_total,"    ", mvps[jugador])
        print("\n")
        time.sleep(2)