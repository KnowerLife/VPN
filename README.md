# Сгенерируйте конфиг Cloudflare WARP для AmneziaWG и WireGuard
Этот bash скрипт сгенерирует конфиг Cloudflare WARP для AmneziaWG и WireGuard.

Не стоит выполнять его локально, так как РКН заблокировал запросы для получения конфига. Вместо этого лучше выполнять на удалённых серверах.

## 1: Aeza Terminator
1. Заходим на https://terminator.aeza.net/en/
2. Выбираем **Debian**
3. Вставляем команду:
```bash
bash <(wget --inet4-only -qO- https://raw.githubusercontent.com/KnowerLife/VPN/refs/heads/main/warp_generator.sh)
```
2. После того, как конфиг сгенерируется, копируем его, либо скачиваем файлом по ссылке и импортируем в AmneziaWG или WireGuard!

3. Теперь нужно установить AmneziaWG или WireGuard и импортировать туда конфиг.​

### На Windows: 
https://github.com/amnezia-vpn/amneziawg-windows-client/releases/download/1.0.0/amneziawg-amd64-1.0.0.msi
https://download.wireguard.com/windows-client/wireguard-installer.exe

### На macOS/iOS: 
https://apps.apple.com/ru/app/amneziawg/id6478942365
https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12
https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8

### На Android: 
https://github.com/amnezia-vpn/amneziawg-android/releases/download/v1.1.1/AmneziaWG.apk
https://play.google.com/store/apps/details?id=com.wireguard.android
(Естественно, есть и в Play Маркете)

### На Linux: 
https://github.com/amnezia-vpn/amneziawg-go

### На роутеры OpenWRT: 
https://github.com/amnezia-vpn/amneziawg-openwrt

После установки запускаем и импортируем конфиг (тот самый скачанный файл):

(на Android импортируем по кнопке + внизу)

Подключаемся. Убеждаемся, что трафик идёт

## Для правильной работы WireGuard удаляем строки из полученного конфига WARP.conf
S1 = 0

S2 = 0

Jc = 120

Jmin = 23

Jmax = 911

H1 = 1

H2 = 2

H3 = 3

H4 = 4

MTU = 1280

## Что-то не получается?
### После подключении в AmneziaWG ничего не работает, в строке **Передача**: получено 0 Б
К сожалению, AmneziaWG не удалось обойти блокировку WireGuard от вашего провайдера

### Вот за что отвечают параметры:
Jc (Junk packet count) - количество пакетов со случайными данными, которые отправляются перед началом сессии

Jmin (Junk packet minimum size) - минимальный размер пакета для Junk packet. То есть все рандомно генерируемые пакеты будут иметь размер не меньше чем Jmin

Jmax (Junk packet maximum size) - максимальный размер для Junk пакетов

S1 (Init packet junk size) - размер случайных данных, которые будут добавлены к init пакету, размер которого изначально фиксированный

S2 (Response packet junk size) - размер случайных данных, которые будут добавлены к ответу, размер которого изначально фиксированный

H1 (Init packet magic header) - заголовок первого байта рукопожатия

H2 (Response packet magic header) - заголовок первого байта ответа на рукопожатие

H4 (Transport packet magic header) - заголовок пакета передаваемых данных

H3 (Underload packet magic header) - заголовок пакета UnderLoad

### Пробуйте менять разные параметры, пока не подберёте те, с которыми всё заработает.


### На мобильных обычно работает:
Jc = 4

Jmin = 40

Jmax = 70

### Другой вопрос?
Напишите в чат: https://t.me/KnowerLifeBot
