sales_data = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 2, 'region': 'NA'},
    {'product': 'Mouse', 'price': 25, 'quantity': 10, 'region': 'EU'},
    {'product': 'Keyboard', 'price': 75, 'quantity': 5, 'region': 'NA'},
    {'product': 'Monitor', 'price': 300, 'quantity': 3, 'region': 'APAC'},
]

def create_pipeline(*steps):
    def pipeline_func(data):
        print("Initial Data:",data)
        res=data    
        for step in steps:
            print(step)
            res=step(res)
        return res
    return pipeline_func


def filtered_by_region(region):
    print("Region:",region)
    def filter_func(data):
        print('filter_func:',data)
        return filter(lambda item:item['region']==region,data)
    return filter_func

def calculate_total_sales(data):
    print('calculate_total_sales:',data)
    return map(lambda item: {**item, 'total':item['price']*item['quantity']},data)


def sort_by_total(data):
    print('sort_by_total:',data)
    return sorted(data, key=lambda item: item['total'], reverse=True)

na_sales_pipeline = create_pipeline(
    filtered_by_region('NA'),
    calculate_total_sales,
    sort_by_total
)

top_na_sales=list(na_sales_pipeline(sales_data))


print("Top sales in North America")

for sale in top_na_sales:
    print(sale)