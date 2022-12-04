from namizun_core import database

from threading import Thread
from random import randint
from time import sleep
import socket


def get_random_ip():
    fragmented_random_ip = database.get_random_range_ip().split('.')
    if fragmented_random_ip[0].isdigit() and 0 < int(fragmented_random_ip[0]) < 255 and \
            fragmented_random_ip[1].isdigit() and 0 < int(fragmented_random_ip[1]) < 255 and \
            fragmented_random_ip[2].isdigit() and 0 <= int(fragmented_random_ip[2]) < 255:
        return f"{fragmented_random_ip[0]}.{fragmented_random_ip[1]}.{fragmented_random_ip[2]}.{randint(1, 255)}"
    else:
        return get_random_ip()


def start_udp_uploader(udp_upload_size, target_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while udp_upload_size >= 0:
        buf = int(randint(3000, 5000) * database.get_cache_parameter('coefficient_buffer_size'))
        if sock.sendto(bytes(buf), (target_ip, 443)):
            udp_upload_size -= buf
            sleep(0.01)
    sock.close()


def multi_udp_uploader(udp_upload_size):
    udp_thread_count = int(randint(3, 7) * database.get_cache_parameter('coefficient_uploader_threads_count'))
    threads = []
    for sender_agent in range(udp_thread_count):
        agent = Thread(target=start_udp_uploader, args=(udp_upload_size, get_random_ip()))
        agent.start()
        threads.append(agent)
    for sender_agent in threads:
        sender_agent.join()
    sleep(randint(1, 5))
    return udp_thread_count
