from socket import ntohl


salario_mensual_bruto: int
sueldo_hora = (salario_mensual_bruto*12)/(52*32)
horas_semana: int


if  36 <= horas_semana <= 43
    horas_extra = (horas_semana-35)*1.25
    horas_basicas = 35

if   horas_semana > 43
    horas_extra = (horas_semana-43)*1.5 + 7*1.25
    horas_basicas = 35


horas_totales = horas_basicas + horas_extra
sueldo_total = horas_totales*sueldo_hora
