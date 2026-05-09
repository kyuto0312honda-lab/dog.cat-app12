import os
import shutil

dog_source = r"PetImages\Dog"
cat_source = r"PetImages\Cat"

target_dog = r"dataset\dog"
target_cat = r"dataset\cat"

os.makedirs(target_dog, exist_ok=True)
os.makedirs(target_cat, exist_ok=True)

# 犬画像コピー
dog_files = [
    f for f in os.listdir(dog_source)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

for file in dog_files[:500]:
    try:
        shutil.copy2(
            os.path.join(dog_source, file),
            os.path.join(target_dog, file)
        )
    except Exception:
        pass

# 猫画像コピー
cat_files = [
    f for f in os.listdir(cat_source)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

for file in cat_files[:500]:
    try:
        shutil.copy2(
            os.path.join(cat_source, file),
            os.path.join(target_cat, file)
        )
    except Exception:
        pass

print(f"犬画像: {len(os.listdir(target_dog))}枚")
print(f"猫画像: {len(os.listdir(target_cat))}枚")
print("コピー完了！")