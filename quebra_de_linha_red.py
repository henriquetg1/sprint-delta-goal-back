import pandas as pd
import json

with open("dados/QuebraLinha_Palmeiras_x_Bragantino.json") as f:
    data = json.load(f)

rupturas_pal = data["time"]["1"]["rupturas"]
rupturas_red = data["time"]["5"]["rupturas"]

for ruptura in rupturas_red:
    print(ruptura)

dic_rupturas_red = {}
zonas_ataque_red = {}

for ruptura in rupturas_red:
    if ruptura["zona_defesa"] not in zonas_ataque_red:
        zonas_ataque_red[ruptura["zona_defesa"]] = 1
    else:
        zonas_ataque_red[ruptura["zona_defesa"]] += 1

    if ruptura["nome_jogador_ruptura"] not in dic_rupturas_red:
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]] = {
            "tempo_ruptura": [ruptura["instante_ruptura"]],
            "jogador_posse_de_bola": [ruptura["nome_jogador_posse_bola"]],
            "desfecho": [ruptura["desfecho"]],
            "qntd_rupturas": 1,
            "zona": [ruptura["zona_defesa"]],
            "time": "Bragantino",
        }
    else:
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]]["tempo_ruptura"].append(
            ruptura["instante_ruptura"]
        )
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]]["desfecho"].append(
            ruptura["desfecho"]
        )
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]]["zona"].append(
            ruptura["zona_defesa"]
        )
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]][
            "jogador_posse_de_bola"
        ].append(ruptura["nome_jogador_posse_bola"])
        dic_rupturas_red[ruptura["nome_jogador_ruptura"]]["qntd_rupturas"] += 1

dic_rupturas_red


ZONAS_ATAQUE_RED = zonas_ataque_red

DF_BRAGANTINO = pd.DataFrame(dic_rupturas_red)
DF_BRAGANTINO = DF_BRAGANTINO.transpose()
# DF_BRAGANTINO
