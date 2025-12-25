import os
import base64

class BitLockerSimulator:
    def __init__(self):
        self.recovery_key = None
        self.encrypted_data = None

    def generate_recovery_key(self):
        self.recovery_key = "-".join([os.urandom(2).hex().upper() for _ in range(8)])
        print(f"\nRecovery Key Generated: {self.recovery_key}")

    def encrypt_data(self, data):
        print("\nEncrypting data...")
        data_bytes = data.encode()
        self.encrypted_data = base64.b64encode(data_bytes).decode()
        print("Data encrypted successfully!")

    def attempt_recovery(self, user_key):
        print("\nAttempting recovery...")
        if user_key == self.recovery_key:
            print("✔ Correct Recovery Key! Access granted.")
            print("Original Data:", base64.b64decode(self.encrypted_data.encode()).decode())
        else:
            print("❌ Incorrect Recovery Key! Access denied.")

# -------- DEMO --------
if __name__ == "__main__":
    sim = BitLockerSimulator()

    sim.generate_recovery_key()

    sim.encrypt_data("This is my confidential file.")

    print("\nEncrypted Output:")
    print(sim.encrypted_data)

    user_input = input("\nEnter your Recovery Key to unlock: ")
    sim.attempt_recovery(user_input)
