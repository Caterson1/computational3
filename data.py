import requests
import json
from gravitational_objects import *
import datetime as d

planetIDS = {"sun": "10", "mercury": "199", "venus": "299", "earth": "399", "mars": "499", "jupiter": "599",
             "saturn": "699", "uranus": "799", "neptune": "899"}
planetDATA = planetIDS
planetCHECKS = planetIDS
planetMASS = {"sun": 1988500E24, "mercury": 3.302E23, "venus": 48.685E23, "earth": 5.97219E24, "mars": 6.4171E23, "jupiter": 189818722E22 * 1E-3,
             "saturn": 5.6834E26, "neptune": 102.409E24, "uranus": 86.813E24}

date = f"{datestart.timetuple()[0]}-{datestart.timetuple()[1]}-{datestart.timetuple()[2]}"
date2 = f"{datestart.timetuple()[0]}-{datestart.timetuple()[1]}-{datestart.timetuple()[2]+1}"
readplanets = {}

with open("DATA", 'r') as d:
    for line in d.readlines():
        line = line.replace("\n", "").split("|")
        readplanets.update({line[3].strip(): CelestialBody(vec_reverse_repr(line[0]), vec_reverse_repr(line[1]), float(line[2]), line[3].strip())})
    d.close()

print(readplanets)

def apidata(planet):
    if isinstance(planet, str):
        planet = planetIDS[planet]
    DATA = requests.get(
        f"https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='{planet}'&OBJ_DATA='YES'&MAKE_EPHEM"
        f"='YES'&EPHEM_TYPE='VECTOR'&CENTER='500@0'&START_TIME='{date}'&STOP_TIME='{date2}"
        "'&STEP_SIZE='1%20d'&QUANTITIES='1,9,20,23,24,29'").text
    # print(DATA)
    # ----------------NAME----------------------
    name = DATA.split()[13]
    # ----------------MASS----------------------
    massDATA = DATA.replace("Mass,", "Mass x").split("Mass x")[1].split()
    # ['10^23', '(kg)', '=', '6.4171', ...]
    #Find the power of 10
    power10 = float(massDATA[0].replace("^", "E").replace("x", ""))/1E1
    # EDGE CASE 1: EPHEMERIS PUTS THE MASS OF JUPITER IN GRAMS FOR SOME REASON >:(
    if massDATA[1] == '(g)':
        power10 /= 1E3
    # EDGE CASE 2: I GENUINELY DON'T KNOW WHERE THIS COMES FROM BUT I FIXED IT
    if massDATA[3] == "Equ.":
        massDATA[3] = massDATA[2]
    # math :3
    mass = power10 * float(massDATA[3].replace("~", "").split("+-")[0])
    # ------------------------------PART II--------------------------------------
    DATA = DATA.split('$$SOE\n')
    DATA = DATA[1].split("\n$$EOE")[0]
    DATA = DATA.split("\n")
    # pos contains the initial position as a string (e.g X =-1.227620398301847E+06 Y =-3.791447270083412E+05 Z =
    # 3.177942514167895E+04)
    pos = [DATA[1], DATA[5]]
    for i in pos:
        ii = i.replace("X =", " ").replace(" Y =", " ").replace(" Z =", " ").split()
        pos[pos.index(i)] = Vec(float(ii[0]) * 1E3, float(ii[1]) * 1E3, float(ii[2]) * 1E3)
    v = [DATA[2], DATA[6]]
    for i in v:
        ii = i.replace("VX=", " ").replace(" VY=", " ").replace(" VZ=", " ").split()
        v[v.index(i)] = Vec(float(ii[0]) * 1E3, float(ii[1]) * 1E3, float(ii[2]) * 1E3)
    # print(pos[0], v[0], planetMASS[planet])
    print(CelestialBody(pos[0], v[0], mass, name))
    with open("DATA", 'a') as d:
        d.write(f"{pos[0]} | {v[0]} | {mass} | {name.lower()}\n")
        d.close()
    return CelestialBody(pos[0], v[0], mass, name)

def getdata(planet):
    try: float(planet)
    except:
        if planet not in readplanets:
            return apidata(planet)
        else:
            return readplanets[planet]
    else:
        return apidata(planet)
