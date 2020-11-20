import csv
from django.http import HttpResponse

def export_to_csv(queryset, fields, columns, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={filename}.csv'
    writer = csv.writer(response)
    headers = fields
    writer.writerow(columns)
    
    for item in queryset:
        writer.writerow([getattr(item, field) for field in headers]
    return response
