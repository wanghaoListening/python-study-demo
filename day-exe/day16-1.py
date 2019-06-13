import redis



def main():
    client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    client.set('username', 'admin')
    print(client.get('username'))