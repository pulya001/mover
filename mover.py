import os
import shutil

os.chdir('/home/dmitry/Загрузки')

print('********|||||||||******SRARRRT********||||||||||********')

directories = [
    "текст", "сертификаты", "пдф", "звуки", "видео",
    "таблицы", "архивы", "скрипты", "картинки",
    "конфиг рубик", "прошивки", "презентации", "логи",
    "логи WireShark", "прошивки Beward", "Postman коллекции",
    "конфиг микрота", "3D Притнер"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

file_extensions = {
    (".txt", ".DOCX", ".docx", ".doc"): "текст",
    (".udx",): "прошивки Beward",
    (".pptx",): "презентации",
    (".dat",): "конфиг рубик",
    (".bin",): "прошивки",
    (".flv", ".mp4"): "видео",
    (".svg", ".png", ".bmp", ".jpg", ".jpeg"): "картинки",
    (".pdf",): "пдф",
    (".wav", ".mp3"): "звуки",
    (".csv", ".xlsx", ".ods", ".odt"): "таблицы",
    (".zip", ".7z", ".tgz"): "архивы",
    (".cer", ".crt"): "сертификаты",
    (".pcap", ".dump"): "логи WireShark",
    (".log",): "логи",
    (".rsc",): "конфиг микрота",
    (".sh", ".py"): "скрипты",
    (".json",): "Postman коллекции",
    (".gx", ".stl"): "3D Притнер"
}

for file in os.listdir():
    try:
        if file == "mover.py":
            print("Skipping mover.py...")
            continue

        target_directory = None
        for extensions, directory in file_extensions.items():
            if file.endswith(extensions):
                target_directory = directory
                break

        if target_directory:
            shutil.move(file, target_directory)

    except Exception as e:
        print(f"Ошибка при переносе файла {file}: {e}")

print('*******||||||||||*******FINISHHH*******||||||||||*********')
