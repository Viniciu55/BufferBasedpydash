# -*- coding: utf-8 -*-

from statistics import mean
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

        #Selecionar a lista de buffers (ative apenas um) 
        #Valores para a função y=x*0,2
        bufferlist = range(0,100,5) #lista das possíveis qualidades em um gráfico linear

        #Valores para a função e^((x-20)/30)
        #bufferlist = [0, 20, 40, 52, 61, 68, 73, 78, 82, 85, 89, 91, 94, 96, 101, 103, 104, 106, 108, 120]
        
        #Valores para a função e^((x-18)/20)
        #bufferlist = [0, 18, 31, 39, 45, 50, 53, 56, 59, 61, 64, 65, 67, 69, 70, 72, 73, 74, 75, 76]

        #Valores para a função e^((x-5)/15)
        #bufferlist = [0, 15, 21, 25, 29, 31, 34, 36, 37, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50]

        #Valores para a função e^((x-5)/7)
        #bufferlist = [0, 5, 9, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

        #Valores para a função x*0.2 se x<10 se não x*0.9-7
        #bufferlist = [0, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]


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
