# Greenhouse Simple API

```
/utility/ - адрес базирования протокола
```

##### Температура:

```
./temp/<sensor_id | avg>

<sensor_id> - value(0-4) - номер датчика
avg - среднее значение всех датчиков
```

##### Влажность воздуха:

```
./air_hum/<sensor_id | avg>

<sensor_id> - value(0-4) - номер датчика
avg - среднее значение всех датчиков
```

##### Влажность почвы:

```
./soil_hum/<sensor_id>

<sensor_id> - value(0-6) - номер датчика
```
