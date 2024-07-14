import requests
import time
from datetime import datetime, timedelta

# Fungsi untuk membaca data dari file
def read_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Fungsi untuk mengirim permintaan POST
def send_post_request(url, cookie, action, account_number):
    headers = {
        "Cookie": cookie,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Account {account_number}: {action} request successful")
    else:
        print(f"Account {account_number}: {action} request failed with status code: {response.status_code}")

# Fungsi untuk menampilkan hitung mundur
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(f"Countdown: {time_format}", end='\r')
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
            account_number = index + 1
            print(f'Processing account {account_number}/{num_accounts}')
            # Harvest farm
            send_post_request("https://recent-deals.vercel.app/api/trpc/userExp.harvestFarm?batch=1", cookie, "Harvest farm", account_number)
            time.sleep(5)
            # Start farm
            send_post_request("https://recent-deals.vercel.app/api/trpc/userExp.startFarm?batch=1", cookie, "Start farm", account_number)
            time.sleep(5)
        
        print('All accounts processed. Starting 8-hour countdown...')
        countdown(8 * 3600)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
