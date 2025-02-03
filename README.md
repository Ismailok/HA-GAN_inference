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

- [Generator]([[https://example.com/G_iter80000.pth](https://drive.google.com/file/d/1orNvz7DLsCn5KWKjjVpEL4e5mO0akf6g/view)](https://drive.google.com/file/d/1orNvz7DLsCn5KWKjjVpEL4e5mO0akf6g/view))
- [Encoder]([https://example.com/E_iter80000.pth](https://drive.google.com/file/d/1orNvz7DLsCn5KWKjjVpEL4e5mO0akf6g/view))
- [Sub-Encoder]([https://example.com/Sub_E_iter80000.pth](https://drive.google.com/file/d/1orNvz7DLsCn5KWKjjVpEL4e5mO0akf6g/view))

## Utilisation

Exécutez le script d'inférence avec :
```sh
python inference.py
```
Par défaut, le script charge une image test et génère une sortie correspondante.

## Exemple de Résultat

Voici un exemple de sortie générée par le modèle :

![Exemple de résultat]([https://example.com/result_image.png](https://github.com/batmanlab/HA-GAN/blob/master/figures/sample_HA_GAN.png))


