import torch
import os
import folder_paths
import numpy as np
from PIL import Image
from .aura_sr import AuraSR


device = "cuda" if torch.cuda.is_available() else "cpu"
folder_paths.folder_names_and_paths["aurasr"] = ([os.path.join(folder_paths.models_dir, "aurasr")], folder_paths.supported_pt_extensions)


def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class AuraSR_ModelLoader_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aurasr_model": (folder_paths.get_filename_list("aurasr"), ),
            }
        }

    RETURN_TYPES = ("AURASRMODEL",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "load_model"
    CATEGORY = "🔎AURASR"
  
    def load_model(self, aurasr_model):
        if not aurasr_model:
            raise ValueError("Please provide the aurasr_model parameter with the name of the model file.")

        aurasr_path = folder_paths.get_full_path("aurasr", aurasr_model)
      
        generator = AuraSR.from_local(aurasr_path)
      
        return [generator]


class AuraSR_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pipe": ("AURASRMODEL",),
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "aurasr_image"
    CATEGORY = "🔎AURASR"
                       
    def aurasr_image(self, pipe, image):
        
        image_t = tensor2pil(image)
        upscaled_image = pipe.upscale_4x(image_t)
        output = pil2tensor(upscaled_image)
        print(output.shape)

        return (output,)


class AuraSR_Lterative_Zho:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pipe": ("AURASRMODEL",),
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "aurasr_image"
    CATEGORY = "🔎AURASR"
                       
    def aurasr_image(self, pipe, image):

        processed_images = []
        for img_tensor in image:         
            image_t = tensor2pil(img_tensor)
            upscaled_image = pipe.upscale_4x(image_t)  
            output = pil2tensor(upscaled_image)
            output_t = output.squeeze(0)
            processed_images.append(output_t)
            
        return (processed_images,)


NODE_CLASS_MAPPINGS = {
    "AuraSR_ModelLoader_Zho": AuraSR_ModelLoader_Zho,
    "AuraSR_Zho": AuraSR_Zho,
    "AuraSR_Lterative_Zho": AuraSR_Lterative_Zho
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AuraSR_ModelLoader_Zho": "🔎AuraSR Model",
    "AuraSR_Zho": "🔎AuraSR(image)",
    "AuraSR_Lterative_Zho": "🔎AuraSR(video)",
}
