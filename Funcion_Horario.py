import re

semana=r'lu|mar|mie|jue|vi|sab|dom'
Diurnal=r'mañana|tarde|todo el dia'
Nocturnal=r'nocturno|noche|madrugada'
Weekdays=r'lu vi| lunes a viernes'
Weekend=r'fines de semana|sabado y domingo|sab|dom|fin de semana'
Alldays=r'lunes a domingo|todos los dias|lu a vi|lunes a vier|dia y noche|mañana y tarde'
regex=re.compile(r'\d')

regex_dias=re.compile(semana,re.I); regex_DIURNAL=re.compile(Diurnal,re.I); regex_NORTURNAL=re.compile(Nocturnal,re.I)
regex_WEEKDAYS=re.compile(Weekdays,re.I); regex_WEEKEND=re.compile(Weekend,re.I); regex_ALLDAYS=re.compile(Alldays,re.I)

regex_L = re.compile(r'lu',re.I); regex_M = re.compile(r'mar',re.I) ; regex_m = re.compile(r'mie',re.I)
regex_J = re.compile(r'jue',re.I); regex_V = re.compile(r'vi',re.I); regex_S = re.compile(r'sab',re.I)
regex_D = re.compile(r'dom',re.I); regex_secuencia=re.compile(r' ')

# no cerramos|dia y noche|DIA y NOCHE
horario=list()
dias=list()
numero=list()
indice=list()
etiqueta_dia=list()
business_hours=dict()
etiqueta_hora=0
texto =('7 am a 23 pm')
indice = regex_secuencia.split(texto)
v=False
x=y=2
print(indice)

def dia_semana(dia):
    if regex_L.match(dia): dia = 'L'
    if regex_M.match(dia): dia = 'M'
    if regex_m.match(dia): dia = 'm'
    if regex_J.match(dia): dia = 'J'
    if regex_V.match(dia): dia = 'V'
    if regex_S.match(dia): dia = 'S'
    if regex_D.match(dia): dia = 'D'
    return (dia)

def funcion_horario(segmentado,Buscador,selector):
    lista=list()
    numpalab= list()
    for n in segmentado:
        if Buscador.search(n):
            numpalab.append(n)
    if selector==0:
        for n in numpalab:
            if n !='24':
                if len(n) < 3:
                    lista.append(n+':00')
                else:
                    lista.append(n)
            else:
                lista= ['00:00','24:00']
    else:
        for n in numpalab:
                lista.append(dia_semana(n))
    return(lista)

def func_comodin(comodin,y):
    business_hours[v][comodin] = list()
    horario = funcion_horario(indice,regex,0);i=0
    if v == True:
        business_hours[v][comodin]=['00:00','24:00']
    elif ((texto.find('diurno')!=-1) | (texto.find('mañana y tarde"')!=-1)):
        business_hours[v][comodin] ='diurno'
    else:
        business_hours[v][comodin]=(horario)
    return

for n in indice:
    if regex_dias.match(n):
        etiqueta_hora += 1
    if regex.search(n):
        etiqueta_dia.append(etiqueta_hora)
    if (n == '24')|(texto=='DIA y NOCHE'):
        v = True

dias = funcion_horario(indice,regex_dias,2)
horario = funcion_horario(indice,regex,0)
business_hours[v] = dict()

if regex_ALLDAYS.search(texto):
    func_comodin('ALLDAYS', v)

elif regex_WEEKEND.search(texto):
    func_comodin('WEEKEND',v);x=1

elif regex_DIURNAL.search(texto):
    business_hours = dict()
    business_hours['False'] = {'DIURNAL': [["7:00", "18:00"]]};x=1

elif regex_NORTURNAL.search(texto):
    business_hours = dict()
    business_hours['False'] = {'NOCTURNAL': [["7:00", "18:00"]]};x=1

elif regex_WEEKDAYS.search(texto):
    func_comodin('WEEKDAYS',v);x=1

elif ((len(dias)==0)&(x!=1)):
    func_comodin('ALLDAYS',v)

elif(x!=1):
    for n in dias:
        business_hours[v][n] = list()
    z=0
    for n in etiqueta_dia:
        business_hours[v][dias[n-1]].append(horario[z])
        z+=1
else:
    print('no comprendo')
print(len(dias))
print(business_hours)