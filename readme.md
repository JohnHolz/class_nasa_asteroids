# Trabalho final

## Metadados


Column| Description
---|---
SPK-ID| Objeto SPK-ID primário
ID do objeto| ID do banco de dados interno do objeto
Object fullname| Nome completo/designação do objeto
pdes| Designação primária do objeto
name| nome IAU do objeto
NEO| Sinalizador de objeto próximo da Terra (NEO)
PHA| Sinalizador de Asteroide Potencialmente Perigoso (PHA)\*
H| Parâmetro de magnitude absoluta
Diameter| diâmetro do objeto (da esfera equivalente) km Unidade
Albedo| albedo geométrico
Diameter_sigma| incerteza de 1 sigma no diâmetro do objeto km Unidade
Orbit_id| ID da solução Orbit
Epoch| Época de osculação na forma modificada do dia juliano
Equinox| Equinócio do quadro de referência
e| Excentricidade
a| Semi-eixo maior au Unit
q| distância do periélio au Unidade
i| inclinação; ângulo em relação ao plano eclíptico x-y
tp| Tempo de passagem do periélio Unidade TDB
moid_ld| Distância Mínima de Interseção da Órbita da Terra au Unit


### Ordem

- Limpeza
- EDA
- Benchmark
- Modelos
- Rede


## Rode você mesmo

Existe um arquivo requirements no docker pra replicar o ambiente. Porem com docker você pode não conseguir utilizar a gpu, o só faz levar mais tempo.

        docker-compose up -d 
        

