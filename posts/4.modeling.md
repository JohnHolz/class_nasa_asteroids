## Escola de usar Escaler

- resposta não precisar de scaling
- Não precisar explicar parametros reescalados ou nd do genero

## Diferenças de datasets para comparações

- Com x Sem sigma
- Standard x MinMaxScaling

Ficamos com 4 datasets a serem testados.

    3 layer 10x16x8x1
    Binary crossentropy
    Adam
    Activations: Relu
    Last Layer: Sigmoid
    Epochs:~50

    rf = RandomForestClassifier(n_estimators=80)
    ada = AdaBoostClassifier()
    knn = KNeighborsClassifier()
