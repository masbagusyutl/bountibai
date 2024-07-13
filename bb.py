import requests
import time
from datetime import datetime, timedelta

# Fungsi untuk membaca data dari file
def read_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Fungsi untuk mengirim permintaan POST
def send_post_request(cookie):
    url = "https://recent-deals.vercel.app/api/trpc/userExp.startFarm?batch=1"
    headers = {
        "Cookie": cookie,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print("Request successful")
    else:
        print("Request failed")

# Fungsi untuk menampilkan hitung mundur
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        t -= 1
    print('Countdown finished! Starting again...')

# Fungsi utama untuk menjalankan proses
def main():
    cookies = read_data('data.txt')
    num_accounts = len(cookies)
    print(f'Total accounts: {num_accounts}')

    while True:
        for index, cookie in enumerate(cookies):
            print(f'Processing account {index + 1}/{num_accounts}')
            send_post_request(cookie)
            time.sleep(5)
        
        print('All accounts processed. Starting 8-hour countdown...')
        countdown(8 * 3600)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
