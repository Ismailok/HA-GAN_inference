# HA-GAN Inference Script

Ce dépôt contient un script Python pour l'inférence avec HA-GAN, un modèle de génération d'images médicales.

## Installation

1. Clonez ce dépôt :
   ```sh
   git clone https://github.com/ismailok/HA-GAN-inference.git
   cd HA-GAN-inference
   ```
2. Installez les dépendances nécessaires :
   ```sh
   pip install -r requirements.txt
   ```

## Téléchargement des modèles

Téléchargez les poids des modèles nécessaires et placez-les dans le dossier `checkpoint/HA_GAN_run1/` :

- <td align="center"><a href="https://drive.google.com/file/d/10AcfBPB_Tnjgy9bSj1qcZTW1s7qTIWRM/view?usp=sharing">Générateur</a></td>
- <td align="center"><a href="https://drive.google.com/file/d/10AcfBPB_Tnjgy9bSj1qcZTW1s7qTIWRM/view?usp=sharing">Encodeur</a></td>
- <td align="center"><a href="https://drive.google.com/file/d/10AcfBPB_Tnjgy9bSj1qcZTW1s7qTIWRM/view?usp=sharing">Sub-Encodeur</a></td>
- <td align="center"><a href="https://drive.google.com/file/d/10AcfBPB_Tnjgy9bSj1qcZTW1s7qTIWRM/view?usp=sharing">Discriminateur</a></td>



## Utilisation

Exécutez le script d'inférence avec :
```sh
python inference.py
```
Par défaut, le script charge une image test et génère une sortie correspondante.

## Exemple de Résultat

Voici un exemple de sortie générée par le modèle :

<p align="center">
  <img width="75%" height="%75" src="https://github.com/batmanlab/HA-GAN/blob/master/figures/sample_HA_GAN.png">
</p>


