import os
from uuid import uuid4
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        img_dir = os.path.join(base_dir, "static", "img")
        
        os.makedirs(img_dir, exist_ok=True)

        bank_payment_id = uuid4()

        hash_payment = f'hash_payment_{bank_payment_id}'
        
        img = qrcode.make(hash_payment)

        file_name = f"qr_code_payment_{bank_payment_id}.png"
        file_path = os.path.join(img_dir, file_name)

        img.save(file_path)

        return {
            "payment_bank_id": str(bank_payment_id),
            "qr_code_path": os.path.join("static", "img", file_name.replace(".png", ""))
        }
