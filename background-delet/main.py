import asyncio

from rembg import remove
from PIL import Image
from pathlib import Path


async def remove_bg():
    list_of_extension = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extension:
        all_files.extend(Path('input_imgs').glob(ext))

    print(all_files)

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'output_imgs/{file_name}_output.png'
        input_img = Image.open(input_path)

        # Downloading data from 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx'
        # to file 'C:\Users\Admin\.u2net\u2net.onnx'.
        output_img = remove(input_img)
        output_img.save(output_path)

        print(f'Completed: {index + 1}/{len(all_files)}')


async def main():
    await remove_bg()


if __name__ == '__main__':
    asyncio.run(main())
