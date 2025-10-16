from django import template
register = template.Library()

@register.filter(name ='row_split'  )
def row_split(list_data,n):
    row=[]
    i=0
    for data in list_data:
        row.append(data)
        i+=1
        if i==n:
            yield row
            row=[]
            i=0
    yield row
        

    
