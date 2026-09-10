import math
import cmath

class CooleyTukeyFFT:
    def fft(self, x):
        n = len(x)
        if n <= 1:
            return x
        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])
        t = [cmath.exp(-2j * math.pi * k / n) * odd[k] for k in range(n // 2)]
        return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]

class WelchPSDEngine:
    """
    Welch's Method for robust Power Spectral Density (PSD) estimation.
    Averages periodograms across overlapping windowed segments.
    """
    def __init__(self):
        self.fft_engine = CooleyTukeyFFT()

    def estimate_psd(self, x, segment_len=16, overlap=8):
        step = segment_len - overlap
        segments = []
        idx = 0
        while idx + segment_len <= len(x):
            segments.append(x[idx:idx+segment_len])
            idx += step
        if not segments:
            segments.append(x[:segment_len])

        window = [0.5 * (1.0 - math.cos(2.0 * math.pi * n / (segment_len - 1))) for n in range(segment_len)]
        w_norm = sum(w**2 for w in window)

        psd_accum = [0.0] * (segment_len // 2 + 1)
        for seg in segments:
            windowed = [seg[i] * window[i] for i in range(segment_len)]
            X = self.fft_engine.fft([complex(v, 0) for v in windowed])
            for k in range(segment_len // 2 + 1):
                p = (abs(X[k]) ** 2) / (w_norm * segment_len)
                if 0 < k < segment_len // 2:
                    p *= 2.0
                psd_accum[k] += p

        return [p / len(segments) for p in psd_accum]
