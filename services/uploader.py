class Uploader:

    @staticmethod
    def upload_images_to_products(instance, filename):
        return f"products/{instance.slug}/{filename}"

    @staticmethod
    def upload_images_to_categories(instance, filename):
        return f"categories/{instance.slug}/{filename}"
