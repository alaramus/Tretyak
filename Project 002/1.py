from ping3 import ping, verbose_ping

def check_google_connectivity():
    google_servers = ['google.com', '8.8.8.8', '8.8.4.4']  # Добавлены несколько адресов Google DNS

    for server in google_servers:
        result = ping(server)
        if result is not None:
            print(f'Ping to {server} successful. Round trip time: {result} ms')
        else:
            print(f'Ping to {server} failed.')

if __name__ == "__main__":
    check_google_connectivity()
