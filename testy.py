cart_items = {
            'a': {
                'name': "Mouse",
                'quantity': "3",
                'totalPrice': "1350",
            },

            'b': {
                'name': "Mouse 4",
                'quantity': "3",
                'totalPrice': "450",
            },

            'c': {
                'name': "Mouse 5",
                'quantity': "3",
                'totalPrice': "300",
            }
        }

ttl = sum([int(i['totalPrice']) for i in cart_items.values()])
print(ttl)