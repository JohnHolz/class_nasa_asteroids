# Primeira olhada no dataset


### Informações gerais

Rows: 958524  
Columns: 45

  Y | Qtd.
 ---|---
N   | 936537
Y   |  2066
NA  | 19921


#### Table head
    raw.head().transpose()
col name | 1 row | 2 row | 3 row
---|---|---|---
id              |       a0000001 |        a0000002 |       a0000003
spkid           |        2000001 |         2000002 |        2000003
full_name       |        1 Ceres |        2 Pallas |         3 Juno
pdes            |              1 |               2 |              3
name            |          Ceres |          Pallas |           Juno
prefix          |            NaN |             NaN |            NaN
neo             |              N |               N |              N
pha             |              N |               N |              N
H               |            3.4 |             4.2 |           5.33
diameter        |          939.4 |           545.0 |        246.596
albedo          |           0.09 |           0.101 |          0.214
diameter_sigma  |            0.2 |            18.0 |         10.594
orbit_id        |         JPL 47 |          JPL 37 |        JPL 112
epoch           |      2458600.5 |       2459000.5 |      2459000.5
epoch_mjd       |          58600 |           59000 |          59000
epoch_cal       |     20190427.0 |      20200531.0 |     20200531.0
equinox         |          J2000 |           J2000 |          J2000
e               |       0.076009 |        0.229972 |       0.256936
a               |       2.769165 |        2.773841 |       2.668285
q               |       2.558684 |        2.135935 |       1.982706
i               |      10.594067 |       34.832932 |      12.991043
om              |      80.305531 |      173.024741 |     169.851482
w               |      73.597695 |      310.202392 |     248.066193
ma              |      77.372098 |      144.975675 |     125.435355
ad              |       2.979647 |        3.411748 |       3.353865
n               |       0.213885 |        0.213345 |       0.226129
tp              | 2458238.754129 |  2458320.962366 |  2458445.79219
tp_cal          |20180430.254129 | 20180721.462366 | 20181123.29219
per             |    1683.145703 |     1687.410992 |    1592.013769
per_y           |       4.608202 |         4.61988 |       4.358696
moid            |        1.59478 |         1.23429 |        1.03429
moid_ld         |     620.640533 |      480.348639 |     402.514639
sigma_e         |            0.0 |             0.0 |            0.0
sigma_a         |            0.0 |             0.0 |            0.0
sigma_q         |            0.0 |             0.0 |            0.0
sigma_i         |            0.0 |        0.000003 |       0.000003
sigma_om        |            0.0 |        0.000006 |       0.000017
sigma_w         |            0.0 |        0.000009 |       0.000018
sigma_ma        |            0.0 |        0.000009 |       0.000008
sigma_ad        |            0.0 |             0.0 |            0.0
sigma_n         |            0.0 |             0.0 |            0.0
sigma_tp        |            0.0 |        0.000041 |       0.000035
sigma_per       |            0.0 |        0.000004 |       0.000003
class           |            MBA |             MBA |            MBA
rms             |        0.43301 |         0.35936 |        0.33848



## Porcentagem de valores diferença e % de falsos
Primeiro vamos tratar nossos problemas horizontais e verticais
Linhas e Colunas

Queremos entender a variabilidade geral dos dados, procurando colunas unicas como ids, remover colunas com uma quantidade elevada de vazios.

#### Quantidade de valores unicos nas colunas

    (raw.nunique()/raw.shape[0]).sort_values()
    pha               0.000002
    sigma_per         0.294919
    sigma_tp          0.303848
    moid              0.327900
    moid_ld           0.327901
    i                 0.999885
    e                 0.999917
    tp_cal            0.999974
    ad                0.999980
    a                 0.999984
    q                 0.999984
    per               0.999985
    per_y             0.999986
    n                 0.999990
    om                0.999994
    w                 0.999995
    ma                0.999995
    tp                0.999995
    pdes              1.000000
    full_name         1.000000
    spkid             1.000000

##### Quantidade de Vazios
    (raw.isna().sum()/raw.shape[0]).sort_values()
    ma                0.000001
    per_y             0.000001
    rms               0.000002
    ad                0.000004
    per               0.000004
    neo               0.000004
    moid_ld           0.000132
    H                 0.006534
    pha               0.020783
    moid              0.020783
    sigma_tp          0.020784
    sigma_n           0.020784
    sigma_ma          0.020784
    sigma_w           0.020784
    sigma_om          0.020784
    sigma_i           0.020784
    sigma_e           0.020784
    sigma_a           0.020784
    sigma_q           0.020784
    sigma_ad          0.020788
    sigma_per         0.020788
    diameter          0.857897
    diameter_sigma    0.858031
    albedo            0.859051
    name              0.976981
    prefix            0.999981

## Dropando
Lidando com problemas horizontais e verticais
1. Primeiro removemos as colunas que parecem IDs
2. Dropando rows onde variavel resposta em branco


#### Tabela de vazios pós remover rows com resposta em branco
    full_name         0.000000
    sigma_tp          0.000001
    sigma_n           0.000001
    sigma_ma          0.000001
    sigma_w           0.000001
    sigma_om          0.000001
    sigma_i           0.000001
    sigma_q           0.000001
    sigma_a           0.000001
    sigma_e           0.000001
    per_y             0.000001
    ma                0.000001
    rms               0.000001
    ad                0.000004
    neo               0.000004
    per               0.000004
    sigma_ad          0.000005
    sigma_per         0.000005
    H                 0.006672
    diameter          0.854881
    diameter_sigma    0.855018
    albedo            0.856059
    name              0.976493
    prefix            0.999981

Verificando manualmente vemos que esse 1-7 dados que todas colunas que apresentam dados são de asteroides onde não há risco, então como já temos nosso dataset desbalanceado. Ficamos com:

**n: 936537  
p: 39**

  Y| Qtd
---|---
 N | 936537
 Y |  2066

## Primeiras Notas

1. Notas:
   1. **Variavel resposta Y:PHA**  
   2. **Variaveis não númericas: NEO(binaria) e CLASS**  
   3. **Todas outras variaveis são númericas**  
2. First Cleaning:
   1. **Dropar dados com variavel resposta vazia**
   2. **Dropar colunas primeiras 6 colunas ids/nomes**

# Conclusão
Optivemos sucesso na nossa primeira olhada dos dados, a primeira limpada retirando o grosso do que não queremos. Identificando bem as variáveis, já tendo em mente que mesmo perdendo colunas e rows hoje não perdemos praticamente nada de informação, e aumentaremos nosso p dummificando a coluna class.
Para na próxima etapa apenas explorarmos apenas os dados "uteis".