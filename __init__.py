from . import AuraSR

import os
import shutil

current_folder = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(current_folder, "config.json")

target_folder = os.path.abspath(os.path.join(current_folder, "..", "..", "models", "aurasr"))

if not os.path.exists(target_folder):
    print(f'Creating target folder: {target_folder}')
    os.makedirs(target_folder)

target_file = os.path.join(target_folder, "config.json")

print(f'Copying {config_file} to {target_file}')
shutil.copy(config_file, target_file)

print('File copied successfully.')


NODE_CLASS_MAPPINGS = {**AuraSR.NODE_CLASS_MAPPINGS,}
NODE_DISPLAY_NAME_MAPPINGS = {**AuraSR.NODE_DISPLAY_NAME_MAPPINGS,}
