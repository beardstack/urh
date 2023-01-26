## cc11011signal

This is a Protocol Buffer definition file written in the proto3 syntax. It defines a package called "cc11011signal" which contains several enums and messages. The enums define different units of measurement (FrequencyUnit, BitrateUnit, PowerSetting), different modulation types (Modulation), and different encoding formats (EncodingFormat). The messages include Message, SyncWord, and Node, which contain information about the data, sync word, and node address respectively. The Signal message is the most complex and contains information about the CC1101 settings (frequency, bitrate, power, etc.) as well as settings for the message (modulation, encoding, etc.). Additionally, the Signal message has optional fields for enabling carrier sense, OOK, and CRC filtering, as well as a user comment field.

### FrequencyUnit
The FrequencyUnit enum defines different units of measurement for frequency, including hertz (HZ), kilohertz (KHZ), megahertz (MHZ), and gigahertz (GHZ). The Modulation enum defines different types of modulation, including amplitude shift keying (ASK), frequency shift keying (FSK), and phase shift keying (PSK). The BitrateUnit enum defines different units of measurement for bitrate, including bits per second (BPS), kilobits per second (KBPS), and megabits per second (MBPS). The PowerSetting enum defines different power settings, including values in decibels (DBM).

### Message
The Message message contains information about the data array and the pauses before and after the data. It has three fields: an optional beginning_pause_ms, an optional end_pause_ms, and a repeated data field. The repeated data field is an array of integers representing the data, and the length field is the length of this array in bits.

### SyncWord
The SyncWord message contains information about the sync word, which is a known sequence of bits used to synchronize the receiver and transmitter. It has three fields: a repeated data field, which is an array of integers representing the sync word, a length field, which is the length of this array in bits, and an optional maxErrBits field, which is the maximum number of bits that can be in error for the sync word to be considered valid.

### Node
The Node message contains information about the node address. It has two fields: a repeated Address field, which is an array of integers representing the node's address, and a numBroadcastAddrs field, which is the number of broadcast addresses.

### Signal
The Signal message is the main message in the package. It contains information about the CC1101 settings and the message settings. The CC1101 settings include the frequency, bitrate, deviation, and power, as well as optional fields for the RX bandwidth and the carrier sense, OOK and CRC filtering. The message settings include the modulation, encoding, and the message data. Additionally, it contains an optional field for user comment.

All in all, this Protocol Buffer definition defines a package for a communication protocol that uses a CC1101 radio module, and it provides a clear and concise way to define the different parameters and settings for the communication.


#### Example C code #1


```
#include <stdio.h>
#include <stdlib.h>
#include "cc11011.pb-c.h"

int main() {
    // Create a new Signal protobuf object
    Cc11011__Signal signal = CC11011__SIGNAL__INIT;

    // Set the signal name
    signal.name = "My Signal";

    // Set the signal frequency
    signal.freq = 433.92;
    signal.freq_unit = CC11011__FREQUENCY_UNIT__MHZ;

    // Set the signal bitrate
    signal.bitrate = 9600;
    signal.bitrate_unit = CC11011__BITRATE_UNIT__BPS;

    // Set the signal modulation
    signal.modulation = CC11011__MODULATION__MODULATION_TYPE_ASK;

    // Set the signal power
    signal.power = CC11011__POWER_SETTING__SEVEN_DBM;
    
    // Add a message to the signal
    Cc11011__Message* message = malloc(sizeof(Cc11011__Message));
    cc11011__message__init(message);
    message->length = 8;
    message->data = malloc(sizeof(int32_t) * message->length);
    message->data[0] = 0;
    message->data[1] = 1;
    message->data[2] = 0;
    message->data[3] = 1;
    message->data[4] = 0;
    message->data[5] = 1;
    message->data[6] = 0;
    message->data[7] = 1;
    signal.message = message;
    signal.n_message = 1;

    // Serialize the Signal protobuf object to a byte array
    size_t size = cc11011__signal__get_packed_size(&signal);
    uint8_t* buffer = malloc(size);
    cc11011__signal__pack(&signal, buffer);

    // Deserialize the byte array back into a Signal protobuf object
    Cc11011__Signal* deserialized = cc11011__signal__unpack(NULL, size, buffer);

    // Print the deserialized signal name
    printf("Deserialized signal name: %s\n", deserialized->name);

    // Clean up
    cc11011__signal__free_unpacked(deserialized, NULL);
    free(buffer);
    free(message->data);
    free(message);

    return 0;
}
```

#### Example C code #2

```
#include <stdio.h>
#include <stdlib.h>
#include "cc11011.pb-c.h"

int main() {
  Signal signal = SIGNAL__INIT;

  //CC1101 settings
  signal.freq = 868.35;
  signal.freq_unit = GHZ;
  signal.bitrate = 100;
  signal.bitrate_unit = KBPS;
  signal.deviation = 5.0;
  signal.rxBw = 10.0;
  signal.power = MINUS_10_DBM;

  //Message settings
  signal.modulation = MODULATION_TYPE_FSK;

  //create the message
  Message message = MESSAGE__INIT;
  message.beginning_pause_ms = 50;
  message.end_pause_ms = 100;
  int32_t data[] = {1, 0, 1, 1, 0};
  message.data = malloc(sizeof(int32_t) * 5);
  memcpy(message.data, data, sizeof(int32_t) * 5);
  message.length = 5;

  //add the message to the signal
  signal.message = &message;
  signal.n_message = 1;
  signal.encoding = ENCODING_MANCHESTER_1;

  //Extra optional fields
  signal.enable_carrier_sense = 1;
  signal.enable_ook = 1;
  signal.enable_crc_filtering = 1;
  signal.data_shaping = 2;
  
  Node node = NODE__INIT;
  int32_t addr[] = {1,2,3,4};
  node.address = malloc(sizeof(int32_t) * 4);
  memcpy(node.address, addr, sizeof(int32_t) * 4);
  node.num_broadcast_addrs = 4;
  signal.node_addr = &node;

  signal.comment = "This is a test signal";

  // Serialize the message
  size_t len = signal__get_packed_size(&signal);
  uint8_t *buf = malloc(len);
  signal__pack(&signal, buf);

  // Do something with the serialized data, e.g. send it over the network
  // ...

  // Clean up
  free(message.data);
  free(node.address);
  free(buf);

  return 0;
}

```

### Example Python code

This code creates a new Signal object, sets its properties, and creates a new Message object and sets its properties. It then serializes the Signal object to a byte string, and then deserializes it back into a new Signal object. Finally, it prints the deserialized signal.
It is important to mention that in order to use this code, you need to have the package cc11011_pb2 generated by protoc compiler.

Please note that this code is just an example and you may need to adjust it to fit your specific use case.


```
import cc11011_pb2 as cc11011

# Create a new Signal object
signal = cc11011.Signal()

# Set the name of the signal
signal.name = "Example Signal"

# Set the frequency of the signal
signal.freq = 433.92
signal.freq_unit = cc11011.FrequencyUnit.MHZ

# Set the bitrate of the signal
signal.bitrate = 9.6
signal.bitrate_unit = cc11011.BitrateUnit.KBPS

# Set the modulation of the signal
signal.modulation = cc11011.Modulation.MODULATION_TYPE_ASK

# Set the encoding of the signal
signal.encoding = cc11011.EncodingFormat.ENCODING_NRZ

# Set the power of the signal
signal.power = cc11011.PowerSetting.SEVEN_DBM

# Create a new Message object
message = cc11011.Message()

# Set the data of the message
message.data.extend([1, 0, 1, 0, 1, 0, 1, 0])

# Set the length of the message
message.length = 8

# Add the message to the signal
signal.message.extend([message])

# Serialize the signal to a byte string
signal_bytes = signal.SerializeToString()

# Deserialize the byte string to a new signal object
new_signal = cc11011.Signal()
new_signal.ParseFromString(signal_bytes)

# Print the deserialized signal
print(new_signal)

```
