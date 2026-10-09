"""
BÔNUS — VISUALIZAÇÃO HUMANA DO MELHOR AGENTE

Este arquivo foi pensado para ser integrado ao template principal.
Ele assume que:
- a classe Agente já existe;
- ENV_ID = "ALE/Freeway-v5";
- gymnasium, ale_py e numpy já foram importados.

Objetivo:
Executar visualmente, em uma janela do Atari, o melhor agente
encontrado pelo processo evolutivo.
"""

import gymnasium as gym
import ale_py

gym.register_envs(ale_py)

ENV_ID = "ALE/Freeway-v5"


def visualizar_agente(agente):
    """
    Executa uma partida com visualização humana.

    IMPORTANTE:
    render_mode="human" cria uma janela mostrando o jogo.
    O agente continua recebendo o estado pela RAM.
    """

    env = gym.make(
        ENV_ID,
        obs_type="ram",
        render_mode="human"
    )

    estado, info = env.reset()

    terminou = False
    recompensa_total = 0

    while not terminou:

        # O MESMO agente treinado escolhe a ação.
        acao = agente.agir(estado)

        estado, recompensa, terminated, truncated, info = env.step(acao)

        recompensa_total += recompensa
        terminou = terminated or truncated

    env.close()

    print(f"Recompensa obtida na visualização: {recompensa_total}")


# ---------------------------------------------------------
# COMO USAR NO PROGRAMA PRINCIPAL
# ---------------------------------------------------------
#
# Depois de encontrar e armazenar o melhor indivíduo:
#
# visualizar_agente(melhor_agente)
#
# ---------------------------------------------------------
