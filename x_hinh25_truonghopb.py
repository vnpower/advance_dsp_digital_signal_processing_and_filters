import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Bước 1: Xác định thông số bộ lọc
N = 128  # Số bậc của bộ lọc (chẵn)
fs = 10000  # Tần số lấy mẫu (Hz)
cutoff = (8+3)/128*10000  # Tần số cắt (Hz)
interp_factor = 16  # Hệ số nội suy (16N)
fft_size = interp_factor * N  # Kích thước FFT mở rộng

# Bước 2: Xác định đáp ứng tần số mong muốn H_k
num_frequencies = N  # Số mẫu tần số trong dải Nyquist
H_k = np.zeros(num_frequencies)  
cutoff_idx = int(cutoff / (fs / 2) * num_frequencies)  
H_k[:cutoff_idx] = 1  # Passband
H_k[cutoff_idx:] = 0  # Stopband
print(H_k)

# 🌟 Bước 3: Dịch H_k một góc pi/N theo chiều kim đồng hồ
H_k_shifted = H_k * np.exp(-1j * np.pi / N * np.arange(N))

# Bước 4: Tạo đối xứng phổ (để có bộ lọc thực)
H_full = np.concatenate([H_k_shifted, H_k_shifted[-2:0:-1].conj()])  

# Bước 5: Thực hiện FFT để thu được đáp ứng xung
h = np.fft.ifft(H_full).real  # Lấy phần thực

# Bước 6: Dịch h(n) N/2 mẫu và mở rộng bằng 0
h = np.roll(h, N // 2)  # Dịch N/2 mẫu để có nhân quả
h_padded = np.pad(h, (0, fft_size - N), mode='constant')  # Chèn (16N - N) mẫu 0

# Bước 7: Thực hiện FFT 16N điểm để nội suy đáp ứng tần số
H_interp = np.fft.fft(h_padded, n=fft_size)  # Đảm bảo FFT có kích thước đúng

# Bước 8: Dịch ngược FFT một góc pi/N ngược chiều kim đồng hồ
H_interp_shifted = H_interp * np.exp(1j * np.pi / N * np.arange(fft_size))  # Kích thước đúng

# Bước 9: Chuyển đổi biên độ sang dB
w = np.linspace(0, fs / 2, fft_size // 2)  # Trục tần số
H_db = 20 * np.log10(abs(H_interp_shifted[:len(w)]))
H_db = np.maximum(H_db, -220)  # Giới hạn nhỏ nhất ở -220 dB

# Bước 10: Vẽ đồ thị đáp ứng tần số
plt.figure(figsize=(7, 5))
plt.plot(w, H_db, 'k')  # Đường màu đen giống bài báo
plt.ylim(-220, 20)
plt.xlim(0, 5000)
plt.xlabel("TẦN SỐ (Hz)")
plt.ylabel("BIÊN ĐỘ (dB)")
plt.grid()

# Chú thích thông số bộ lọc
plt.text(3000, -20, f"N={N}", fontsize=12)

# Tiêu đề đồ thị theo bài báo
plt.title("Hình 25: Đáp ứng tần số của bộ lọc FIR - Trường hợp B (Tối ưu)")

# Hiển thị đồ thị
plt.show()
