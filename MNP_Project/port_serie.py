import serial
import threading

# Remplace "COMX" par le bon port sous Windows (ex: "COM5"), ou "/dev/ttyACM0" sous Linux/macOS
PORT = "/dev/ttyACM0" #"COMX"  # ⚠️ À MODIFIER selon ton système
BAUDRATE = 115200

# Ouverture du port série
ser = serial.Serial(PORT, BAUDRATE, timeout=1)

def lire_port():
    """ Fonction qui lit et affiche les messages reçus du Micro:bit. """
    while True:
        if ser.in_waiting > 0:  # Vérifie si des données sont reçues
            message = ser.readline().decode('utf-8').strip()  # Lit et nettoie
            print("Micro:bit:", message)  # Affiche la réponse

# Thread pour la lecture du port série
thread = threading.Thread(target=lire_port, daemon=True)
thread.start()

print("Tape un message pour l'envoyer au Micro:bit (CTRL+C pour quitter).")

try:
    while True:
        dest = 2
        msg_type = 0
        payload = input("Message")  # Demande à l'utilisateur d'écrire
        message = chr(dest)+chr(msg_type)+payload
        ser.write(message.encode('utf-8'))  # Envoie le message au Micro:bit
except KeyboardInterrupt:
    print("\n🔌 Fermeture du port série...")
    ser.close()