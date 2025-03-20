def make_car( marca, modello, **dettagli):
    car_info = {'marca': marca, 'modello': modello}
    car_info.update(dettagli)
    return car_info

car = make_car ('fiat', '500', color = 'grigio')
print(car)
