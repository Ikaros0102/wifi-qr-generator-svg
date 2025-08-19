import qrcode
import random
import string
import svgwrite
from PIL import ImageFont
import os

# Функция для генерации случайного пароля
def generate_password(length=10):
    # Исключаем буквы I, l, i, и L
    chars = string.ascii_letters + string.digits
    chars = chars.replace('I', '').replace('l', '').replace('i', '').replace('L', '')
    return ''.join(random.choice(chars) for _ in range(length))

# Функция для создания имени сети Wi-Fi с номером
def generate_wifi_name(base_name="Home_net"):
    return f"{base_name}{random.randint(100, 9999)}"

# Функция для создания QR-кода в SVG формате
def create_qr_code_svg(ssid, password):
    wifi_info = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_info)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

# Функция для создания SVG файла с двумя сетями
def create_combined_svg(ssid_24, ssid_5g, password, output_file, index, qr_dir):
    dwg = svgwrite.Drawing(output_file, profile='tiny')
    font_size = 32
    font_family = "Microsoft YaHei UI"
    qr_size = 200  # Размеры QR-кодов
    
    # Функция для добавления текста с отступом, QR-кода и рамки
    def draw_text_and_qr(dwg, position, ssid, password, network_type, index):
        x, y = position
        rect_width = 600
        rect_height = qr_size + 20
        
        # Добавляем рамку
        dwg.add(dwg.rect(insert=(x - 10, y - 10), size=(rect_width, rect_height), fill='none', stroke='black', stroke_width=2))

        # Добавляем текст и QR-код
        dwg.add(dwg.text(f"Название сети {network_type}:", insert=(x, y + 40), font_size=font_size, font_family=font_family, font_weight="normal"))
        dwg.add(dwg.text(f"      {ssid}", insert=(x, y + 80), font_size=font_size, font_family=font_family, font_weight="bold"))
        dwg.add(dwg.text(f"Пароль:", insert=(x, y + 120), font_size=font_size, font_family=font_family, font_weight="normal"))
        dwg.add(dwg.text(f"      {password}", insert=(x, y + 160), font_size=font_size, font_family=font_family, font_weight="bold"))
        qr_image = create_qr_code_svg(ssid, password)
        qr_filename = os.path.join(qr_dir, f"qr_{network_type}_{index}.png").replace("\\", "/")

        qr_image.save(qr_filename)
        dwg.add(dwg.image(href=qr_filename, insert=(x + 380, y), size=(qr_size, qr_size)))

    draw_text_and_qr(dwg, (50, 50), ssid_24, password, "2.4GHz", index)   
    draw_text_and_qr(dwg, (50, 370), ssid_5g, password, "5GHz", index)

    dwg.save()

def main():
    n = 20  
    svg_dir = "svg"
    qr_dir = "/png"
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(qr_dir, exist_ok=True)

    for i in range(n):
        ssid_24 = generate_wifi_name()
        ssid_5g = f"{ssid_24}_5G"
        password = generate_password()
        output_file = os.path.join(svg_dir, f"WiFi_{i + 1}.svg")
        create_combined_svg(ssid_24, ssid_5g, password, output_file, i + 1, qr_dir)
        print(f"SVG файл сохранен: {output_file} {ssid_24} {ssid_5g} пароль {password}")

if __name__ == "__main__":
    main()
