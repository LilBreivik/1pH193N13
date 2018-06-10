import logging, os, sys
 
config = dict(

    PATH = '/BacklogFILES',
    BACKLOGPATH =  '/BacklogFILES',
    BACKLOGFILE = 'backlog.log',
    BACKLOGFILEPOSTFIX = '/backlog.log'

)

class BacklogManager:


    @staticmethod
    def initLogger():

       logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='/Users/dustin/git/Seminararbeit/1pH193N13/BacklogFILES/backlog.log', filemode='w')
         
       
       ch = logging.StreamHandler(sys.stdout)
       ch.setLevel(logging.DEBUG)
       formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
       ch.setFormatter(formatter)
       logging.getLogger().addHandler(ch)

    @staticmethod
    def createBacklog():

        
        BacklogPath = os.getcwd() 
        BacklogPath +=  config['PATH']

         
        
     

    
    @staticmethod
    def writeToBacklog(message):
   
        
        
        logging.debug(message)

        
