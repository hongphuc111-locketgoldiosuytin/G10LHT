import subprocess
import sys
from multiprocessing import Pool

# Hàm để chạy lệnh spamv3.py
def run_spam(phone_number, spam_count):
    # Chạy script spamv3.py với các tham số đầu vào qua pipe
    subprocess.run(f"echo '{phone_number} {spam_count}' | python spamv3.py", shell=True)

if __name__ == "__main__":
    # Lấy tham số từ đầu vào (sdt, so_lan_spam, so_lan_chay_song_song)
    phone_number = sys.argv[1]
    spam_count = int(sys.argv[2])
    concurrent_runs = int(sys.argv[3])  # Số lần chạy song song

    # Tính toán số lần spam cho mỗi tiến trình
    spam_per_process = spam_count // concurrent_runs

    # Tạo danh sách các tham số (phone_number, spam_per_process) cho mỗi tiến trình
    args = [(phone_number, spam_per_process) for _ in range(concurrent_runs)]

    # Chạy các tiến trình song song
    with Pool(concurrent_runs) as pool:
        pool.starmap(run_spam, args)

    print(f"Đã hoàn thành việc spam {spam_count} lần với {concurrent_runs} tiến trình song song.")
