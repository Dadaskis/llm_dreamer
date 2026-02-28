import os
import random
import string
import getpass
import platform

def generate_fake_passwords():
    """Generate hilariously bad password suggestions"""
    bad_passwords = [
        "123456", "password", "qwerty", "abc123", "password123",
        "admin", "letmein", "welcome", "monkey", "dragon",
        "sunshine", "iloveyou", "trustno1", "master", "hello",
        "world", "passw0rd", "123456789", "password1", "admin123",
        "12345678", "qwerty123", "welcome123", "password!", "admin!",
        f"{random.randint(1000, 9999)}", f"123{random.choice(string.ascii_letters)}",
        f"{random.choice(string.ascii_letters)}123", "p@ssw0rd", "p@$$w0rd",
        "abc123456", "123456abc", "qwerty123456", "password123456",
        f"password{random.randint(10, 99)}", f"123456{random.choice(string.ascii_letters)}",
        f"!@#{random.randint(100, 999)}", "p@ssw0rd!", "qwert123!",
        "abc123!@#", "password123!", "admin123456", f"!@#{random.choice(string.ascii_letters)}123"
    ]
    
    return [random.choice(bad_passwords) for _ in range(10)]

def simulate_virus_scan():
    """Simulate a virus scan with dramatic effects"""
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                         🔴 FAKE VIRUS ACTIVATED 🔴                                        ║")
    print("║      This is a harmless demonstration. No actual harm will occur to your system.          ║")
    print("║            Press Ctrl+C to exit if you're uncomfortable with this simulation.             ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Simulate scanning process
    print("🔍 SCANNING YOUR COMPUTER FOR PASSWORDS...")
    print("   Starting system analysis...")
    for i in range(5):
        print(f"   [{i+1}/5] Accessing system files...")
        import time
        time.sleep(0.5)
    
    print("\n🔍 ANALYZING SAFETY LEVELS...")
    for i in range(3):
        print(f"   [{i+1}/3] Computing vulnerability assessment...")
        time.sleep(0.3)
    
    print("\n⚠️  SECURITY WARNING: MULTIPLE WEAK PASSWORDS DETECTED!")
    print("   File: /home/user/.config/login.txt")
    print("   File: /home/user/secure_notes.txt")
    print("   File: /home/user/finance_documents.txt")
    print("   File: /home/user/passwords.db")
    
    # Display fake password suggestions
    print("\n📝 ANALYSIS COMPLETE! HERE ARE YOUR CURRENT PASSWORD SUGGESTIONS:")
    print("   (These are worse than most real passwords, but at least they're original!)")
    print()
    
    fake_passwords = generate_fake_passwords()
    
    for i, password in enumerate(fake_passwords, 1):
        strength = random.choice(["LOW", "VERY LOW", "EXTREMELY LOW", "PATHETIC"])
        print(f"   {i}. '{password}' [{strength} STRENGTH]")

def pseudo_security_warning():
    """Display some fake security warnings"""
    warnings = [
        "⚠️  WARNING: This system has been flagged for displaying offensive content!",
        "⚠️  WARNING: Native code injection detected!",
        "⚠️  WARNING: Strange user behavior detected!",
        "⚠️  WARNING: Artistic license violation!",
        "⚠️  WARNING: Repository modified!",
        "⚠️  WARNING: User profile compromised!",
        "⚠️  WARNING: Cultural sensitivity issues found!",
        "⚠️  WARNING: Internet Explorer detected!"
    ]
    
    for warning in warnings:
        print(warning)
        import time
        time.sleep(0.5)

def disk_encryption_simulation():
    """Simulate disk encryption to make it more believable"""
    print("\n🔐 SIMULATING DISK ENCRYPTION...")
    print("   Initializing self-encryption protocol...")
    print("   Installing ransomware components...")
    for i in range(10):
        progress = "█" * (i+1) + "░" * (10-i) if i < 10 else "██████████"
        print(f"   {progress} {((i+1)*10)}% Complete", end="\r")
        import time
        time.sleep(0.2)
    print("\n✅ Encryption complete!" if random.choice([True, False]) else "\n⚠️  Encryption failed!")

def main():
    """Main function that ties everything together"""
    try:
        print("Initializing fake virus simulation...")
        print("OS detected:", platform.system())
        print("User:", getpass.getuser())
        print()
        
        # Simulate virus activation
        simulate_virus_scan()
        
        # Add more dramatic elements
        print("\n🎭 ADDITIONAL SECURITY ANALYSIS:")
        pseudo_security_warning()
        
        # Disk encryption simulation
        disk_encryption_simulation()
        
        print("\n" + "="*70)
        print("🔒 FAKE VIRUS SIMULATION COMPLETE!")
        print("🤖 This was just a demonstration. No actual viruses were created or")
        print("   installed on your computer.")
        print("   Your passwords are safe... for now!")
        print("="*70)
        
        # Humorous ending
        print("\nVERTISEMENT: Our fake virus also detects:")
        advertisements = [
            "✗ 327 security issues",
            "✗ 13,542 passwords",
            "✗ 84.2% insufficient security",
            "✗ 93.7% insecure browsing",
            "✗ 42 unsecured data streams",
            "✗ 237 zero-day vulnerabilities",
            "✗ 73 malicious files"
        ]
        
        for ad in advertisements:
            print(f"   {ad}")
        
        print("\n🌈 REMARKABLE BONUS: The current password is 'iHateSecurity'")
        print("   This password has been tested and found to be more secure than average")
        print("   because it's easily identifiable as a poor choice!")
        
        # Dedication section
        print("\n🎉 DEDICATION: To all security researchers out there")
        print("   who prefer actual malware over this hilarious demo...")
        print("   Happy to know you're working hard to keep the world safe!")
        
    except KeyboardInterrupt:
        print("\n\n🛑 USER ABORTED SIMULATION")
        print("   Emergency shutdown initiated...")
        print("   No damage was done to your system")

if __name__ == "__main__":
    main()