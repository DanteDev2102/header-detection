import requests

def main(dominio):
    if dominio:
        try:
            url = requests.get(url=dominio)
            headers = dict(url.headers)
            for i in headers:
                print(f'{i}: {headers[i]}')
        except:
            print('no se han podido sacar las cabezeras')
    else:
        print('no hay objetivo')
        if __name__ == '__main__':
            main()

dominio = input('ingresa la url a analizar: ')
main(dominio)