import qrcode
from PIL import Image

def generate_random_qr_code():
    # Generate random data (e.g., UUID)
    import uuid
    data = str(uuid.uuid4())
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Save QR code as image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"random_qr_code_{data}.png")

# Generate QR code
generate_random_qr_code()
