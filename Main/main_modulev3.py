# What makes this function unique is that I have changed two things, the scoring weights and the time modifier. Since
# this function is supposed to look at historical data and prioritize aggressive IPs, I have put more importance
# on the the daily averages over the total stats. This way, IPs that have been super active consistently will grow
# faster than ones who have been active for only a day. I have also altered the time modifier so that instead of using
# the first time seen, it uses the last time the IP is seen. That way, if an IP is consistent every day, its score will
# not decrease, while IPs that are active for only a day will decrease faster.
import math


def prioritize_consistent_original_6(list_of_flows, time_of_newest_data_file):

        # These values will define which of the four metrics are the most important
        total_event_weight = 0.20
        average_event_weight = 0.10
        total_duration_weight = 0.10
        average_duration_weight = 0.10
        total_byte_weight = 0.20
        byte_average_weight = 0.10
        total_packets_weight = 0.10
        average_packet_weight = 0.10

        # The actual rating section
        list_of_raw_ratings = []
        for flow in list_of_flows:
            # Convert all strings to float
            events = float(flow[1])
            duration = float(flow[2])
            average_duration = float(flow[3])
            bytes = float(flow[4])
            average_bytes = float(flow[5])
            packets = float(flow[6])
            average_packets = float(flow[7])
            last_event = float(flow[9])
            average_events = float(flow[10])

            # Calculate the scores
            event_score = (events * total_event_weight)
            average_events_score = (average_events * average_event_weight)
            duration_score = (duration * total_duration_weight)
            average_duration_score = (average_duration * average_duration_weight)
            bytes_score = (bytes * total_byte_weight)
            average_bytes_score = (average_bytes * byte_average_weight)
            packets_score = (packets * total_packets_weight)
            average_packets_score = (average_packets * average_packet_weight)

            # This is the time modifier section. The longer an IP does not have any events, the lower its score will
            # be. An IP will lose .01 of its score per day that it is not active, thus taking 100 days to be reduced
            # to a score of zero.
            if (time_of_newest_data_file - last_event) < 86400:
                time_modifier = 1
            else:
                time_modifier_factor = (time_of_newest_data_file - last_event) // 86400
                # I am using the general function y = x/(x + 10), where x is the number of days an IP is not seen.
                # In this way, the amount by which a score will decrease will increase to about 50% in about 30 days,
                # and will infinities approach 100% after that.
                time_modifier = 6/(time_modifier_factor+6)
            total_score = math.sqrt((event_score + average_events_score + duration_score + average_duration_score
                                     + bytes_score + average_bytes_score + packets_score + average_packets_score) * time_modifier)
            list_of_raw_ratings.append([flow[0], total_score])
        return list_of_raw_ratings


def todays_ips_only(list_of_flows, time):
    # These values will define which of the four metrics are the most important
    total_event_weight = 0.20
    average_event_weight = 0.10
    total_duration_weight = 0.10
    average_duration_weight = 0.10
    total_byte_weight = 0.20
    byte_average_weight = 0.10
    total_packets_weight = 0.10
    average_packet_weight = 0.10

    # The actual rating section
    list_of_raw_ratings = []
    for flow in list_of_flows:
        # Convert all strings to float
        events = float(flow[1])
        duration = float(flow[2])
        average_duration = float(flow[3])
        bytes = float(flow[4])
        average_bytes = float(flow[5])
        packets = float(flow[6])
        average_packets = float(flow[7])
        average_events = float(flow[1])

        # Calculate the scores
        event_score = (events * total_event_weight)
        average_events_score = (average_events * average_event_weight)
        duration_score = (duration * total_duration_weight)
        average_duration_score = (average_duration * average_duration_weight)
        bytes_score = (bytes * total_byte_weight)
        average_bytes_score = (average_bytes * byte_average_weight)
        packets_score = (packets * total_packets_weight)
        average_packets_score = (average_packets * average_packet_weight)

        total_score = math.sqrt(event_score + average_events_score + duration_score + average_duration_score
                                + bytes_score + average_bytes_score + packets_score + average_packets_score)

        list_of_raw_ratings.append([flow[0], total_score])
    return list_of_raw_ratings


def prioritize_new_original_6(list_of_flows, time_of_newest_data_file):

        # These values will define which of the four metrics are the most important
        total_event_weight = 0.20
        average_event_weight = 0.10
        total_duration_weight = 0.10
        average_duration_weight = 0.10
        total_byte_weight = 0.20
        byte_average_weight = 0.10
        total_packets_weight = 0.10
        average_packet_weight = 0.10

        # The actual rating section
        list_of_raw_ratings = []
        for flow in list_of_flows:
            # Convert all strings to float
            events = float(flow[1])
            duration = float(flow[2])
            average_duration = float(flow[3])
            bytes = float(flow[4])
            average_bytes = float(flow[5])
            packets = float(flow[6])
            average_packets = float(flow[7])
            first_event = float(flow[8])
            last_event = float(flow[9])
            average_events = float(flow[10])

            # Calculate the scores
            event_score = (events * total_event_weight)
            average_events_score = (average_events * average_event_weight)
            duration_score = (duration * total_duration_weight)
            average_duration_score = (average_duration * average_duration_weight)
            bytes_score = (bytes * total_byte_weight)
            average_bytes_score = (average_bytes * byte_average_weight)
            packets_score = (packets * total_packets_weight)
            average_packets_score = (average_packets * average_packet_weight)

            # This is the time modifier section. The longer an IP does not have any events, the lower its score will
            # be. An IP will lose .01 of its score per day that it is not active, thus taking 100 days to be reduced
            # to a score of zero.
            if (time_of_newest_data_file - last_event) < 86400:
                time_modifier = 1
            else:
                time_modifier_factor = (time_of_newest_data_file - last_event) // 86400
                # I am using the general function y = x/(x + 10), where x is the number of days an IP is not seen.
                # In this way, the amount by which a score will decrease will increase to about 50% in about 30 days,
                # and will infinities approach 100% after that.
                time_modifier = 6 / (time_modifier_factor + 6)
            total_score = math.sqrt((event_score + average_events_score + duration_score + average_duration_score
                                     + bytes_score + average_bytes_score + packets_score + average_packets_score) * time_modifier)
            list_of_raw_ratings.append([flow[0], total_score])
        return list_of_raw_ratings


def prioritize_consistent_normalized_6(list_of_flows, time_of_newest_data_file):
    # These values will define which of the four metrics are the most important
    total_event_weight = 0.20
    average_event_weight = 0.10
    total_duration_weight = 0.10
    average_duration_weight = 0.10
    total_byte_weight = 0.20
    byte_average_weight = 0.10
    total_packets_weight = 0.10
    average_packet_weight = 0.10

    # Create a list of each data type in order to compare them all when normalizing the scores
    list_of_event_values_for_normalization = []
    list_of_duration_values_for_normalization = []
    list_of_av_duration_values_for_normalization = []
    list_of_byte_values_for_normalization = []
    list_of_av_byte_values_for_normalization = []
    list_of_packet_values_for_normalization = []
    list_of_av_packet_values_for_normalization = []
    list_of_av_event_values_for_normalization = []

    # List of Mins and Max's each of the data types.
    min_event = 100
    max_event = 0
    min_dur = 100
    max_dur = 0
    min_av_dur = 100
    max_av_dur = 0
    min_byte = 100
    max_byte = 0
    min_av_byte = 100
    max_av_byte = 0
    min_packet = 100
    max_packet = 0
    min_av_packet = 100
    max_av_packet = 0
    min_av_event = 100
    max_av_event = 0

    for flow in list_of_flows:
        list_of_event_values_for_normalization.append(float(flow[1]))
        if float(flow[1]) > max_event:
            max_event = float(flow[1])
        if float(flow[1]) < min_event:
            min_event = float(flow[1])
        list_of_duration_values_for_normalization.append(float(flow[2]))
        if float(flow[2]) > max_dur:
            max_dur = float(flow[2])
        if float(flow[2]) < min_dur:
            min_dur = float(flow[2])
        list_of_av_duration_values_for_normalization.append(float(flow[3]))
        if float(flow[3]) > max_av_dur:
            max_av_dur = float(flow[3])
        if float(flow[3]) < min_av_dur:
            min_av_dur = float(flow[3])
        list_of_byte_values_for_normalization.append(float(flow[4]))
        if float(flow[4]) > max_byte:
            max_byte = float(flow[4])
        if float(flow[4]) < min_byte:
            min_byte = float(flow[4])
        list_of_av_byte_values_for_normalization.append(float(flow[5]))
        if float(flow[5]) > max_av_byte:
            max_av_byte = float(flow[5])
        if float(flow[5]) < min_av_byte:
            min_av_byte = float(flow[5])
        list_of_packet_values_for_normalization.append(float(flow[6]))
        if float(flow[6]) > max_packet:
            max_packet = float(flow[6])
        if float(flow[6]) < min_packet:
            min_packet = float(flow[6])
        list_of_av_packet_values_for_normalization.append(float(flow[7]))
        if float(flow[7]) > max_av_packet:
            max_av_packet = float(flow[7])
        if float(flow[7]) < min_av_packet:
            min_av_packet = float(flow[7])
        list_of_av_event_values_for_normalization.append(float(flow[10]))
        if float(flow[10]) > max_av_event:
            max_av_event = float(flow[10])
        if float(flow[10]) < min_av_event:
            min_av_event = float(flow[10])

    print(min(list_of_event_values_for_normalization))
    print(max(list_of_event_values_for_normalization))
    print(min_event)
    print(max_event)
    # The actual rating section
    list_of_raw_ratings = []
    for flow in list_of_flows:
        # Convert all strings to float
        events = float(flow[1])
        duration = float(flow[2])
        average_duration = float(flow[3])
        bytes = float(flow[4])
        average_bytes = float(flow[5])
        packets = float(flow[6])
        average_packets = float(flow[7])
        last_event = float(flow[9])
        average_events = float(flow[10])

        # Calculate the scores
        event_score = (((events - min_event) / (max_event - min_event)) * total_event_weight)
        average_events_score = (
                    ((average_events - min_av_event) / (max_av_event - min_av_event)) * average_event_weight)
        duration_score = ((duration - min_dur) / (max_dur - min_dur)) * total_duration_weight
        average_duration_score = (
                    ((average_duration - min_av_dur) / (max_av_dur - min_av_dur)) * average_duration_weight)
        bytes_score = (((bytes - min_byte) / (max_byte - min_byte)) * total_byte_weight)
        average_bytes_score = (((average_bytes - min_av_byte) / (max_av_byte - min_av_byte)) * byte_average_weight)
        packets_score = (((packets - min_packet) / (max_packet - min_packet)) * total_packets_weight)
        average_packets_score = (
                    ((average_packets - min_av_packet) / (max_av_packet - min_av_packet)) * average_packet_weight)

        # This is the time modifier section. The longer an IP does not have any events, the lower its score will
        # be. An IP will lose .01 of its score per day that it is not active, thus taking 100 days to be reduced
        # to a score of zero.
        if (time_of_newest_data_file - last_event) < 86400:
            time_modifier = 1
        else:
            time_modifier_factor = (time_of_newest_data_file - last_event) // 86400
            # I am using the general function y = x/(x + 10), where x is the number of days an IP is not seen.
            # In this way, the amount by which a score will decrease will increase to about 50% in about 30 days,
            # and will infinities approach 100% after that.
            time_modifier = 6 / (time_modifier_factor + 6)
        total_score = math.sqrt((event_score + average_events_score + duration_score + average_duration_score
                                 + bytes_score + average_bytes_score + packets_score + average_packets_score) * time_modifier)
        list_of_raw_ratings.append([flow[0], total_score])
    return list_of_raw_ratings


