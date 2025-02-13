# Pwn | Teleport

## Информация

> Для борьбы против Arbalest of Siberia нам понадобился телепорт.
>
> Посмотрим, всё ли правильно делаем?
> 
> `nc <ip> <port>`
>
> `flag in /tmp/flag.txt`

## Запуск

Отдать командам всё из deploy/static и ip-адрес сервера

```sh
cd deploy
docker-compose -p teleport up --build -d 
```


## Описание

ELF 64bit, C, no strip, no pack

Суть задания - перезаписать master-cookie и получить утечку из libc


## Решение

1. Смещение от создаваемого с помощью mmap региона памяти до TLS всегда одинаковое (для одной и той же libc)
2. Запускаем локально и находим смещение до перезаписи канарейки, которая используется во всех функциях
3. Переписываем канарейку
4. Находим смещение в libc, по которому сможем получить утечку адреса
5. Получаем утечку
6. Используем переполнение буфера на стеке и one_gadget для получения шелла

[Пример эксплоита](solve/exploit.py)


## Флаг

`Cup{469ab7bcb81db06e9bebd5e6561215c43b7b77eebe6eb7558ba071dca9c0ff61}`
