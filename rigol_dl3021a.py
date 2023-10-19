class rigol_dl3021a():

	def __init__(self, pyvisa_instr):
		self.dl3021a = pyvisa_instr # this is the pyvisa instrument, rm.open_resource('USB0::0x0466::0x2860::04074562::INSTR')


	def get_all_scpi_list(self):
        result_list = []
        for command in self.scpi_cmd_dict:
#			print(str(command) + "\n")
			result = (self.dl3021a.query(command.format("?"))).rstrip('\r\n')
			result = " " + result
			result_list.append(command.format(result))
        return result_list


	def get_unique_scpi_list(self):
        unique_scpi_list = []
        inst_settings_list = self.get_all_scpi_list()
        for setting in inst_settings_list:
            if (setting not in self.settings_por_scpi_list):
                unique_scpi_list.append(setting)
        return unique_scpi_list
        

	scpi_cmd_dict = { "TRIGger:SOURce{0}"                     : "trigger source that you set for the instrument {BUS|EXTernal|MANUal}",
				      "SOURce:INPut:STATe{0}"                 : "input of the electronic load to be on or off {0|1|ON|OFF}", 
				      "SOURce:FUNCtion{0}"                    : "static operation mode of the electronic load {CURRent|RESistance|VOLTage|POWer}", 
				      ":SOURce:FUNCtion:MODE{0}"              : "input regulation mode setting  {FIXed|LIST|WAVe|BATTery|OCP|OPP}", 
				      "SOURce:TRANsient{0}"                   : "trigger function to be on or off {0|1|ON|OFF}", 
				      ":SOURce:CURRent:LEVel:IMMediate{0}"    : "load regulated current in CC mode {<value>|MINimum|MAXimum|DEFault}", 
				      "SOURce:CURRent:RANGe{0}"               : "current range set in CC mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:SLEW{0}"                : "rising and falling slew rate in CC mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:SLEW:POSitive{0}"       : "rising rate in transient operation mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:SLEW:NEGative{0}"       : "falling rate set in transient operation mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:VON{0}"                 : "starting voltage in CC mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:VLIMt{0}"               : "voltage limit in CC mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:ILIMt{0}"               : "current limit in CC mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:MODE{0}"      : "transient operation mode in CC mode {CONTinuous|PULSe|TOGGle}",
				      "SOURce:CURRent:TRANsient:ALEVel{0}"    : "Level A in transient operation mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:BLEVel{0}"    : "Level B in transient operation mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:AWIDth{0}"    : "width of Level A in continuous and pulsed transient operation {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:BWIDth{0}"    : "width of Level B in continuous and pulsed transient operation {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:FREQuency{0}" : "frequency in continuous mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:PERiod{0}"    : "period in continuous mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:CURRent:TRANsient:ADUTy{0}"     : "duty cycle in continuous mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:VOLTage:LEVel:IMMediate{0}"     : "load voltage in CV mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:VOLTage:RANGe{0}"               : "voltage range in CV mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:VOLTage:VLIMt{0}"               : "voltage limit in CV mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:VOLTage:ILIMt{0}"               : "current limit in CV mode {<value>|MINimum|MAXimum|DEFault}",
				      ":SOURce:RESistance:LEVel:IMMediate{0}" : "load resistance in CR mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:RESistance:RANGe{0}"            : "resistance range in CR mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:RESistance:VLIMt{0}"            : "voltage limit in CR mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:RESistance:ILIMt{0}"            : "current limit in CR mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:POWer:LEVel:IMMediate{0}"       : "load power in CP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:POWer:VLIMt{0}"                 : "voltage limit set in CP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:POWer:ILIMt{0}"                 : "current limit in CP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:LIST:MODE{0}"                   : "running mode of the load in List operation {CC|CV|CR|CP}",
				      "SOURce:LIST:RANGe{0}"                  : "range for each running mode in List operation <value>",
				      "SOURce:LIST:COUNt{0}"                  : "number of times the list is cycled {<value>|MINimum|MAXimum}",
				      "SOURce:LIST:STEP{0}"                   : "number of steps executed in each cycle {<value>|MINimum|MAXimum}",
				      "SOURce:LIST:LEVel{0}"                  : "input value for each step <step>",
				      "SOURce:LIST:WIDth{0}"                  : "width for each step <step>",
				      "SOURce:LIST:SLEW{0}"                   : "slew rate for CC mode in List operation <step>",
				      "SOURce:LIST:END{0}"                    : "end state when input is completed in list operation {LAST|OFF}",
				      "SOURce:BATTary:RANGe{0}"               : "current range in Battery mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:BATTary:LEVel:IMMediate{0}"     : "load regulation current in Battery mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:BATTary:VSTop{0}"               : "voltage at which the battery stops discharging in Battery mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:BATTary:CSTop{0}"               : "battery capacity at which the battery stops discharging in Battery mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:BATTary:TIMestop{0}"            : "discharge cutoff time at which the battery stops discharging in Battery mode {<value>}",
				      "SOURce:BATTary:VON{0}"                 : "starting voltage in Battery mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:BATTary:VENabstop{0}"           : "cut-off voltage switch of the electronic load {0|1|ON|OFF}",
				      "SOURce:BATTary:CENabstop{0}"           : "battery capacity switch of the discharge cutoff of the electronic load {0|1|ON|OFF}",
				      "SOURce:BATTary:TENabstop{0}"           : "discharge cut-off time switch of the electronic load {0|1|ON|OFF}",
				      "SOURce:OCP:RANGe{0}"                   : "current range in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:VON{0}"                     : "starting voltage in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:VONDelay{0}"                : "delay time of the starting voltage in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:ISET{0}"                    : "starting current in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:ISTep{0}"                   : "step current in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:IDELaystep{0}"              : "delay time of the step current in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:IMAX{0}"                    : "maximum current in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:IMIN{0}"                    : "minimum current in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:VOCP{0}"                    : "protection voltage in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OCP:TOCP{0}"                    : "maximum overcurrent protection time in OCP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:VON{0}"                     : "starting voltage in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:VONDelay{0}"                : "delay time of the starting voltage in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:PSET{0}"                    : "starting power in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:PSTep{0}"                   : "step power in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:PDELaystep{0}"              : "delay time of the step power in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:PMAX{0}"                    : "maximum power in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:PMIN{0}"                    : "minimum power in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:VOPP{0}"                    : "protection voltage in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:OPP:TOPP{0}"                    : "maximum overpower protection time in OPP mode {<value>|MINimum|MAXimum|DEFault}",
				      "SOURce:WAVe:TIMe{0}"                   : "window time in the waveform display interface {ADD|SUB}",
				      "SOURce:WAVe:TSTep{0}"                  : "time step scale in the waveform display interface {1|10}",
				      "SOURce:SENSe{0}"                       : "Enables or disables the Sense function {0|1|ON|OFF}" }

	settings_por_scpi_list = [ ]







