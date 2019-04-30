import web
import config
import json


class Api_clientes:
    def get(self, id_cliente):
        try:
            # http://0.0.0.0:8080/api_clientes?user_hash=12345&action=get
            if id_cliente is None:
                result = config.model.get_all_clientes()
                clientes_json = []
                for row in result:
                    tmp = dict(row)
                    clientes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
            else:
                # http://0.0.0.0:8080/api_clientes?user_hash=12345&action=get&id_cliente=1
                result = config.model.get_clientes(int(id_cliente))
                clientes_json = []
                clientes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=put&nombre_c=Carmen&apepat_c=Ortiz&apemat_c=Romero&telefono_c=7751012307&email=carmen@gmai.com
    def put(self, nombre_c,apepat_c,apemat_c,telefono_c,email):
        try:
            config.model.insert_clientes(nombre_c,apepat_c,apemat_c,telefono_c,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=delete&id_cliente=5
    def delete(self, id_cliente):
        try:
            config.model.delete_clientes(id_cliente)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_clientes?user_hash=12345&action=update&id_cliente=9&nombre_c=Yoselin&apepat_c=Ortiz&apemat_c=Romero&telefono_c=7756789123&email=gabi@gmai.com
    def update(self, id_cliente, nombre_c,apepat_c,apemat_c,telefono_c,email):
        try:
            config.model.edit_clientes(id_cliente,nombre_c,apepat_c,apemat_c,telefono_c,email)
            clientes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            clientes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(clientes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_cliente=None,
            nombre_c=None,
            apepat_c=None,
            apemat_c=None,
            telefono_c=None,
            email=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_cliente=user_data.id_cliente

            nombre_c=user_data.nombre_c

            apepat_c=user_data.apepat_c

            apemat_c=user_data.apemat_c

            telefono_c=user_data.telefono_c

            email=user_data.email

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_cliente)
                elif action == 'put':
                    return self.put(nombre_c,apepat_c,apemat_c,telefono_c,email)
                elif action == 'delete':
                    return self.delete(id_cliente)
                elif action == 'update':
                    return self.update(id_cliente, nombre_c,apepat_c,apemat_c,telefono_c,email)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
