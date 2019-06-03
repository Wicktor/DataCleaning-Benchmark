from sqlalchemy import Column, Float, Integer, String, ARRAY
from persistance.db_connection.db_connector import Base


class Cloth(Base):
    __tablename__ = 'cloth'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    mrp = Column(String)
    price = Column(String)
    pdp_url = Column(String)
    brand_name = Column(String)
    product_category = Column(String)
    retailer = Column(String)
    description = Column(String)
    rating = Column(Float)
    review_count = Column(Float)
    style_attributes = Column(ARRAY(String))
    total_size = Column(ARRAY(String))
    available_size = Column(ARRAY(String))
    color = Column(String)

    def __init__(self, product_name, mrp, price, pdp_url, brand_name, product_category, retailer, description, rating, review_count, style_attributes, total_size, available_size, color):
        self.product_name = product_name
        self.mrp = mrp
        self.price = price
        self.pdp_url = pdp_url
        self.brand_name = brand_name
        self.product_category = product_category
        self.retailer = retailer
        self.description = description
        self.rating = rating
        self.review_count = review_count
        self.style_attributes = style_attributes
        self.total_size = total_size
        self.available_size = available_size
        self.color = color

    def __str__(self):
        string_vis = ''
        for attr, value in self.__dict__.items():
            string_vis = string_vis + '\n' + str(attr) + ' : ' + str(value)
        return string_vis

