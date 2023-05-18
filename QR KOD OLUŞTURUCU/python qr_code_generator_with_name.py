import qrcode

def generate_qr_code(data, version=1, box_size=10, border=4):
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def print_header(name):
    print(r"""
   

            WİNCHASTER


    """)
    print(f"\n{name}, QR kodu oluşturucusuna hoş geldiniz.")

def main():
    name = "Lancelot"  # İsminizi buraya "Lancelot" olarak değiştirin
    print_header(name)
    data = input("QR kodu için veri girin: ")
    qr_code = generate_qr_code(data)
    qr_code.show()

    print(f"\n{name}, QR kodu başarıyla oluşturuldu.")

if __name__ == '__main__':
    main()
