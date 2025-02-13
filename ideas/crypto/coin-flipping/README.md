# Crypto | Coin Flipping

## Информация

> Монетка — древнейший и эффективный способ разрешения конфликтов, универсальное средство выбора.
> 
> После победы над Arbalests of Siberia нам нужно будет подумать о правильном распределении ресурсов между Землёй и Kzfland-52.
> 
> Представьте, что у вас есть две модели потребления — модель Kzfland-52 и современная земная модель, а ваши ресурсы ограничены.
> 
> Как вы их поделите?
> 
> `nc host 44147`


## Описание

[Сервер](service/server.py) "подбрасывает" монетку и предлагает нам угадать результат. Если угадать 50 раз, то мы получим флаг. Результат каждого подбрасывания [подписывается](https://en.wikipedia.org/wiki/Commitment_scheme#Coin_flipping), чтобы мы могли быть уверены, что сервер нас не обманывает.


## Решение

Если посмотреть на класс `Cipher`, то можно заметить, что по сути он генерирует нужное количество байтов и ксорит входные данные. Используемый генератор — [Dual_EC_DRBG](https://ru.wikipedia.org/wiki/Dual_EC_DRBG), который был отозван NIST из-за возможного наличия бекдора.

В таске как раз бекдор явный, его можно найти в методе получения точек:

```py3
def _get_points(self, curve):
    P = curve.G
    Q = 31337 * P
    return P, Q
```

Зная, как генерируются точки `P` и `Q`, можно скомпрометировать генератор и угадывать "подбрасывания" монеток на сервере.

[Пример решения](exploit.py)


## Флаг

`Cup{1t's_t00_34sy_t0_br34k_th3_3ncrypt10n_1f_y0u_kn0w_th3_b4ckd00r}`
