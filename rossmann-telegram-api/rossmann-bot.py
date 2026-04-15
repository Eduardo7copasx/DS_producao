import requests
import json
import pandas as pd
from flask import Flask, request, Response

# constante
token = '8668303242:AAGdb8ldVTx5zbvRH0SnPwquL56lSWAWI3U'
webhook_url = 'https://9a077a0a8272d5.lhr.life'  # ← atualizar quando reconectar o tunnel


def set_webhook():
    url = 'https://api.telegram.org/bot{}/setWebhook?url={}'.format(token, webhook_url)
    r = requests.get(url)
    print('Webhook set status: {}'.format(r.status_code))
    print('Webhook response: {}'.format(r.json()))


def send_message(chat_id, text):
    try:
        url = 'https://api.telegram.org/bot{}/'.format(token)
        url = url + 'sendMessage?chat_id={}'.format(chat_id)
        r = requests.post(url, json={'text': text})
        print('send_message status code: {}'.format(r.status_code))
    except Exception as e:
        print('ERRO em send_message: {}'.format(e))
    return None


def load_dataset(store_id):
    try:
        df10 = pd.read_csv('test.csv')
        df_store_raw = pd.read_csv('store.csv')

        df_test = pd.merge(df10, df_store_raw, how='left', on='Store')
        df_test = df_test[df_test['Store'] == store_id]

        if not df_test.empty:
            df_test = df_test[df_test['Open'] != 0]
            df_test = df_test[~df_test['Open'].isnull()]
            df_test = df_test.drop('Id', axis=1)
            data = json.dumps(df_test.to_dict(orient='records'))
            print('load_dataset OK — {} linhas encontradas'.format(len(df_test)))
        else:
            print('load_dataset: loja {} não encontrada'.format(store_id))
            data = 'error'

    except Exception as e:
        print('ERRO em load_dataset: {}'.format(e))
        data = 'error'

    return data


def predict(data):
    try:
        url = 'https://rossmannproject-production.up.railway.app/rossmann/predict'  # ← URL atualizada
        header = {'Content-type': 'application/json'}

        r = requests.post(url, data=data, headers=header)
        print('predict status code: {}'.format(r.status_code))

        d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())
        print('predict OK — shape: {}'.format(d1.shape))
        return d1

    except Exception as e:
        print('ERRO em predict: {}'.format(e))
        return None


def parse_message(message):
    try:
        chat_id = message['message']['chat']['id']
        store_id = message['message']['text']
        store_id = store_id.replace('/', '')

        try:
            store_id = int(store_id)
        except ValueError:
            print('parse_message: store_id inválido — {}'.format(store_id))
            store_id = 'error'

        print('parse_message OK — chat_id: {}, store_id: {}'.format(chat_id, store_id))
        return chat_id, store_id

    except Exception as e:
        print('ERRO em parse_message: {}'.format(e))
        return None, 'error'


# API initialize
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        print('Mensagem recebida: {}'.format(message))

        chat_id = None
        try:
            chat_id, store_id = parse_message(message)

            if store_id != 'error':
                data = load_dataset(store_id)

                if data != 'error':
                    d1 = predict(data)

                    if d1 is not None:
                        d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()
                        msg = 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format(
                            d2['store'].values[0],
                            d2['prediction'].values[0]
                        )
                        send_message(chat_id, msg)
                    else:
                        send_message(chat_id, 'Erro ao fazer a predição, tente novamente')
                else:
                    send_message(chat_id, 'Loja não encontrada')
            else:
                send_message(chat_id, 'ID inválido, envie apenas o número da loja. Ex: /22')

        except Exception as e:
            print('ERRO GERAL no index: {}'.format(e))
            if chat_id:
                send_message(chat_id, 'Erro interno: {}'.format(str(e)))

        return Response('Ok', status=200)

    else:
        return '<h1>Rossmann Telegram Bot</h1>'


if __name__ == '__main__':
    set_webhook()  # ← seta o webhook automaticamente ao iniciar
    app.run(host='0.0.0.0', port=5000)