############### Образ для сборки виртуального окружения ################
# Основа — «тяжелый» (~1 ГБ, в сжатом виде ~500 ГБ) образ со всеми необходимыми
# библиотеками для сборки модулей
FROM --platform=linux/amd64 snakepacker/python:all as builder

# Создаем виртуальное окружение и обновляем pip
RUN python3.8 -m venv /usr/share/python3/app
RUN /usr/share/python3/app/bin/pip install -U pip

# Устанавливаем зависимости отдельно, чтобы закешировать. При последующей сборке
# Docker пропустит этот шаг, если requirements.txt не изменится
COPY requirements.txt /mnt/
RUN /usr/share/python3/app/bin/pip install -Ur /mnt/requirements.txt

# Копируем source distribution в контейнер и устанавливаем его
COPY dist/ /mnt/dist/
#COPY requirements.txt /mnt/dist/
RUN /usr/share/python3/app/bin/pip install /mnt/dist/* \
    && /usr/share/python3/app/bin/pip check

########################### Финальный образ ############################
# За основу берем «легкий» (~100 МБ, в сжатом виде ~50 МБ) образ с Python
FROM snakepacker/python:3.8 as api

# Копируем в него готовое виртуальное окружение из контейнера builder
COPY --from=builder /usr/share/python3/app /usr/share/python3/app

# Устанавливаем ссылки, чтобы можно было воспользоваться командами
# приложения
RUN ln -snf /usr/share/python3/app/bin/disc_backend-* /usr/local/bin/

# Устанавливаем выполняемую при запуске контейнера команду по умолчанию
CMD ["disc_backend-api"]