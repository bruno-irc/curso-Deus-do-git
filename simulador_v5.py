def envia_lat_long_v5(latitude, longitude):

    source = '\x02'
    destination = '\x01'

    frame_id = '\x01'
    current_index = '\x01'
    total_index = '\x01'
    type = '\x01'
    subtype = '\x01'
    key_value = '\x01'

    Altitude = '\x00' + '\x00' + '\x03' + '\x20'
    End_tour_pressure = '\x0A'

    DATA = '\x03' + latitude + longitude + Altitude + '\x10' + End_tour_pressure

    g = {
        'type': 'tx',
        'frame_id': frame_id,
        'dest_addr': Controlador,
        'data': protocol.build_message(source, destination, frame_id,
                                       current_index, total_index, type, subtype, key_value, DATA)
    }

    radio.send_xbee_frame(g)