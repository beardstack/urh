## cc11011 Signal

This .proto file defines a Protocol Buffer message format for a "Signal" object. It specifies the fields that a Signal object can have, including various settings (frequency, bitrate, modulation type, etc.) as well as data fields (messages, node address, etc.).

The syntax of the file is "proto2", which is an older version of Protocol Buffers.

The file starts by defining several enumerations (FrequencyUnit, Modulation, BitrateUnit, PowerSetting and EncodingFormat) which are used to specify the possible values for some of the fields of the Signal message.

Then, the "Message" message is defined, it has 4 fields, beginning_pause_ms, end_pause_ms, data and length.

Then, the "SyncWord" message is defined, it has 3 fields, data, length and max_err_bits.

Then, the "Node" message is defined, it has 2 fields, addresses and num_broadcast_addrs.

Finally, the "Signal" message is defined. It has 17 fields, name, freq, freq_unit, bitrate, bitrate_unit, deviation, rx_bw, power, modulation, messages, encoding, enable_carrier_sense, enable_ook, enable_crc_filtering, data_shaping, node_address and comment. Most of the fields are optional, and have default values specified.

This .proto file is used to generate code in the desired language (e.g. python) for serializing and deserializing instances of the Signal message. Once the code is generated, the Signal message can be used to create, read, and write Signal objects in a language- and platform-independent way.


## Enumerated types (enums):

### FrequencyUnit: 
This enumerated type contains values for specifying the unit of frequency. Possible values are: FREQUENCY_UNIT_UNSPECIFIED, FREQUENCY_UNIT_HZ, FREQUENCY_UNIT_KHZ, FREQUENCY_UNIT_MHZ, FREQUENCY_UNIT_GHZ.

### Modulation: 
This enumerated type contains values for specifying the modulation type. Possible values are: MODULATION_TYPE_UNSPECIFIED, MODULATION_TYPE_ASK, MODULATION_TYPE_FSK, MODULATION_TYPE_PSK.

### BitrateUnit: 
This enumerated type contains values for specifying the unit of bitrate. Possible values are: BITRATE_UNIT_UNSPECIFIED, BITRATE_UNIT_BPS, BITRATE_UNIT_KBPS, BITRATE_UNIT_MBPS.

### PowerSetting: 
This enumerated type contains values for specifying the power setting. Possible values are: POWER_SETTING_UNSPECIFIED, POWER_SETTING_MINUS_30_DBM, POWER_SETTING_MINUS_20_DBM, POWER_SETTING_MINUS_15_DBM, POWER_SETTING_MINUS_10_DBM, POWER_SETTING_ZERO_DBM, POWER_SETTING_FIVE_DBM, POWER_SETTING_SEVEN_DBM, POWER_SETTING_TEN_DBM.

### EncodingFormat: 
This enumerated type contains values for specifying the encoding format. Possible values are: ENCODING_FORMAT_UNSPECIFIED, ENCODING_FORMAT_NRZ, ENCODING_FORMAT_NRZ_INVERT, ENCODING_FORMAT_MANCHESTER_1, ENCODING_FORMAT_MANCHESTER_2, ENCODING_FORMAT_DIFF_MANCHESTER, ENCODING_FORMAT_WHITENING.


## Message types:

### Message: 

This message type contains fields for specifying a data message and its properties. It has the following fields:

* eginning_pause_ms: An optional field that specifies the beginning pause in milliseconds. The default value is 0.
* end_pause_ms: An optional field that specifies the end pause in milliseconds. The default value is 0.
* data: A repeated field that contains the data.
* length: A required field that specifies the length of the bit array. The default value is 0.

### SyncWord: 
* This message type contains fields for specifying the SyncWord and its properties. It has the following fields:

data: A repeated field that contains the data.
length: A required field that specifies the length of the SyncWord.
max_err_bits: An optional field that specifies the maximum number of error bits allowe

### Node

The Node message in the provided code is used to specify information about the destination of the signal being transmitted. It has the following fields:

* repeated int32 addresses: This field can contain multiple destination addresses, represented as integers.
* required int32 num_broadcast_addrs: This field is used to specify the number of broadcast addresses. A broadcast address is an address that allows the message to be received by all devices on a network. This field is set to 0 by default.

The repeated keyword in the addresses field indicates that this field can hold multiple values, while the required keyword in the num_broadcast_addrs field indicates that this field must always have a value.

### Signal

The Signal message in the provided code is a Protocol Buffer message that describes a radio signal. It contains various fields that can be used to specify the characteristics of the signal, such as the frequency and modulation type.

Here is a breakdown of the fields in the Signal message:

#### name (required, string) : 
A label for the signal. Default is "default_signal"
#### freq (required, float) : 
The frequency of the signal. Default is 433.92
#### freq_unit (required, FrequencyUnit) : 
The unit of the frequency. Can be one of the following:

        FREQUENCY_UNIT_UNSPECIFIED
        FREQUENCY_UNIT_HZ
        FREQUENCY_UNIT_KHZ
        FREQUENCY_UNIT_MHZ
        FREQUENCY_UNIT_GHZ
#### bitrate (required, float) : 
The bitrate of the signal. Default is 600
#### bitrate_unit (required, BitrateUnit) : 
The unit of the bitrate. Can be one of the following:

        BITRATE_UNIT_UNSPECIFIED
        BITRATE_UNIT_BPS
        BITRATE_UNIT_KBPS
        BITRATE_UNIT_MBPS
#### deviation (optional, float) : 
The deviation of the signal.
#### rx_bw (optional, float) : 
The receiver bandwidth of the signal.
#### power (optional, PowerSetting) : 
The power setting of the signal. Can be one of the following:

        POWER_SETTING_UNSPECIFIED
        POWER_SETTING_MINUS_30_DBM
        POWER_SETTING_MINUS_20_DBM
        POWER_SETTING_MINUS_15_DBM
        POWER_SETTING_MINUS_10_DBM
        POWER_SETTING_ZERO_DBM
        POWER_SETTING_FIVE_DBM
        POWER_SETTING_SEVEN_DBM
        POWER_SETTING_TEN_DBM
#### modulation (optional, Modulation) : The modulation type of the signal. Can be one of the following:
        MODULATION_TYPE_UNSPECIFIED
        MODULATION_TYPE_ASK
        MODULATION_TYPE_FSK
        MODULATION_TYPE_PSK
#### messages (repeated): This field contains an array of Message objects, which define the data and settings for the signal. Each Message object has the following fields:

* beginning_pause_ms (optional, default is 0): This field defines the number of milliseconds of pause before the data transmission.
* end_pause_ms (optional, default is 0): This field defines the number of milliseconds of pause after the data transmission.
* data (repeated): This field contains the data of the message as an array of integers
* length (required): This field defines the length of the data array in bits
* encoding (optional, default is ENCODING_FORMAT_NRZ): This field defines the encoding format used for the signal. It is an enumerated field with the options of ENCODING_FORMAT_UNSPECIFIED, ENCODING_FORMAT_NRZ, ENCODING_FORMAT_NRZ_INVERT, ENCODING_FORMAT_MANCHESTER_1, ENCODING_FORMAT_MANCHESTER_2, ENCODING_FORMAT_DIFF_MANCHESTER and ENCODING_FORMAT_WHITENING.
* enable_carrier_sense (optional, default is false): This field enables or disables carrier sense filtering.
* enable_ook (optional, default is false): This field enables or disables OOK modulation.
* enable_crc_filtering (optional, default is false): This field enables or disables crc filtering.
* data_shaping (optional): The purpose of this field is not specified in the code provided
* node_address (optional): This field contains the node address information as a Node message, which includes an array of addresses and the number of broadcast addresses.
* comment (optional): This field is a user-defined comment field.


#### encoding(optional)
Enumerated type called EncodingFormat. This field represents the encoding format used for the signal. The default value for this field is ENCODING_FORMAT_NRZ, which stands for "Non-Return-to-Zero". Other possible values for this field include: 

    ENCODING_FORMAT_NRZ_INVERT: Non-Return-to-Zero Inverted
    ENCODING_FORMAT_MANCHESTER_1: Manchester 1
    ENCODING_FORMAT_MANCHESTER_2: Manchester 2
    ENCODING_FORMAT_DIFF_MANCHESTER: Differential Manchester
    ENCODING_FORMAT_WHITENING: Whitening

These values correspond to different types of line coding used for digital signals. NRZ is a basic type of line coding in which the signal is a constant amplitude for a logic 1 and a logic 0 is represented by no signal. Manchester coding is a type of line coding that uses a transition in the middle of a bit time to indicate a logic 1 or 0, this can improve signal integrity. Differential Manchester coding is a variation of Manchester coding in which the signal transition is made at the beginning of the bit time and the signal level is different for logic 1 or 0. Whitening is a technique used to randomize a signal, this can be useful in some wireless communications to avoid long runs of zeroes or ones.


Example C++ code #1
```
#include <iostream>
#include "cc11011.pb.h"

int main() {
    cc11011::Signal signal;

    // Fill in required fields
    signal.set_name("Example Signal");
    signal.set_freq(433.92);
    signal.set_freq_unit(cc11011::FrequencyUnit::FREQUENCY_UNIT_MHZ);
    signal.set_bitrate(600);
    signal.set_bitrate_unit(cc11011::BitrateUnit::BITRATE_UNIT_KBPS);

    // Fill in optional fields
    signal.set_power(cc11011::PowerSetting::POWER_SETTING_SEVEN_DBM);
    signal.set_enable_ook(true);
    signal.set_enable_crc_filtering(true);
    signal.set_data_shaping(10);
    signal.set_comment("This is an example signal");

    // Create a new message and add it to the signal
    cc11011::Message* message = signal.add_messages();
    message->set_beginning_pause_ms(100);
    message->set_end_pause_ms(200);
    message->set_length(8);
    message->add_data(1);
    message->add_data(0);
    message->add_data(1);
    message->add_data(0);
    message->add_data(1);
    message->add_data(0);
    message->add_data(1);
    message->add_data(0);

    // serialize the message to a string
    std::string serialized;
    signal.SerializeToString(&serialized);

    //print serialized data
    std::cout << "Serialized data: " << serialized << std::endl;
    return 0;
}
```


