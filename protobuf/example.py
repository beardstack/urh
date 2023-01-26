import cc11011_pb2

signal = cc11011_pb2.Signal()

# required fields
signal.name = "example_signal"
signal.freq = 433.92
signal.freq_unit = cc11011_pb2.FrequencyUnit.FREQUENCY_UNIT_MHZ
signal.bitrate = 600
signal.bitrate_unit = cc11011_pb2.BitrateUnit.BITRATE_UNIT_KBPS

# optional fields
signal.deviation = 500.0
signal.rx_bw = 10.0
signal.power = cc11011_pb2.PowerSetting.POWER_SETTING_TEN_DBM
signal.modulation = cc11011_pb2.Modulation.MODULATION_TYPE_PSK

message = signal.messages.add()
message.beginning_pause_ms = 100
message.end_pause_ms = 200
message.data.extend([1, 0, 1, 0, 1])
message.length = 5

signal.encoding = cc11011_pb2.EncodingFormat.ENCODING_FORMAT_MANCHESTER_1
signal.enable_carrier_sense = True
signal.enable_ook = False
signal.enable_crc_filtering = True
signal.data_shaping = 3

node = signal.node_address
node.addresses.extend([1, 2, 3])
node.num_broadcast_addrs = 2

signal.comment = "example comment"
