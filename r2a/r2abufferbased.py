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
        print("==========================================")
        b = self.whiteboard.get_playback_buffer_size()
        Qselec = 0
        bufferlist = range(0,100,5) #lista de qualidades possíveis

        #verifica se existem informações de buffer, caso contrário, o buffer é =5
        if len(b)>0:
            buffer = b[-1][1]
            print(f"o buffer é: {buffer}")
        else:
            buffer = 5

        #verifica o tamanho do buffer atual e seta a qualidade a partir disso
        if buffer>0:
            if buffer < bufferlist[0]:
                Qselec = 0
            elif buffer < bufferlist[1]:
                Qselec = 1
            elif buffer < bufferlist[2]:
                Qselec = 2
            elif buffer <= bufferlist[3]:
                Qselec = 3
            elif buffer < bufferlist[4]:
                Qselec = 4
            elif buffer < bufferlist[5]:
                Qselec = 5
            elif buffer < bufferlist[6]:
                Qselec = 6
            elif buffer < bufferlist[7]:
                Qselec = 7
            elif buffer < bufferlist[8]:
                Qselec = 8
            elif buffer < bufferlist[9]:
                Qselec = 9
            elif buffer < bufferlist[10]:
                Qselec = 10
            elif buffer < bufferlist[11]:
                Qselec = 11
            elif buffer < bufferlist[12]:
                Qselec = 12
            elif buffer < bufferlist[13]:
                Qselec = 13
            elif buffer < bufferlist[14]:
                Qselec = 14
            elif buffer < bufferlist[15]:
                Qselec = 15
            elif buffer < bufferlist[16]:
                Qselec = 16
            elif buffer < bufferlist[17]:
                Qselec = 17
            elif buffer < bufferlist[18]:
                Qselec = 18
            elif buffer < bufferlist[19]:
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
