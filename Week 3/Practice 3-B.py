{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'cod': '200', 'message': 0.0041, 'cnt': 40, 'list': [{'dt': 1541106000, 'main': {'temp': 11.9, 'temp_min': 7.47, 'temp_max': 11.9, 'pressure': 956.91, 'sea_level': 1033.6, 'grnd_level': 956.91, 'humidity': 78, 'temp_kf': 4.43}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.52, 'deg': 52.5001}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-01 21:00:00'}, {'dt': 1541116800, 'main': {'temp': 8.79, 'temp_min': 5.47, 'temp_max': 8.79, 'pressure': 956.63, 'sea_level': 1033.6, 'grnd_level': 956.63, 'humidity': 76, 'temp_kf': 3.33}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.41, 'deg': 62.0008}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 00:00:00'}, {'dt': 1541127600, 'main': {'temp': 6.48, 'temp_min': 4.26, 'temp_max': 6.48, 'pressure': 956.81, 'sea_level': 1034.01, 'grnd_level': 956.81, 'humidity': 61, 'temp_kf': 2.22}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.42, 'deg': 62.0016}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 03:00:00'}, {'dt': 1541138400, 'main': {'temp': 13.76, 'temp_min': 12.65, 'temp_max': 13.76, 'pressure': 957.3, 'sea_level': 1034.36, 'grnd_level': 957.3, 'humidity': 33, 'temp_kf': 1.11}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.77, 'deg': 71.0013}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-02 06:00:00'}, {'dt': 1541149200, 'main': {'temp': 21, 'temp_min': 21, 'temp_max': 21, 'pressure': 956.6, 'sea_level': 1033.01, 'grnd_level': 956.6, 'humidity': 36, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.82, 'deg': 90.0079}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-02 09:00:00'}, {'dt': 1541160000, 'main': {'temp': 22.58, 'temp_min': 22.58, 'temp_max': 22.58, 'pressure': 954.74, 'sea_level': 1030.88, 'grnd_level': 954.74, 'humidity': 29, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.16, 'deg': 101.503}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-02 12:00:00'}, {'dt': 1541170800, 'main': {'temp': 17.74, 'temp_min': 17.74, 'temp_max': 17.74, 'pressure': 954.6, 'sea_level': 1030.81, 'grnd_level': 954.6, 'humidity': 34, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.5, 'deg': 92.5022}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 15:00:00'}, {'dt': 1541181600, 'main': {'temp': 9.51, 'temp_min': 9.51, 'temp_max': 9.51, 'pressure': 954.9, 'sea_level': 1031.46, 'grnd_level': 954.9, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.21, 'deg': 96.5008}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 18:00:00'}, {'dt': 1541192400, 'main': {'temp': 6.75, 'temp_min': 6.75, 'temp_max': 6.75, 'pressure': 954.58, 'sea_level': 1031.46, 'grnd_level': 954.58, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.21, 'deg': 82.5018}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 21:00:00'}, {'dt': 1541203200, 'main': {'temp': 5.69, 'temp_min': 5.69, 'temp_max': 5.69, 'pressure': 954.25, 'sea_level': 1031.31, 'grnd_level': 954.25, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.47, 'deg': 80.0005}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-03 00:00:00'}, {'dt': 1541214000, 'main': {'temp': 5, 'temp_min': 5, 'temp_max': 5, 'pressure': 954.18, 'sea_level': 1031.55, 'grnd_level': 954.18, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.86, 'deg': 78.0001}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-03 03:00:00'}, {'dt': 1541224800, 'main': {'temp': 11.19, 'temp_min': 11.19, 'temp_max': 11.19, 'pressure': 954.58, 'sea_level': 1031.96, 'grnd_level': 954.58, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 24}, 'wind': {'speed': 2.43, 'deg': 79.0034}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-03 06:00:00'}, {'dt': 1541235600, 'main': {'temp': 18.31, 'temp_min': 18.31, 'temp_max': 18.31, 'pressure': 953.56, 'sea_level': 1030.18, 'grnd_level': 953.56, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 36}, 'wind': {'speed': 3.75, 'deg': 87.0011}, 'rain': {'3h': 0.025}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-03 09:00:00'}, {'dt': 1541246400, 'main': {'temp': 19.75, 'temp_min': 19.75, 'temp_max': 19.75, 'pressure': 951.6, 'sea_level': 1027.71, 'grnd_level': 951.6, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 24}, 'wind': {'speed': 4.93, 'deg': 99.0025}, 'rain': {'3h': 0.005}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-03 12:00:00'}, {'dt': 1541257200, 'main': {'temp': 16.75, 'temp_min': 16.75, 'temp_max': 16.75, 'pressure': 951.53, 'sea_level': 1027.74, 'grnd_level': 951.53, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 48}, 'wind': {'speed': 4.22, 'deg': 91.5019}, 'rain': {'3h': 0.02}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-03 15:00:00'}, {'dt': 1541268000, 'main': {'temp': 14.6, 'temp_min': 14.6, 'temp_max': 14.6, 'pressure': 952.08, 'sea_level': 1028.69, 'grnd_level': 952.08, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 56}, 'wind': {'speed': 3.22, 'deg': 89.5007}, 'rain': {'3h': 0.05}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-03 18:00:00'}, {'dt': 1541278800, 'main': {'temp': 13.12, 'temp_min': 13.12, 'temp_max': 13.12, 'pressure': 951.74, 'sea_level': 1028.6, 'grnd_level': 951.74, 'humidity': 96, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 64}, 'wind': {'speed': 2.76, 'deg': 68.5012}, 'rain': {'3h': 0.05}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-03 21:00:00'}, {'dt': 1541289600, 'main': {'temp': 12.6, 'temp_min': 12.6, 'temp_max': 12.6, 'pressure': 950.6, 'sea_level': 1027.58, 'grnd_level': 950.6, 'humidity': 94, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 76}, 'wind': {'speed': 2.66, 'deg': 61.5}, 'rain': {'3h': 0.12}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-04 00:00:00'}, {'dt': 1541300400, 'main': {'temp': 13.08, 'temp_min': 13.08, 'temp_max': 13.08, 'pressure': 949.62, 'sea_level': 1026.64, 'grnd_level': 949.62, 'humidity': 93, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 92}, 'wind': {'speed': 2.16, 'deg': 42.0028}, 'rain': {'3h': 0.14}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-04 03:00:00'}, {'dt': 1541311200, 'main': {'temp': 15.34, 'temp_min': 15.34, 'temp_max': 15.34, 'pressure': 949.67, 'sea_level': 1026.6, 'grnd_level': 949.67, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 2.06, 'deg': 39.5038}, 'rain': {'3h': 0.06}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-04 06:00:00'}, {'dt': 1541322000, 'main': {'temp': 18.99, 'temp_min': 18.99, 'temp_max': 18.99, 'pressure': 948.5, 'sea_level': 1024.9, 'grnd_level': 948.5, 'humidity': 65, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 56}, 'wind': {'speed': 2.16, 'deg': 345.001}, 'rain': {'3h': 0.03}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-04 09:00:00'}, {'dt': 1541332800, 'main': {'temp': 20.14, 'temp_min': 20.14, 'temp_max': 20.14, 'pressure': 947.11, 'sea_level': 1023.22, 'grnd_level': 947.11, 'humidity': 57, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 80}, 'wind': {'speed': 2.96, 'deg': 321.001}, 'rain': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-04 12:00:00'}, {'dt': 1541343600, 'main': {'temp': 17.38, 'temp_min': 17.38, 'temp_max': 17.38, 'pressure': 947.66, 'sea_level': 1023.76, 'grnd_level': 947.66, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 24}, 'wind': {'speed': 2.52, 'deg': 323.002}, 'rain': {'3h': 0.48}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-04 15:00:00'}, {'dt': 1541354400, 'main': {'temp': 11.72, 'temp_min': 11.72, 'temp_max': 11.72, 'pressure': 948.23, 'sea_level': 1024.84, 'grnd_level': 948.23, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.66, 'deg': 340.517}, 'rain': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-04 18:00:00'}, {'dt': 1541365200, 'main': {'temp': 8.43, 'temp_min': 8.43, 'temp_max': 8.43, 'pressure': 947.91, 'sea_level': 1024.91, 'grnd_level': 947.91, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.86, 'deg': 25.0023}, 'rain': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-04 21:00:00'}, {'dt': 1541376000, 'main': {'temp': 7.09, 'temp_min': 7.09, 'temp_max': 7.09, 'pressure': 947.31, 'sea_level': 1024.4, 'grnd_level': 947.31, 'humidity': 90, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.86, 'deg': 150.007}, 'rain': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-05 00:00:00'}, {'dt': 1541386800, 'main': {'temp': 6.22, 'temp_min': 6.22, 'temp_max': 6.22, 'pressure': 946.76, 'sea_level': 1024.02, 'grnd_level': 946.76, 'humidity': 89, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.17, 'deg': 171.002}, 'rain': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-05 03:00:00'}, {'dt': 1541397600, 'main': {'temp': 12.68, 'temp_min': 12.68, 'temp_max': 12.68, 'pressure': 947.4, 'sea_level': 1024.7, 'grnd_level': 947.4, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 68}, 'wind': {'speed': 1.62, 'deg': 204.501}, 'rain': {'3h': 0.03}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-05 06:00:00'}, {'dt': 1541408400, 'main': {'temp': 15.92, 'temp_min': 15.92, 'temp_max': 15.92, 'pressure': 947.37, 'sea_level': 1024.18, 'grnd_level': 947.37, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 76}, 'wind': {'speed': 2.11, 'deg': 247.005}, 'rain': {'3h': 0.12}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-05 09:00:00'}, {'dt': 1541419200, 'main': {'temp': 17.11, 'temp_min': 17.11, 'temp_max': 17.11, 'pressure': 946.8, 'sea_level': 1023.42, 'grnd_level': 946.8, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 44}, 'wind': {'speed': 3.41, 'deg': 257}, 'rain': {'3h': 0.04}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-05 12:00:00'}, {'dt': 1541430000, 'main': {'temp': 14.8, 'temp_min': 14.8, 'temp_max': 14.8, 'pressure': 947.77, 'sea_level': 1024.64, 'grnd_level': 947.77, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 68}, 'wind': {'speed': 3.06, 'deg': 262}, 'rain': {'3h': 0.62}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-05 15:00:00'}, {'dt': 1541440800, 'main': {'temp': 12.77, 'temp_min': 12.77, 'temp_max': 12.77, 'pressure': 948.68, 'sea_level': 1025.93, 'grnd_level': 948.68, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 76}, 'wind': {'speed': 1.86, 'deg': 248.506}, 'rain': {'3h': 2.54}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-05 18:00:00'}, {'dt': 1541451600, 'main': {'temp': 12.86, 'temp_min': 12.86, 'temp_max': 12.86, 'pressure': 948.86, 'sea_level': 1026.07, 'grnd_level': 948.86, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 80}, 'wind': {'speed': 2.87, 'deg': 247.502}, 'rain': {'3h': 1.88}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-05 21:00:00'}, {'dt': 1541462400, 'main': {'temp': 13.27, 'temp_min': 13.27, 'temp_max': 13.27, 'pressure': 948.85, 'sea_level': 1025.92, 'grnd_level': 948.85, 'humidity': 98, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 80}, 'wind': {'speed': 3.42, 'deg': 246.007}, 'rain': {'3h': 1.35}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-06 00:00:00'}, {'dt': 1541473200, 'main': {'temp': 13.25, 'temp_min': 13.25, 'temp_max': 13.25, 'pressure': 949.24, 'sea_level': 1026.42, 'grnd_level': 949.24, 'humidity': 98, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 92}, 'wind': {'speed': 2.96, 'deg': 249.001}, 'rain': {'3h': 1.78}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-06 03:00:00'}, {'dt': 1541484000, 'main': {'temp': 13.99, 'temp_min': 13.99, 'temp_max': 13.99, 'pressure': 951.15, 'sea_level': 1028.18, 'grnd_level': 951.15, 'humidity': 99, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 32}, 'wind': {'speed': 2.08, 'deg': 240}, 'rain': {'3h': 1.02}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-06 06:00:00'}, {'dt': 1541494800, 'main': {'temp': 16.94, 'temp_min': 16.94, 'temp_max': 16.94, 'pressure': 951.31, 'sea_level': 1028.2, 'grnd_level': 951.31, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.06, 'deg': 260.006}, 'rain': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-06 09:00:00'}, {'dt': 1541505600, 'main': {'temp': 15.88, 'temp_min': 15.88, 'temp_max': 15.88, 'pressure': 951.51, 'sea_level': 1028.37, 'grnd_level': 951.51, 'humidity': 94, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 76}, 'wind': {'speed': 3.11, 'deg': 262.006}, 'rain': {'3h': 0.41}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-06 12:00:00'}, {'dt': 1541516400, 'main': {'temp': 14.46, 'temp_min': 14.46, 'temp_max': 14.46, 'pressure': 952.53, 'sea_level': 1029.67, 'grnd_level': 952.53, 'humidity': 95, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 76}, 'wind': {'speed': 2.26, 'deg': 259.507}, 'rain': {'3h': 0.28}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-06 15:00:00'}, {'dt': 1541527200, 'main': {'temp': 13.63, 'temp_min': 13.63, 'temp_max': 13.63, 'pressure': 953.91, 'sea_level': 1031.2, 'grnd_level': 953.91, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 80}, 'wind': {'speed': 1.67, 'deg': 246.001}, 'rain': {'3h': 0.039999999999999}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-06 18:00:00'}], 'city': {'id': 250441, 'name': 'Amman', 'coord': {'lat': 31.9516, 'lon': 35.924}, 'country': 'JO', 'population': 1275857}}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "forecast_link = \"http://api.openweathermap.org/data/2.5/forecast\"\n",
    "\n",
    "forecast_parameters = {\n",
    "   \"APPID\":\"c1b18ae011a7b56982725966192c78cc\",\n",
    "   \"q\":\"Amman,Jo\",\n",
    "   \"units\":\"metric\"\n",
    "    \n",
    "}\n",
    "\n",
    "forecast_data = requests.get(forecast_link,forecast_parameters).json()\n",
    "\n",
    "print(forecast_data)\n",
    "\n",
    "   \n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weather forecast for Day 1 :  {'dt': 1541106000, 'main': {'temp': 11.9, 'temp_min': 7.47, 'temp_max': 11.9, 'pressure': 956.91, 'sea_level': 1033.6, 'grnd_level': 956.91, 'humidity': 78, 'temp_kf': 4.43}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.52, 'deg': 52.5001}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-01 21:00:00'}\n",
      "**************\n",
      "Weather forecast for Day 2 :  {'dt': 1541116800, 'main': {'temp': 8.79, 'temp_min': 5.47, 'temp_max': 8.79, 'pressure': 956.63, 'sea_level': 1033.6, 'grnd_level': 956.63, 'humidity': 76, 'temp_kf': 3.33}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.41, 'deg': 62.0008}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 00:00:00'}\n",
      "**************\n",
      "Weather forecast for Day 3 :  {'dt': 1541127600, 'main': {'temp': 6.48, 'temp_min': 4.26, 'temp_max': 6.48, 'pressure': 956.81, 'sea_level': 1034.01, 'grnd_level': 956.81, 'humidity': 61, 'temp_kf': 2.22}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.42, 'deg': 62.0016}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-02 03:00:00'}\n",
      "**************\n",
      "Weather forecast for Day 4 : {'dt': 1541138400, 'main': {'temp': 13.76, 'temp_min': 12.65, 'temp_max': 13.76, 'pressure': 957.3, 'sea_level': 1034.36, 'grnd_level': 957.3, 'humidity': 33, 'temp_kf': 1.11}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.77, 'deg': 71.0013}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-02 06:00:00'}\n",
      "**************\n",
      "Weather forecast for Day 5 : {'dt': 1541149200, 'main': {'temp': 21, 'temp_min': 21, 'temp_max': 21, 'pressure': 956.6, 'sea_level': 1033.01, 'grnd_level': 956.6, 'humidity': 36, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.82, 'deg': 90.0079}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-02 09:00:00'}\n"
     ]
    }
   ],
   "source": [
    "print(\"Weather forecast for Day 1 : \" , forecast_data[\"list\"][0])\n",
    "print(\"**************\") \n",
    "print(\"Weather forecast for Day 2 : \" , forecast_data[\"list\"][1])\n",
    "print(\"**************\")\n",
    "print(\"Weather forecast for Day 3 : \" , forecast_data[\"list\"][2])\n",
    "print(\"**************\")\n",
    "print(\"Weather forecast for Day 4 :\"  , forecast_data[\"list\"][3])\n",
    "print(\"**************\")\n",
    "print(\"Weather forecast for Day 5 :\"  , forecast_data[\"list\"][4])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
