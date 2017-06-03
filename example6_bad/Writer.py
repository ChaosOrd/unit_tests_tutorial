

class CustomerDbWriter(object):

    def add_customer(self, db_connection, customer_id, customer_name):
        cur = db_connection.db.cursor()
        cur.execute("""
        INSERT INTO customers (id, name)
        VALUES (:customer_id, :customer_name)
        """, {'customer_id': customer_id, 'customer_name': customer_name})

        # cur.execute("""
        # INSERT INTO customers (name, id)
        # VALUES (:customer_name, :customer_id)
        # """, {'customer_id': customer_id, 'customer_name': customer_name})
