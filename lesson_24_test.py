class Car:
    def __init__(self, year_model, make):
        self.speed = 0
        self.year_model = year_model
        self.make = make
    def accelerate(self):
        self.speed += 3
    def break_(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed

car = Car("2015","VW Polo")
car_2 = Car("2017","Skoda Rapid")
def test_start_speed():
    assert car.get_speed() == 0

for i in range(5):
    car.accelerate()
    print(f"Текущая скорость авто {car.get_speed()}")

for i in range(5):
    car.break_()
    print(f"Текущая скорость авто {car.get_speed()}")


# Проверка, увеличивается ли скорость точно на 5
def get_speed():
    car.accelerate()
    assert car.get_speed() == 5

# установка
pip install pytest
pip install pytest-html
pip install pytest-json
# запуск
pytest --html=report.html
pytest --json=report.json