import pytest

class Patient:
    def __init__(self, fio, address, phone, name_trusted, phone_trusted):
        self.fio = fio
        self.address = address
        self.phone = phone
        self.name_trusted = name_trusted
        self.phone_trusted = phone_trusted

    def get_fio(self):
        return self.fio

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_name_trusted(self):
        return self.name_trusted

    def get_phone_trusted(self):
        return self.phone_trusted

    def edit_fio(self, fio):
        self.fio = fio

    def edit_address(self, address):
        self.address = address

    def edit_phone(self, phone):
        self.phone = phone

    def edit_name_trusted(self, name_trusted):
        self.name_trusted = name_trusted

    def edit_phone_trusted(self, phone_trusted):
        self.phone_trusted = phone_trusted

class Procedure:
    def __init__(self, name_procedure, data_procedure, name_doctor, price):
        self.name_procedure = name_procedure
        self.data_procedure = data_procedure
        self.name_doctor = name_doctor
        self.price = price

    def get_name_procedure(self):
        return self.name_procedure
    def get_data_procedure(self):
        return self.data_procedure
    def get_name_doctor(self):
        return self.name_doctor
    def get_price(self):
        return self.price

    def edit_name_procedure(self, name_procedure):
        self.name_procedure = name_procedure
    def edit_data_procedure(self, data_procedure):
        self.data_procedure = data_procedure
    def edit_name_procedure(self, name_doctor):
        self.name_doctor = name_doctor
    def edit_price(self, price):
        self.price = price


patien_1 = Patient("Иван", "РФ, Смол.обл., г.Смоленск, ул.Железнодорожная, д.2", "+78845641358", "Василий", "+78895181358")
patien_1.edit_address("г. Смоленск, ул. Наравская д.4")


procedures = [{"number_p":"1", "name_p":"врачебный осмотр", "date_p":"сегодняшняя", "doctor_p":"Ирвин", "price":"250.00"}, {"number_p":"2", "name_p":"рентгеноскопия", "date_p":"сегодняшняя", "doctor_p":"Джемисон", "price":"500.00"}, {"number_p":"3", "name_p":"анализ крови", "date_p":"сегодняшняя", "doctor_p":"Смит", "price":"200.00"}]

for i in range(3):
    procedures_1 = Procedure(procedures[i]["name_p"], procedures[i]["date_p"], procedures[i]["doctor_p"], procedures[i]["price"])
    print(f"{"="*18}\n {procedures_1.get_name_procedure()}\n {procedures_1.get_data_procedure()}\n {procedures_1.get_name_doctor()}\n {procedures_1.get_price()}\n")