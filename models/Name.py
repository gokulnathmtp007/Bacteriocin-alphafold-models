import os

# List of bacteriocins
bacteriocins = [
    "Nisin_Test_a557c",
    "Pediocin_Test_c9959_0",
    "Plantaricin_E_568ce",
    "Plantaricin_A_2087d",
    "Enterocin_P_8900c",
    "Enterocin_JSA_e64fd",
    "Enterocin_A_98615",
    "Subtilosin_A_6ee4f",
    "Leucocin_A_be1c5",
    "Lacticin3147_A2_d98b2_0",
    "Lacticin3147_A1",
    "Mersacidin"
]

# Base directory where you want to create folders
base_dir = "Bacteriocin-alphafold-models"

# Create base folder if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Create subfolders for each bacteriocin
for name in bacteriocins:
    folder_path = os.path.join(base_dir, name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

print("All bacteriocin folders created successfully!")
