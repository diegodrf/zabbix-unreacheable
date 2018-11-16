from ZabbixAPI_py import Zabbix

api = Zabbix(server='http://127.0.0.1/zabbix')
api.login(user='Admin', password='zabbix')

# Host - status
# Possible values are:
# 0 - (default) monitored host;
# 1 - unmonitored host.

# Item - state
# Possible values:
# 0 - (default) normal;
# 1 - not supported.

# Item - status
# Possible values:
# 0 - (default) enabled item;
# 1 - disabled item.

# Monta um array com todos os itens com status não reconhecido.
items = [item for item in api.item('get', {'output': ['itemid', 'name'],
                                           'filter': {'state': '1', 'status': '0'},
                                           'selectHosts': ['hostid', 'host', 'status']})]

# Retorna apenas os itens do array em que o host dono do item está com monitoramento ativo.
count = 1
for item in items:
    if item['hosts'][0]['status'] == '0':
        print('{} - {}'.format(count, item))
        count += 1