import serial
import time
import serial.tools.list_ports
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] #cписок скоростей
ports = [p.device for p in serial.tools.list_ports.comports()] #цикл заносит в список найденные порты
try: #проверка на ошибки
 port_name = ports[0] #заносим в переменную первый найденный порт
 port_speed = int(speeds[-1]) #заносим в переменную скорость
 port_timeout = 10 #заносим в переменную время таймаута
 ard = serial.Serial(port_name, port_speed, timeout = port_timeout) #передаём в библиотеку данные
 time.sleep(1) #задержка
 ard.flushInput() #метод, который очищает все ожидающие символы и буфер RX потока
 try: #проверка на ошибки
  msg_bin = ard.read(ard.inWaiting()) #читаем все символы в буфере
  msg_bin += ard.read(ard.inWaiting()) #читаем все символы в буфере и прибавляем к уже имеющимся
  msg_bin += ard.read(ard.inWaiting()) #читаем все символы в буфере и прибавляем к уже имеющимся
  msg_bin += ard.read(ard.inWaiting()) #читаем все символы в буфере и прибавляем к уже имеющимся
  msg_str_ = msg_bin.decode() #декодируем
  print(len(msg_bin)) #выводим длину полученных символов
 except Exception as e: 
  print('Error!')
 ard.close() #закрываем
 time.sleep(1) #задержка
 print(msg_str_) #вывод полученных символов
except Exception as e:
 print('Порты отсутствуют')
