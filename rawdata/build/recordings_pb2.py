# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recordings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2 as structures__pb2
import positions_pb2 as positions__pb2
import sensors_pb2 as sensors__pb2
import locatorevents_pb2 as locatorevents__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='recordings.proto',
  package='indoors.proto',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10recordings.proto\x12\rindoors.proto\x1a\x10structures.proto\x1a\x0fpositions.proto\x1a\rsensors.proto\x1a\x13locatorevents.proto\"\xc5\x05\n\tRecording\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x08\x62uilding\x18\x02 \x02(\x03\x12\x12\n\ncreated_at\x18\x03 \x02(\x01\x12\r\n\x05start\x18\x04 \x02(\x01\x12\x0b\n\x03\x65nd\x18\x05 \x02(\x01\x12\'\n\x04meta\x18\x06 \x03(\x0b\x32\x19.indoors.proto.NamedValue\x12,\n\raccelerations\x18\x07 \x03(\x0b\x32\x15.indoors.proto.Sensor\x12$\n\x05gyros\x18\x08 \x03(\x0b\x32\x15.indoors.proto.Sensor\x12(\n\tmagnetics\x18\t \x03(\x0b\x32\x15.indoors.proto.Sensor\x12,\n\trotations\x18\n \x03(\x0b\x32\x15.indoors.proto.SensorB\x02\x18\x01\x12*\n\tpressures\x18\x0b \x03(\x0b\x32\x17.indoors.proto.Pressure\x12$\n\x06radios\x18\x0c \x03(\x0b\x32\x14.indoors.proto.Radio\x12\"\n\x05steps\x18\r \x03(\x0b\x32\x13.indoors.proto.Step\x12(\n\x08\x63ontexts\x18\x0e \x03(\x0b\x32\x16.indoors.proto.Context\x12*\n\tpositions\x18\x0f \x03(\x0b\x32\x17.indoors.proto.Position\x12\x37\n\x10global_positions\x18\x14 \x03(\x0b\x32\x1d.indoors.proto.GlobalPosition\x12\x30\n\x0corientations\x18\x15 \x03(\x0b\x32\x1a.indoors.proto.Orientation\x12\x0e\n\x06parent\x18\x16 \x01(\x03\x12\x0e\n\x06\x64\x65vice\x18\x17 \x01(\t\x12\x11\n\tuser_name\x18\x18 \x01(\t\x12+\n\x06\x65vents\x18\x19 \x03(\x0b\x32\x1b.indoors.proto.LocatorEvent'
  ,
  dependencies=[structures__pb2.DESCRIPTOR,positions__pb2.DESCRIPTOR,sensors__pb2.DESCRIPTOR,locatorevents__pb2.DESCRIPTOR,])




_RECORDING = _descriptor.Descriptor(
  name='Recording',
  full_name='indoors.proto.Recording',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='indoors.proto.Recording.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='building', full_name='indoors.proto.Recording.building', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='indoors.proto.Recording.created_at', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='indoors.proto.Recording.start', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='indoors.proto.Recording.end', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='indoors.proto.Recording.meta', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accelerations', full_name='indoors.proto.Recording.accelerations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gyros', full_name='indoors.proto.Recording.gyros', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='magnetics', full_name='indoors.proto.Recording.magnetics', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotations', full_name='indoors.proto.Recording.rotations', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pressures', full_name='indoors.proto.Recording.pressures', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radios', full_name='indoors.proto.Recording.radios', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steps', full_name='indoors.proto.Recording.steps', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contexts', full_name='indoors.proto.Recording.contexts', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='positions', full_name='indoors.proto.Recording.positions', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='global_positions', full_name='indoors.proto.Recording.global_positions', index=15,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orientations', full_name='indoors.proto.Recording.orientations', index=16,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='indoors.proto.Recording.parent', index=17,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='indoors.proto.Recording.device', index=18,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='indoors.proto.Recording.user_name', index=19,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='indoors.proto.Recording.events', index=20,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=816,
)

_RECORDING.fields_by_name['meta'].message_type = structures__pb2._NAMEDVALUE
_RECORDING.fields_by_name['accelerations'].message_type = sensors__pb2._SENSOR
_RECORDING.fields_by_name['gyros'].message_type = sensors__pb2._SENSOR
_RECORDING.fields_by_name['magnetics'].message_type = sensors__pb2._SENSOR
_RECORDING.fields_by_name['rotations'].message_type = sensors__pb2._SENSOR
_RECORDING.fields_by_name['pressures'].message_type = sensors__pb2._PRESSURE
_RECORDING.fields_by_name['radios'].message_type = sensors__pb2._RADIO
_RECORDING.fields_by_name['steps'].message_type = sensors__pb2._STEP
_RECORDING.fields_by_name['contexts'].message_type = sensors__pb2._CONTEXT
_RECORDING.fields_by_name['positions'].message_type = positions__pb2._POSITION
_RECORDING.fields_by_name['global_positions'].message_type = positions__pb2._GLOBALPOSITION
_RECORDING.fields_by_name['orientations'].message_type = sensors__pb2._ORIENTATION
_RECORDING.fields_by_name['events'].message_type = locatorevents__pb2._LOCATOREVENT
DESCRIPTOR.message_types_by_name['Recording'] = _RECORDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Recording = _reflection.GeneratedProtocolMessageType('Recording', (_message.Message,), {
  'DESCRIPTOR' : _RECORDING,
  '__module__' : 'recordings_pb2'
  # @@protoc_insertion_point(class_scope:indoors.proto.Recording)
  })
_sym_db.RegisterMessage(Recording)


_RECORDING.fields_by_name['rotations']._options = None
# @@protoc_insertion_point(module_scope)
