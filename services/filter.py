class ProductFilter:
    def __init__(self, request, products, query_params):
        self.request = request
        self.products = products
        self.query_params = query_params

    def filter_product_by_category(self, request, products, query_params):
        if "category" in request.GET:
            category = request.GET.getlist('category')
            for cat in category:
                query_params += f"category={cat}&"
            products = products.filter(
                category__id__in=category
            )
        return products, query_params

    def filter_product_by_size(self, request, products, query_params):
        if "size" in request.GET:
            sizes = request.GET.getlist('size')
            for sz in sizes:
                query_params += f"size={sz}&"
            repeated_products = products.filter(
                sizes__id__in=sizes
            )
            products = products.filter(
                id__in=repeated_products.values_list("id", flat=True)
            )
        return products, query_params

    def filter_product_by_price(self, request, products, query_params):
        min_price = request.GET.get("min_price", None)
        max_price = request.GET.get("max_price", None)

        if min_price:
            query_params += f"min_price={min_price}&"
            products = products.filter(
                total_price__gte=min_price
            )

        if max_price:
            query_params += f"max_price={max_price}&"
            products = products.filter(
                total_price__lte=max_price
            )
        return products, query_params

    def filter_products(self):
        products, query_params = self.filter_product_by_category(
            self.request, self.products, self.query_params
        )
        products, query_params = self.filter_product_by_size(
            self.request, products, query_params
        )
        products, query_params = self.filter_product_by_price(
            self.request, products, query_params
        )
        return products, query_params
