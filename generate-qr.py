import qrcode
import os
import sys

# Generating QR Code
def generate_qr(url, code_dir, file_name, fill, back_color):
    # Set default values if not provided
    if url is None:
        url = "https://github.com/SashankNallapareddy"
    
    if file_name is None:
        file_name = "qr_001.png"
        
    if fill is None:
        fill = "black"
    
    if back_color is None:
        back_color = "white"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill=fill, back_color=back_color)
    if code_dir is not None:
        if not os.path.exists(code_dir):
            os.makedirs(code_dir)
        img.save(f'{code_dir}/{file_name}')
    else:
        img.save(f'{file_name}')
    
    print(f"Created QRCode for {url}")


# Get environment variables
url = os.getenv("QR_DATA_URL")
code_dir = os.getenv("QR_CODE_DIR")
file_name = os.getenv("QR_CODE_FILENAME")
fill = os.getenv("FILL_COLOR")
back_color = os.getenv("BACK_COLOR")

# Get URL from args
if len(sys.argv[1:]) > 0 and sys.argv[1] == '--url' and sys.argv[2] is not None:
    url = sys.argv[2]
    
if __name__ == '__main__':
    generate_qr(url, code_dir, file_name, fill, back_color)
