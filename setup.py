from setuptools import setup, find_packages

setup(
    name = 'django-lazycrud-bs5',
    version = '0.1.0',
    packages = find_packages(),
    author = 'Matteo Sorrentino',
    author_email = 'mtsorre@gmail.com',
    license='MIT',
    description = 'A little Django app to reduce boilerplate code at a minimum when you write class based views in a typical CRUD scenario.',
    url = 'https://github.com/matteosorre/django-lazycrud-bs5',
    keywords = ['django', 'crud', 'bs5', 'bootstrap5'],
    include_package_data = True,
    zip_safe=False,
    install_requires=[
        'django-crispy-forms>=2.0',
        'crispy-bootstrap5>=2024.1',
    ]
)
