# Wi-Fi QR Generator

This project generates **Wi-Fi credentials** (SSID and password) along with QR codes in **SVG format**.  
It automatically creates both **2.4GHz** and **5GHz** Wi-Fi networks with random names and secure passwords, and produces QR codes that can be scanned to connect instantly.  

##  Features
- ✅ Generates random and secure Wi-Fi passwords (excluding ambiguous characters like `I`, `l`, `i`, `L`)  
- ✅ Creates random Wi-Fi network names (SSIDs)  
- ✅ Generates QR codes for both **2.4GHz** and **5GHz** networks  
- ✅ Outputs ready-to-use **SVG files** with text + QR codes  
- ✅ Saves QR images in `.png` format  

##  Technologies Used
- [Python](https://www.python.org/)  
- [qrcode](https://pypi.org/project/qrcode/) – QR code generation  
- [svgwrite](https://pypi.org/project/svgwrite/) – SVG file creation  
- [Pillow (PIL)](https://pypi.org/project/Pillow/) – Image processing  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/wifi-qr-generator.git
cd wifi-qr-generator
```
## Install dependencies:
```
pip install qrcode[pil] svgwrite pillow
```
Run the script:
```
python main.py 
```
or 
```
python3 main.py
```
The script will generate 20 sets of Wi-Fi networks by default.

Each run creates:

Random SSID for 2.4GHz and 5GHz

Secure password

SVG file with text + QR codes

PNG QR codes in the /png directory

Example output:
```
SVG file saved: svg/WiFi_1.svg Home_net1234 Home_net1234_5G password aB8dE9gH2k
```
Configuration
```
n = 20 → number of Wi-Fi sets to generate

svg_dir = "svg" → output folder for SVGs

qr_dir = "png" → output folder for QR PNGs
```
