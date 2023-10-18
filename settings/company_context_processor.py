from .models import Company




def get_company_data(self):
    data = Company.objects.last()
    
    return {'company_data':data}