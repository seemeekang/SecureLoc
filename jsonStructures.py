class dataset:
    """Contains all the data received through MQTT that need to be stored"""
    
    def __init__(self,sample = None, protocol = '',anchorID = None, botID= None, 
                 rp = None, distance = None,timestamps = {}, 
                 rssi = None, fp_power = None, fp_ampl2 = None, std_noise = None, temperature = None):
        self.sample = sample
        self.protocol = protocol
        self.anchorID = anchorID
        self.botID = botID
        self.rp = rp # used only in the case of measurement protocol
        self.distance = distance
        self.timestamps = timestamps 
        self.rssi = rssi
        self.fp_power = fp_power
        self.std_noise = std_noise
        self.temperature = temperature
        self.fp_ampl2 = fp_ampl2
        
    def export(self):
        """returns the dataset as a dictionary"""
        
        return({"sample":self.sample, 
                "protocol":self.protocol,
                "anchorID":self.anchorID,
                "botID":self.botID,
                "distance":self.distance,
                "reference_point":self.rp,
                "timestamps":self.timestamps,
                "rssi":self.rssi,
                "fp_power":self.fp_power,
                "fp_ampl2":self.fp_ampl2,
                "std_noise":self.std_noise,
                "temperature":self.temperature})
    
    
class position:
    """Contains the data to log related to positions"""
    
    def __init__(self,bot_id = '', x = 0, y = 0, z = 0,mse = None,anchors_mse= {}):
        self.bot_id = bot_id
        self.x = x
        self.y = y
        self.z = z
        self.mse = mse
        self.anchors_mse = anchors_mse
        
    def export(self):
        """returns position as a dictionary"""
        dic = {"bot_id": self.bot_id,
                "x": self.x,
                "y":self.y,
                "z":self.z,
                "MSE":self.mse}
        for anchor in self.anchors_mse:
            key = "anchor " + anchor + " mse"
            dic[key] = self.anchors_mse[anchor]
        return(dic)
    
class metadata:
    """Contains information on the parameters used for measurements"""
    
    def __init__(self, tabfile = 'anchors.tab',comments = ''):
        self.tabfile = tabfile
        self.tabfile_content = ''
        self.comments = comments
    
    def dump_tabfile(self):
        """returns the content of anchors tabfile as a string"""
              
        with open('anchors.tab','r') as f:
            for line in f:
                self.tabfile_content = self.tabfile_content + line[:-1] + " | "
        return
     

        
    def export(self):
        """returns metadata as dictionary"""    
        self.dump_tabfile()
                      
        return({"metadata":True,
                "anchors_positions":str(self.tabfile_content)})
        



     
     