import fitz
import os
from PIL import Image
import numpy as np
import io

def crop_pdfs_in_folder(folder):
    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(folder, filename)
            output_path = os.path.join(folder, filename.replace(".pdf", "_cropped.pdf"))
            
            doc = fitz.open(input_path)
            for page in doc:
                rect = page.cropbox  # Oldal eredeti mérete
                pix = page.get_pixmap()  # Pixmap létrehozása a fehér margók felismeréséhez
                
                img_bytes = pix.tobytes("ppm")  # PPM formátumban mentés
                img = Image.open(io.BytesIO(img_bytes)).convert("L")  # Betöltés és átalakítás szürkeárnyalatossá
                img = np.array(img)
                
                # Fehér pixelek helyének keresése (0=black, 255=white)
                cols = np.where(img.min(axis=0) < 250)[0]
                rows = np.where(img.min(axis=1) < 250)[0]
                
                if cols.size > 0 and rows.size > 0:
                    x0, x1 = cols[0], cols[-1]
                    y0, y1 = rows[0], rows[-1]
                    
                    # Koordináták konvertálása PDF méretarányba
                    new_rect = fitz.Rect(
                        rect.x0 + x0 * rect.width / pix.width,
                        rect.y0 + y0 * rect.height / pix.height,
                        rect.x0 + x1 * rect.width / pix.width,
                        rect.y0 + y1 * rect.height / pix.height,
                    )
                    
                    page.set_cropbox(new_rect)
            
            doc.save(output_path)
            doc.close()
            print(f"Cropped: {filename} -> {output_path}")

if __name__ == "__main__":
    folder_path = input("Add meg a könyvtár elérési útvonalát: ").strip()
    if os.path.isdir(folder_path):
        crop_pdfs_in_folder(folder_path)
    else:
        print("Hibás könyvtár elérési útvonal!")
