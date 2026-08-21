from faker import Faker

fake = Faker()


def generate_email():
    return fake.email()


def generate_password():
    return fake.password()


def generate_text():
    return fake.paragraph()


def generate_name():
    return fake.name()


def generate_number():
    return fake.random_number()
