import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = (
    "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2026/refs/heads/main/dati/integrazione_derivazione/oscilloscope.csv"
)

df = pd.read_csv(url)
print(df.columns)

t = df["time"].to_numpy()
ch1 = df["signal1"].to_numpy()
ch2 = df["signal2"].to_numpy()

# Derivata tramite differenza centrale con passo n 
def central_difference(y: np.ndarray, t: np.ndarray, n: int = 1):
  t_mid = t[n:-n]
  dy_dt = (y[2 * n :] - y[: -2 * n]) / (t[2 * n :] - t[: -2 * n])
  return t_mid, dy_dt


# Grafico dei segnali dell'oscilloscopio
plt.figure(figsize=(9, 5))
plt.plot(t, ch1, label="signal1")
plt.plot(t, ch2, label="signal2")
plt.title("Segnali dell'oscilloscopio")
plt.xlabel("Tempo [s]")
plt.ylabel("Ampiezza [V]")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

# Derivate di signal1 per diversi valori di n
for n in [1, 3, 5, 10]:
  t_mid, dch1 = central_difference(ch1, t, n=n)
  ax1.plot(t_mid, dch1, label=f"n = {n}")

ax1.set_title("Derivata di signal1")
ax1.set_ylabel("d(signal1)/dt")
ax1.grid(True, alpha=0.3)
ax1.legend()

# Derivate di signal2 per diversi valori di n
for n in [1, 3, 5, 10]:
  t_mid, dch2 = central_difference(ch2, t, n=n)
  ax2.plot(t_mid, dch2, label=f"n = {n}")

ax2.set_title("Derivata di signal2")
ax2.set_xlabel("Tempo [s]")
ax2.set_ylabel("d(signal2)/dt")
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()