# Misc | joKER's trap

## Информация

> Нам давно известно, что некоторый joKER помогает Arbalest of Siberia делать нехорошие дела.
> 
> Один из наших агентов попал в его ловушку и не может понять, как из неё выбраться.
> 
> Посмотри может у тебя получится помочь ему.
> 
> `nc <ip> <port>`
>
> флаг находится в текущей директории в файле `flag.txt`


## Запуск

Отдать командам ip-адрес и порт где запущен сервер

```sh
cd deploy
docker-compose up --build -d
```


## Описание

Pyjail on python 2.7 

Суть задания - прочитать flag.txt


## Решение

Самый простой вариант прочитать файл, это использовать SSTI-пейлоад для чтения файла.

[Пример пейлоада](solve/payload.txt)

## Флаг

`Cup{011d886a7de28dc26896c8fa4e9961b48f823caadafc96c385620dc91610221f}`
