import base_enums

class ApplicationModeMenager:
    
    @staticmethod
    def get_application_mode_from_id(application_mode_as_id):
        for application_mode in base_enums.ApplicationMode:
            if application_mode.value == application_mode_as_id:
                return application_mode
        raise Exception("No application mode could be found for given application mode parameters")    
            
   