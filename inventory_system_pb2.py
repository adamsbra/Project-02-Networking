# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory_system.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='inventory_system.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16inventory_system.proto\"\x89\x01\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x05 \x01(\t\x12\x11\n\tsale_cost\x18\x06 \x01(\x01\x12\x16\n\x0ewholesale_cost\x18\x07 \x01(\x01\"}\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12 \n\x08products\x18\x04 \x03(\x0b\x32\x0e.ProductAmount\x12\x0f\n\x07is_paid\x18\x05 \x01(\x08\x12\x12\n\nis_shipped\x18\x06 \x01(\x08\"\x15\n\x07OrderID\x12\n\n\x02id\x18\x01 \x01(\t\"\x1a\n\x07Success\x12\x0f\n\x07success\x18\x01 \x01(\x08\"-\n\x11ProductIdentifier\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"O\n\rProductAmount\x12.\n\x12product_identifier\x18\x01 \x01(\x0b\x32\x12.ProductIdentifier\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"Y\n\x12ProductDescription\x12.\n\x12product_identifier\x18\x01 \x01(\x0b\x32\x12.ProductIdentifier\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"[\n\x13ProductManufacturer\x12.\n\x12product_identifier\x18\x01 \x01(\x0b\x32\x12.ProductIdentifier\x12\x14\n\x0cmanufacturer\x18\x02 \x01(\t\"T\n\x0fProductSaleCost\x12.\n\x12product_identifier\x18\x01 \x01(\x0b\x32\x12.ProductIdentifier\x12\x11\n\tsale_cost\x18\x02 \x01(\x01\"^\n\x14ProductWholesaleCost\x12.\n\x12product_identifier\x18\x01 \x01(\x0b\x32\x12.ProductIdentifier\x12\x16\n\x0ewholesale_cost\x18\x02 \x01(\x01\"$\n\x0cManufacturer\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\x94\x05\n\x0fInventorySystem\x12,\n\nGetProduct\x12\x12.ProductIdentifier\x1a\x08.Product\"\x00\x12,\n\nAddProduct\x12\x08.Product\x1a\x12.ProductIdentifier\"\x00\x12\x38\n\x19GetProductsByManufacturer\x12\r.Manufacturer\x1a\x08.Product\"\x00\x30\x01\x12*\n\x12GetProductsInStock\x12\x06.Empty\x1a\x08.Product\"\x00\x30\x01\x12\x33\n\x15\x44\x65\x63reaseProductAmount\x12\x0e.ProductAmount\x1a\x08.Success\"\x00\x12\x33\n\x15IncreaseProductAmount\x12\x0e.ProductAmount\x1a\x08.Success\"\x00\x12=\n\x19UpdateProductManufacturer\x12\x14.ProductManufacturer\x1a\x08.Success\"\x00\x12;\n\x18UpdateProductDescription\x12\x13.ProductDescription\x1a\x08.Success\"\x00\x12\x35\n\x15UpdateProductSaleCost\x12\x10.ProductSaleCost\x1a\x08.Success\"\x00\x12?\n\x1aUpdateProductWholesaleCost\x12\x15.ProductWholesaleCost\x1a\x08.Success\"\x00\x12\x1e\n\x08GetOrder\x12\x08.OrderID\x1a\x06.Order\"\x00\x12\x1e\n\x08\x41\x64\x64Order\x12\x06.Order\x1a\x08.OrderID\"\x00\x12!\n\x0bUpdateOrder\x12\x06.Order\x1a\x08.Success\"\x00\x62\x06proto3'
)




_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Product.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Product.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Product.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Product.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='Product.manufacturer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sale_cost', full_name='Product.sale_cost', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wholesale_cost', full_name='Product.wholesale_cost', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=164,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Order.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='Order.destination', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='Order.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='products', full_name='Order.products', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_paid', full_name='Order.is_paid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_shipped', full_name='Order.is_shipped', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=291,
)


_ORDERID = _descriptor.Descriptor(
  name='OrderID',
  full_name='OrderID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='OrderID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=314,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Success.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=342,
)


_PRODUCTIDENTIFIER = _descriptor.Descriptor(
  name='ProductIdentifier',
  full_name='ProductIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ProductIdentifier.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ProductIdentifier.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=389,
)


_PRODUCTAMOUNT = _descriptor.Descriptor(
  name='ProductAmount',
  full_name='ProductAmount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_identifier', full_name='ProductAmount.product_identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ProductAmount.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=470,
)


_PRODUCTDESCRIPTION = _descriptor.Descriptor(
  name='ProductDescription',
  full_name='ProductDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_identifier', full_name='ProductDescription.product_identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ProductDescription.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=561,
)


_PRODUCTMANUFACTURER = _descriptor.Descriptor(
  name='ProductManufacturer',
  full_name='ProductManufacturer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_identifier', full_name='ProductManufacturer.product_identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='ProductManufacturer.manufacturer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=654,
)


_PRODUCTSALECOST = _descriptor.Descriptor(
  name='ProductSaleCost',
  full_name='ProductSaleCost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_identifier', full_name='ProductSaleCost.product_identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sale_cost', full_name='ProductSaleCost.sale_cost', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=740,
)


_PRODUCTWHOLESALECOST = _descriptor.Descriptor(
  name='ProductWholesaleCost',
  full_name='ProductWholesaleCost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_identifier', full_name='ProductWholesaleCost.product_identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wholesale_cost', full_name='ProductWholesaleCost.wholesale_cost', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=742,
  serialized_end=836,
)


_MANUFACTURER = _descriptor.Descriptor(
  name='Manufacturer',
  full_name='Manufacturer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='Manufacturer.manufacturer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=874,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=883,
)

_ORDER.fields_by_name['products'].message_type = _PRODUCTAMOUNT
_PRODUCTAMOUNT.fields_by_name['product_identifier'].message_type = _PRODUCTIDENTIFIER
_PRODUCTDESCRIPTION.fields_by_name['product_identifier'].message_type = _PRODUCTIDENTIFIER
_PRODUCTMANUFACTURER.fields_by_name['product_identifier'].message_type = _PRODUCTIDENTIFIER
_PRODUCTSALECOST.fields_by_name['product_identifier'].message_type = _PRODUCTIDENTIFIER
_PRODUCTWHOLESALECOST.fields_by_name['product_identifier'].message_type = _PRODUCTIDENTIFIER
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrderID'] = _ORDERID
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['ProductIdentifier'] = _PRODUCTIDENTIFIER
DESCRIPTOR.message_types_by_name['ProductAmount'] = _PRODUCTAMOUNT
DESCRIPTOR.message_types_by_name['ProductDescription'] = _PRODUCTDESCRIPTION
DESCRIPTOR.message_types_by_name['ProductManufacturer'] = _PRODUCTMANUFACTURER
DESCRIPTOR.message_types_by_name['ProductSaleCost'] = _PRODUCTSALECOST
DESCRIPTOR.message_types_by_name['ProductWholesaleCost'] = _PRODUCTWHOLESALECOST
DESCRIPTOR.message_types_by_name['Manufacturer'] = _MANUFACTURER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:Product)
  })
_sym_db.RegisterMessage(Product)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  })
_sym_db.RegisterMessage(Order)

OrderID = _reflection.GeneratedProtocolMessageType('OrderID', (_message.Message,), {
  'DESCRIPTOR' : _ORDERID,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:OrderID)
  })
_sym_db.RegisterMessage(OrderID)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESS,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:Success)
  })
_sym_db.RegisterMessage(Success)

ProductIdentifier = _reflection.GeneratedProtocolMessageType('ProductIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTIDENTIFIER,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductIdentifier)
  })
_sym_db.RegisterMessage(ProductIdentifier)

ProductAmount = _reflection.GeneratedProtocolMessageType('ProductAmount', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTAMOUNT,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductAmount)
  })
_sym_db.RegisterMessage(ProductAmount)

ProductDescription = _reflection.GeneratedProtocolMessageType('ProductDescription', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTDESCRIPTION,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductDescription)
  })
_sym_db.RegisterMessage(ProductDescription)

ProductManufacturer = _reflection.GeneratedProtocolMessageType('ProductManufacturer', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTMANUFACTURER,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductManufacturer)
  })
_sym_db.RegisterMessage(ProductManufacturer)

ProductSaleCost = _reflection.GeneratedProtocolMessageType('ProductSaleCost', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTSALECOST,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductSaleCost)
  })
_sym_db.RegisterMessage(ProductSaleCost)

ProductWholesaleCost = _reflection.GeneratedProtocolMessageType('ProductWholesaleCost', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTWHOLESALECOST,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:ProductWholesaleCost)
  })
_sym_db.RegisterMessage(ProductWholesaleCost)

Manufacturer = _reflection.GeneratedProtocolMessageType('Manufacturer', (_message.Message,), {
  'DESCRIPTOR' : _MANUFACTURER,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:Manufacturer)
  })
_sym_db.RegisterMessage(Manufacturer)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'inventory_system_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_INVENTORYSYSTEM = _descriptor.ServiceDescriptor(
  name='InventorySystem',
  full_name='InventorySystem',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=886,
  serialized_end=1546,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetProduct',
    full_name='InventorySystem.GetProduct',
    index=0,
    containing_service=None,
    input_type=_PRODUCTIDENTIFIER,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddProduct',
    full_name='InventorySystem.AddProduct',
    index=1,
    containing_service=None,
    input_type=_PRODUCT,
    output_type=_PRODUCTIDENTIFIER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetProductsByManufacturer',
    full_name='InventorySystem.GetProductsByManufacturer',
    index=2,
    containing_service=None,
    input_type=_MANUFACTURER,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetProductsInStock',
    full_name='InventorySystem.GetProductsInStock',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PRODUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DecreaseProductAmount',
    full_name='InventorySystem.DecreaseProductAmount',
    index=4,
    containing_service=None,
    input_type=_PRODUCTAMOUNT,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IncreaseProductAmount',
    full_name='InventorySystem.IncreaseProductAmount',
    index=5,
    containing_service=None,
    input_type=_PRODUCTAMOUNT,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProductManufacturer',
    full_name='InventorySystem.UpdateProductManufacturer',
    index=6,
    containing_service=None,
    input_type=_PRODUCTMANUFACTURER,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProductDescription',
    full_name='InventorySystem.UpdateProductDescription',
    index=7,
    containing_service=None,
    input_type=_PRODUCTDESCRIPTION,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProductSaleCost',
    full_name='InventorySystem.UpdateProductSaleCost',
    index=8,
    containing_service=None,
    input_type=_PRODUCTSALECOST,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProductWholesaleCost',
    full_name='InventorySystem.UpdateProductWholesaleCost',
    index=9,
    containing_service=None,
    input_type=_PRODUCTWHOLESALECOST,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOrder',
    full_name='InventorySystem.GetOrder',
    index=10,
    containing_service=None,
    input_type=_ORDERID,
    output_type=_ORDER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddOrder',
    full_name='InventorySystem.AddOrder',
    index=11,
    containing_service=None,
    input_type=_ORDER,
    output_type=_ORDERID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateOrder',
    full_name='InventorySystem.UpdateOrder',
    index=12,
    containing_service=None,
    input_type=_ORDER,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INVENTORYSYSTEM)

DESCRIPTOR.services_by_name['InventorySystem'] = _INVENTORYSYSTEM

# @@protoc_insertion_point(module_scope)
