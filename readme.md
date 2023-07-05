#####

Estrutura

- Metadados
- Limpeza
- Benchmark
- Modelo 2
- Rede

## Metadados

Y: Variavel resposta é

SPK-ID: Objeto SPK-ID primário
ID do objeto: ID do banco de dados interno do objeto
Object fullname:: Nome completo/designação do objeto
pdes: Designação primária do objeto
name: nome IAU do objeto

NEO: Sinalizador de objeto próximo da Terra (NEO)
PHA: Sinalizador de Asteroide Potencialmente Perigoso (PHA)\*
H: Parâmetro de magnitude absoluta
Diameter: diâmetro do objeto (da esfera equivalente) km Unidade
Albedo: albedo geométrico
Diameter_sigma: incerteza de 1 sigma no diâmetro do objeto km Unidade
Orbit_id: ID da solução Orbit
Epoch: Época de osculação na forma modificada do dia juliano
Equinox: Equinócio do quadro de referência
e: Excentricidade
a: Semi-eixo maior au Unit
q: distância do periélio au Unidade
i: inclinação; ângulo em relação ao plano eclíptico x-y
tp: Tempo de passagem do periélio Unidade TDB
moid_ld: Distância Mínima de Interseção da Órbita da Terra au Unit

####

> raw.nunique()/raw.shape[0]

    #id                1.000000
    #spkid             1.000000
    #full_name         1.000000
    #pdes              1.000000

> (df.isna().sum()/df.shape[0]).sort_values()

    diameter          0.857897
    diameter_sigma    0.858031
    albedo            0.859051

> raw.columns[:6] ## to drop

    # ['id', 'spkid', 'full_name', 'pdes', 'name', 'prefix']

> df.equinox.unique()

    # equinox -> ['J2000'] 1 value

n: 958_524
p: 44?


svm needs scaling
knn needs scaling
random forest ?
logistica no
tf better with scalling


y -> classes que começam com A, pois tem Near-Earth 