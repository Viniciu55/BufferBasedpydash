# -*- coding: utf-8 -*-

from player.parser import *
from r2a.ir2a import IR2A


class R2ABufferBased(IR2A):

    def __init__(self, id):
        IR2A.__init__(self, id)
        self.parsed_mpd = ''
        self.quality = []

    def handle_xml_request(self, msg):
        self.send_down(msg)

    def handle_xml_response(self, msg):
        
        # pegando as qualidades
        self.parsed_mpd = parse_mpd(msg.get_payload())
        self.qi = self.parsed_mpd.get_qi()
        
        ###################
        self.send_up(msg)
        ###################

    def handle_segment_size_request(self, msg):
        # definir a qualidade
        print("===========================================")
        b = self.whiteboard.get_playback_buffer_size()
        Qselec = 0
        bufferlists = range(0,100,5) #seleciona a lista de qualidades 

        #verifica se existem informações de buffer, caso contrário, o buffer é =5
        if len(b)>0:
            buffer = b[-1][1]
            print(f"o buffer é: {buffer}")
        else:
            buffer = 5

        if buffer>0:
            if buffer < bufferlists[0]:
                Qselec = 0
            elif buffer < bufferlists[1]:
                Qselec = 1
            elif buffer < bufferlists[2]:
                Qselec = 2
            elif buffer <= bufferlists[3]:
                Qselec = 3
            elif buffer < bufferlists[4]:
                Qselec = 4
            elif buffer < bufferlists[5]:
                Qselec = 5
            elif buffer < bufferlists[6]:
                Qselec = 6
            elif buffer < bufferlists[7]:
                Qselec = 7
            elif buffer < bufferlists[8]:
                Qselec = 8
            elif buffer < bufferlists[9]:
                Qselec = 9
            elif buffer < bufferlists[10]:
                Qselec = 10
            elif buffer < bufferlists[11]:
                Qselec = 11
            elif buffer < bufferlists[12]:
                Qselec = 12
            elif buffer < bufferlists[13]:
                Qselec = 13
            elif buffer < bufferlists[14]:
                Qselec = 14
            elif buffer < bufferlists[15]:
                Qselec = 15
            elif buffer < bufferlists[16]:
                Qselec = 16
            elif buffer < bufferlists[17]:
                Qselec = 17
            elif buffer < bufferlists[18]:
                Qselec = 18
            elif buffer < bufferlists[19]:
                Qselec = 19
            


        #seleciona a qualidade
        msg.add_quality_id(self.qi[Qselec])
    
        ####################
        self.send_down(msg)
        ###################

    def handle_segment_size_response(self, msg):
        self.send_up(msg)

    def initialize(self):
        pass

    def finalization(self):
        pass
