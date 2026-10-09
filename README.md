# Neuroevolucao no Freeway

Projeto pratico de Fundamentos de Inteligencia Artificial usando neuroevolucao no ambiente `ALE/Freeway-v5`.

## Como executar

Instale as dependencias:

```powershell
pip install "gymnasium[atari]" ale-py numpy matplotlib
```

Execute o experimento principal:

```powershell
python main.py
```

Para executar os tres experimentos obrigatorios:

```powershell
python main.py --experimentos todos
```

Para fazer um teste rapido:

```powershell
python main.py --geracoes 1 --populacao 3 --max-passos 50 --baseline-episodios 1
```

## Configuracao padrao

- Ambiente: `ALE/Freeway-v5`
- Observacao: RAM do Atari, vetor com 128 valores
- Acoes: `0 = NOOP`, `1 = UP`, `2 = DOWN`
- Modo/fase padrao: `1`
- Dificuldade padrao: `1`
- Populacao: 20 individuos
- Geracoes: 30
- Rede neural: 128 entradas, 16 neuronios ocultos e 3 saidas
- Elitismo: 2 melhores individuos preservados sem mutacao
- Selecao: ranking por fitness, usando a metade superior como pais
- Reproducao: copia independente de um pai com `copy.deepcopy`, seguida de mutacao

## Experimentos de mutacao

| Experimento | Taxa de mutacao | Intensidade |
| --- | ---: | ---: |
| A | 1% | 0,05 |
| B | 10% | 0,20 |
| C | 40% | 0,50 |

O experimento B e executado por padrao. Use `--experimentos todos` para gerar a comparacao completa.

## Modo, dificuldade e fases

No codigo, a configuracao padrao fica em `MODO_JOGO` e `DIFICULDADE_JOGO`.

O Freeway na ALE possui modos de `0` a `7` e dificuldades `0` ou `1`. O projeto esta configurado para comecar em `modo=1` e `dificuldade=1`.

Para escolher outro modo ou dificuldade:

```powershell
python main.py --modo 3 --dificuldade 1
```

Para testar varias variacoes de fase:

```powershell
python main.py --variacoes-fase
```

Quando `--variacoes-fase` e usado, o melhor geral e escolhido por fitness ponderado:

```text
fitness_ponderado = fitness_bruto * peso_fase
peso_fase = 1 + modo*0.15 + dificuldade*0.50
```

Assim, 10 pontos em uma fase mais dificil valem mais do que 10 pontos em uma fase simples.

## Saidas geradas

Os resultados ficam na pasta `resultados/`:

- `fitness.csv`: melhor, media e pior fitness por geracao
- `fitness.png`: grafico com melhor fitness e fitness medio
- `baseline.txt`: comparacao com agente aleatorio
- `melhor_agente.txt`: resumo do melhor agente geral usando fitness ponderado
- `melhor_agente.pkl`: melhor agente encontrado, salvo para visualizacao posterior

## Bonus: visualizacao humana

Para treinar e, ao final, abrir uma janela mostrando o melhor agente jogando:

```powershell
python main.py --renderizar-melhor
```

Depois que um treinamento ja gerou `resultados/melhor_agente.pkl`, voce tambem pode visualizar sem treinar de novo:

```powershell
python main.py --visualizar-arquivo resultados/melhor_agente.pkl
```

O bonus esta implementado na funcao `visualizar_agente`, que usa `render_mode="human"` para abrir a janela do Atari.

## Conceitos no codigo

- Agente: classe `Agente`, que recebe o estado e escolhe uma acao.
- Ambiente: funcao `criar_ambiente`, usando Gymnasium/ALE.
- Acao: metodo `agir`, escolhendo o indice de maior saida da rede com `argmax`.
- Recompensa: valor `recompensa` retornado por `ambiente.step(...)`.
- Fitness: soma das recompensas no episodio, calculada em `avaliar`.
- Individuo: cada objeto `Agente`, com seus proprios pesos `W1`, `b1`, `W2` e `b2`.
- Populacao: lista criada em `criar_populacao`.
- Geracao: ciclo executado em `executar_experimento`.
- Selecao: funcao `selecionar`.
- Elitismo: copias dos melhores individuos em `nova_geracao`.
- Mutacao: funcao `mutar`.
- Exploracao: populacao inicial aleatoria e ruido aplicado pela mutacao.
- Convergencia: analisada pelo historico salvo em `fitness.csv` e pelo grafico `fitness.png`.

## Analise esperada

Compare os tres experimentos:

- Mutacao quase zero tende a gerar pouca diferenca entre pais e filhos, reduzindo a exploracao.
- Mutacao intermediaria busca equilibrar preservacao e diversidade.
- Mutacao muito alta aumenta a diversidade, mas pode destruir solucoes boas.

Para defesa `fitness.csv`, o `fitness.png` e o `baseline.txt` como evidencias.

