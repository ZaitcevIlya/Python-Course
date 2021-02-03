# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Enter time in seconds: '))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time - (hours * 3600) - (minutes * 60)

f_hours = f'0{hours}' if len(str(hours)) == 1 else hours
f_minutes = f'0{minutes}' if len(str(minutes)) == 1 else minutes
f_seconds = f'0{seconds}' if len(str(seconds)) == 1 else seconds

print(f'Your entered time is: {f_hours}:{f_minutes}:{f_seconds}')
