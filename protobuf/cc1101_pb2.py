# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cc1101.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x63\x31\x31\x30\x31.proto\x12\x07\x63\x63\x31\x31\x30\x31\x31\"b\n\x07Message\x12\x1d\n\x12\x62\x65ginning_pause_ms\x18\x01 \x01(\x05:\x01\x30\x12\x17\n\x0c\x65nd_pause_ms\x18\x02 \x01(\x05:\x01\x30\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x05\x12\x11\n\x06length\x18\x04 \x02(\x05:\x01\x30\">\n\x08SyncWord\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x05\x12\x0e\n\x06length\x18\x02 \x02(\x05\x12\x14\n\x0cmax_err_bits\x18\x03 \x01(\x05\"9\n\x04Node\x12\x11\n\taddresses\x18\x01 \x03(\x05\x12\x1e\n\x13num_broadcast_addrs\x18\x02 \x02(\x05:\x01\x30\"\xef\x04\n\x06Signal\x12\x1c\n\x04name\x18\x01 \x02(\t:\x0e\x64\x65\x66\x61ult_signal\x12\x14\n\x04\x66req\x18\x02 \x02(\x02:\x06\x34\x33\x33.92\x12=\n\tfreq_unit\x18\x03 \x02(\x0e\x32\x16.cc11011.FrequencyUnit:\x12\x46REQUENCY_UNIT_MHZ\x12\x14\n\x07\x62itrate\x18\x04 \x02(\x02:\x03\x36\x30\x30\x12=\n\x0c\x62itrate_unit\x18\x05 \x02(\x0e\x32\x14.cc11011.BitrateUnit:\x11\x42ITRATE_UNIT_KBPS\x12\x11\n\tdeviation\x18\x06 \x01(\x02\x12\r\n\x05rx_bw\x18\x07 \x01(\x02\x12=\n\x05power\x18\x08 \x01(\x0e\x32\x15.cc11011.PowerSetting:\x17POWER_SETTING_SEVEN_DBM\x12<\n\nmodulation\x18\t \x01(\x0e\x32\x13.cc11011.Modulation:\x13MODULATION_TYPE_ASK\x12\"\n\x08messages\x18\n \x03(\x0b\x32\x10.cc11011.Message\x12>\n\x08\x65ncoding\x18\x0b \x01(\x0e\x32\x17.cc11011.EncodingFormat:\x13\x45NCODING_FORMAT_NRZ\x12\x1c\n\x14\x65nable_carrier_sense\x18\x0c \x01(\x08\x12\x12\n\nenable_ook\x18\r \x01(\x08\x12\x1c\n\x14\x65nable_crc_filtering\x18\x0e \x01(\x08\x12\x14\n\x0c\x64\x61ta_shaping\x18\x0f \x01(\x05\x12#\n\x0cnode_address\x18\x10 \x01(\x0b\x32\r.cc11011.Node\x12\x0f\n\x07\x63omment\x18\x11 \x01(\t*\x8e\x01\n\rFrequencyUnit\x12\x1e\n\x1a\x46REQUENCY_UNIT_UNSPECIFIED\x10\x00\x12\x15\n\x11\x46REQUENCY_UNIT_HZ\x10\x01\x12\x16\n\x12\x46REQUENCY_UNIT_KHZ\x10\x02\x12\x16\n\x12\x46REQUENCY_UNIT_MHZ\x10\x03\x12\x16\n\x12\x46REQUENCY_UNIT_GHZ\x10\x04*x\n\nModulation\x12\x1f\n\x1bMODULATION_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13MODULATION_TYPE_ASK\x10\x01\x12\x17\n\x13MODULATION_TYPE_FSK\x10\x02\x12\x17\n\x13MODULATION_TYPE_PSK\x10\x03*o\n\x0b\x42itrateUnit\x12\x1c\n\x18\x42ITRATE_UNIT_UNSPECIFIED\x10\x00\x12\x14\n\x10\x42ITRATE_UNIT_BPS\x10\x01\x12\x15\n\x11\x42ITRATE_UNIT_KBPS\x10\x02\x12\x15\n\x11\x42ITRATE_UNIT_MBPS\x10\x03*\x9d\x02\n\x0cPowerSetting\x12\x1d\n\x19POWER_SETTING_UNSPECIFIED\x10\x00\x12\x1e\n\x1aPOWER_SETTING_MINUS_30_DBM\x10\x01\x12\x1e\n\x1aPOWER_SETTING_MINUS_20_DBM\x10\x02\x12\x1e\n\x1aPOWER_SETTING_MINUS_15_DBM\x10\x03\x12\x1e\n\x1aPOWER_SETTING_MINUS_10_DBM\x10\x04\x12\x1a\n\x16POWER_SETTING_ZERO_DBM\x10\x05\x12\x1a\n\x16POWER_SETTING_FIVE_DBM\x10\x06\x12\x1b\n\x17POWER_SETTING_SEVEN_DBM\x10\x07\x12\x19\n\x15POWER_SETTING_TEN_DBM\x10\x08*\xf2\x01\n\x0e\x45ncodingFormat\x12\x1f\n\x1b\x45NCODING_FORMAT_UNSPECIFIED\x10\x00\x12\x17\n\x13\x45NCODING_FORMAT_NRZ\x10\x01\x12\x1e\n\x1a\x45NCODING_FORMAT_NRZ_INVERT\x10\x02\x12 \n\x1c\x45NCODING_FORMAT_MANCHESTER_1\x10\x03\x12 \n\x1c\x45NCODING_FORMAT_MANCHESTER_2\x10\x04\x12#\n\x1f\x45NCODING_FORMAT_DIFF_MANCHESTER\x10\x05\x12\x1d\n\x19\x45NCODING_FORMAT_WHITENING\x10\x06')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cc1101_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FREQUENCYUNIT._serialized_start=875
  _FREQUENCYUNIT._serialized_end=1017
  _MODULATION._serialized_start=1019
  _MODULATION._serialized_end=1139
  _BITRATEUNIT._serialized_start=1141
  _BITRATEUNIT._serialized_end=1252
  _POWERSETTING._serialized_start=1255
  _POWERSETTING._serialized_end=1540
  _ENCODINGFORMAT._serialized_start=1543
  _ENCODINGFORMAT._serialized_end=1785
  _MESSAGE._serialized_start=25
  _MESSAGE._serialized_end=123
  _SYNCWORD._serialized_start=125
  _SYNCWORD._serialized_end=187
  _NODE._serialized_start=189
  _NODE._serialized_end=246
  _SIGNAL._serialized_start=249
  _SIGNAL._serialized_end=872
# @@protoc_insertion_point(module_scope)
