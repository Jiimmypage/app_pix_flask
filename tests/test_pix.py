import os
import sys

sys.path.append("C:/Users/douglas/Documents/appflask")

import pytest
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()

  
    payment_info = pix_instance.create_payment(base_dir="../")

    assert "payment_bank_id" in payment_info, "Chave 'payment_bank_id' ausente no retorno."
    assert "qr_code_path" in payment_info, "Chave 'qr_code_path' ausente no retorno."

    qr_code_path = payment_info["qr_code_path"]
    print(f"QR Code Path: {qr_code_path}")  

   
    qr_code_file_path = os.path.abspath(os.path.join("../", qr_code_path + ".png"))
    print(f"QR Code File Path: {qr_code_file_path}") 
   
    assert os.path.isfile(qr_code_file_path), f"Arquivo não encontrado: {qr_code_file_path}"
