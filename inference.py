import SimpleITK as sitk
import torch
import numpy as np
from utils import trim_state_dict_name

# Configuration
latent_dim = 1024
save_step = 80000
batch_size = 1
img_size = 256
num_class = 0
exp_name = "HA_GAN_run1"

# Importation des modèles
if img_size == 256:
    from models.Model_HA_GAN_256 import Generator, Encoder, Sub_Encoder
elif img_size == 128:
    from models.Model_HA_GAN_128 import Generator, Encoder, Sub_Encoder

def load_model(model_class, checkpoint_path):
    model = model_class().cuda()
    ckpt = torch.load(checkpoint_path)['model']
    ckpt = trim_state_dict_name(ckpt)
    model.load_state_dict(ckpt)
    model.eval()
    return model

# Chargement des modèles
G = load_model(lambda: Generator(mode='eval', latent_dim=latent_dim, num_class=num_class), f"./checkpoint/{exp_name}/G_iter{save_step}.pth")
E = load_model(Encoder, f"./checkpoint/{exp_name}/E_iter{save_step}.pth")
Sub_E = load_model(lambda: Sub_Encoder(latent_dim=latent_dim), f"./checkpoint/{exp_name}/Sub_E_iter{save_step}.pth")

def inference(image_path):
    image = sitk.ReadImage(image_path)
    image_array = sitk.GetArrayFromImage(image)
    image_tensor = torch.tensor(image_array, dtype=torch.float32).unsqueeze(0).cuda()
    
    with torch.no_grad():
        encoded = E(image_tensor)
        sub_encoded = Sub_E(encoded)
        generated = G(sub_encoded)
    
    return generated.cpu().numpy()

if __name__ == "__main__":
    test_image_path = "path_to_test_image.nii"
    result = inference(test_image_path)
    print("Inference completed.")
