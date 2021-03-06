from application import db

class customer(db.model):
    customer_id = db.column(db.integer, primary_key= True)
    first_name= db.column(db.char(50))
    last_name= db.column(db.char(50))
    address= db.columndb.column(db.char(255))
    phone_no= db.column(db.integer)
    email_address= db.column(db.char(50))
    customer_orders= db.relationship('order', backref= 'customer')

class order(db.model):
    order_id = db.column(db.integer, primary_key= True)
    item= db.column(db.string(50))
    quantity= db.column(db.integer)
    price= db.column(db.float)
    customer_id= db.column(db.integer, db.foreign_key('customer.customer_id'))
    
    # def __repr__(self):
    #     return f"{self.quantity} {self.item} {self.price} {self.customer_id}"
    
# class Customer(db.Model):
#     cust_id= db.Column(db.Integer, primary_key= True)
#     first_name= db.Column(db.String(50))
#     last_name= db.Column(db.String(50))
#     address= db.Column(db.String(50))
#     phone_no= db.Column(db.Integer)
#     e_mail= db.Column(db.Integer)
#     customer_orders= db.relationship('Order', backref='customer')

# class Order(db.Model):
#     order_no= db.Column(db.Integer, primary_key= True)
#     item= db.Column(db.String(50))
#     quantity= db.Column(db.Integer)
#     price= db.Column(db.Integer)
#     cust_id= db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
