import math
from client import WelchPSDEngine

def main():
    print("=== Testing Welch PSD Estimation Engine ===")
    welch = WelchPSDEngine()
    sig = [math.sin(2 * math.pi * 0.25 * i) for i in range(64)]
    psd = welch.estimate_psd(sig, segment_len=16, overlap=8)
    print("Estimated PSD bins:", [round(p, 4) for p in psd])
    assert len(psd) == 9
    assert all(p >= 0 for p in psd)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
