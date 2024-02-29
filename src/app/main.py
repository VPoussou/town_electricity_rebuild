import pandas as pd
import json
from .model import (Batiment, Infra)


def main(file='./src/app/assets/data/reseau_en_arbre.csv'):
    # Le fichier CSV
    network_file = file
    # Lire le fichier CSV avec Pandas
    network_df = pd.read_csv(network_file)

    ########## ALGORITHME ###################

    # Trier uniquement les infratructures à remplacer
    network_df = network_df[network_df['infra_type'] == 'a_remplacer']
    # print(f'Network shape: {network_df.shape}')
    # print(f'{network_df}')

    # Créer la liste des batiments
    BatimentList = []

    # Grouper par identifiant de l'infrature
    infras_df = network_df.groupby(by='infra_id')

    # Grouper par identifiant de l'infrature
    batiments_df = network_df.groupby(by='id_batiment')
    for index_bat, bat_df in batiments_df:
        # print(f'{index_bat}')
        # print(f'{bat_df}')
        liste_infras = []
        # print(bat_df['infra_id'])
        for infra_id in bat_df['infra_id']:
            # print(f'Grouped by {infra_id=}')
            # print(infras_df.get_group(infra_id))
            # print('-'*30)
            infra_df = infras_df.get_group(infra_id)
            # print(f'{infra_df["infra_type"].iloc[0]}')
            # print(f'{infra_df}')
            # print('_' * 30)
            infra = Infra(
                infra_id,
                infra_df['infra_type'].iloc[0],
                infra_df['nb_maisons'].sum(),
                infra_df['longueur'].iloc[0],
            )
            liste_infras.append(infra)
        batiment = Batiment(index_bat, liste_infras)
        BatimentList.append(batiment)

    # print(BatimentList)

    # Methode : (Alternative)
    # Calculer la diffuclcuté des batiments
    # BatimentDict = {}
    # DifficultyList = []
    # # print(f'Batimin min: {min(BatimentList)}')
    #
    # for batiment in BatimentList:
    #     # print(f'{batiment.list_infras}')
    #     difficulty = batiment.get_building_difficulty()
    #     DifficultyList.append(difficulty)
    #     # print(f"Difficulty: {difficulty}")
    #     # print('_'*30)
    #     BatimentDict[f'{difficulty}'] = batiment
    #     # print()
    #
    # OrderBatimentDict = dict(sorted(BatimentDict.items()))
    # # A
    # print(f'Min is {min(BatimentList)}')
    # print(f'{OrderBatimentDict}')

    # Méthode du prof : (Récommandée)
    PriorityOrder = {}
    PriorityOrderDetail = {}
    i = 1
    while len(BatimentList) > 0:
        batiment = min(BatimentList)
        # batiment
        list_infras = batiment.list_infras
        # print(f'Batiment id: {batiment.id_building}')
        # print(f'Min infra id: {min(list_infras)}')

        bat_dic = {
            'id_batiment': batiment.id_building,
            'priority': i,
            'metric': batiment.difficulty,
            'infra_oder': ' < '.join(infra.infra_id for infra in list_infras),
            'nb_of_infras': len(list_infras)
        }
        PriorityOrder[batiment.id_building] = bat_dic
        PriorityOrderDetail[batiment.id_building] = {
            **bat_dic,
            'infras_details':{
                f'{(infra.infra_id)}':
                    {'infra_id': infra.infra_id,
                     'priority': index_infra,
                     'metric': infra.difficulty,
                     'longueur': infra.length,
                     'nb_batiments_attache': int(infra.nb_houses),
                     } for index_infra, infra in enumerate(list_infras)
            }
        }
        BatimentList.remove(batiment)
        i += 1

    # Convert the object to a JSON-formatted string with indentation for readability
    priority_json = json.dumps(PriorityOrder, indent=4)
    print(f'Priority Order')
    print(f'{priority_json}')

    # priority_detail_json = json.dumps(PriorityOrderDetail, indent=4)
    # print(f'Priority Detail')
    # print(f'{priority_detail_json}')
