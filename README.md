# Генерация конфига Cloudflare WARP для AmneziaWG и WireGuard

Эта инструкция поможет вам сгенерировать конфигурацию Cloudflare WARP для использования с клиентами AmneziaWG и WireGuard. Следуйте шагам ниже, чтобы настроить VPN-соединение.

> **Внимание**: В некоторых регионах, например, в России, доступ к ресурсам для генерации конфига может быть ограничен (РКН). Рекомендуется выполнять скрипт на удалённом сервере, например, через [Aeza Terminator](https://terminator.aeza.net/en/).

---

## Содержание
- [Требования](#требования)
- [Генерация конфига](#генерация-конфига)
- [Установка клиентов](#установка-клиентов)
- [Импорт конфига](#импорт-конфига)
- [Проверка подключения](#проверка-подключения)
- [Настройка параметров](#настройка-параметров)
- [Устранение неполадок](#устранение-неполадок)
- [Поддержка](#поддержка)
- [Пример конфига](#пример-конфига)

---

## Требования

Перед началом убедитесь, что у вас есть:
- Доступ к удалённому серверу с Debian (или другой совместимой ОС).
- Установленные утилиты `wget` и `curl`. Для установки на Debian:
  ```bash
  sudo apt update && sudo apt install -y wget curl
  ```
- Установленный клиент AmneziaWG или WireGuard на вашем устройстве (см. [Установка клиентов](#установка-клиентов)).
- Доступ к интернету без строгих ограничений UDP-портов.

> **Примечание**: Если доступ к GitHub заблокирован, используйте VPN или зеркало для загрузки скрипта.

---

## Генерация конфига

1. Перейдите на [Aeza Terminator](https://terminator.aeza.net/en/) и выберите сервер с Debian.
2. Выполните команду для генерации конфига:
   ```bash
   bash <(wget --inet4-only -qO- https://github.com/KnowerLife/VPN/raw/refs/heads/main/warp_generator.sh)
   ```
3. После выполнения скрипта:
   - Скопируйте сгенерированный конфиг (текст или QR-код).
   - Или скачайте файл конфигурации по предоставленной ссылке.

> **Альтернатива**: Если доступ к скрипту заблокирован, скачайте его вручную:
> ```bash
> wget https://raw.githubusercontent.com/KnowerLife/VPN/main/warp_generator.sh
> chmod +x warp_generator.sh
> ./warp_generator.sh
> ```

---

## Установка клиентов

Установите клиент AmneziaWG или WireGuard в зависимости от вашей платформы:

| Платформа | AmneziaWG | WireGuard | AmneziaVPN |
|-----------|-----------|-----------|-----------|
| **Windows** | [Скачать](https://github.com/amnezia-vpn/amneziawg-windows-client/releases/download/1.0.0/amneziawg-amd64-1.0.0.msi) | [Скачать](https://download.wireguard.com/windows-client/wireguard-installer.exe) | [Скачать](https://github.com/amnezia-vpn/amnezia-client/releases/download/4.8.9.2/AmneziaVPN_4.8.9.2_windows_x64.exe) |
| **macOS** | [Скачать](https://apps.apple.com/ru/app/amneziawg/id6478942365) | [Скачать](https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12) | [Скачать](https://github.com/amnezia-vpn/amnezia-client/releases/download/4.8.9.2/AmneziaVPN_4.8.9.2_macos.zip) |
| **iOS** | [Скачать](https://apps.apple.com/ru/app/amneziawg/id6478942365) | [Скачать](https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8) | [Скачать](https://apps.apple.com/us/app/amneziavpn/id1600529900) |
| **Android** | [Скачать](https://github.com/amnezia-vpn/amneziawg-android/releases/download/v1.1.1/AmneziaWG.apk) | [Скачать](https://play.google.com/store/apps/details?id=com.wireguard.android) | [Скачать](https://github.com/amnezia-vpn/amnezia-client/releases/tag/4.8.9.2) |
| **Linux** | [Скачать](https://github.com/amnezia-vpn/amneziawg-go) | Установить через пакетный менеджер, например: `sudo apt install wireguard` | [Скачать](https://github.com/amnezia-vpn/amnezia-client/releases/download/4.8.9.2/AmneziaVPN_4.8.9.2_linux_x64.tar.zip) |
| **OpenWRT** | [Скачать](https://github.com/amnezia-vpn/amneziawg-openwrt) | Следуйте [инструкции](https://www.wireguard.com/install/) | [Пока что нет инструкций] |

---

## Импорт конфига

1. Установите клиент для вашей платформы.
2. Импортируйте сгенерированный конфиг:
   - **AmneziaWG**:
     - Откройте приложение.
     - Выберите «Импорт конфигурации» и укажите файл `WARP.conf` или вставьте текст конфига.
     - Нажмите «Подключиться».
   - **AmneziaVPN**:
     - Откройте приложение.
     - Выберите «Импорт конфигурации» и укажите файл `WARP.conf` или вставьте текст конфига.
     - Нажмите «Подключиться».
   - **WireGuard**:
     - Откройте приложение.
     - Нажмите «+» (или эквивалент) и выберите «Импорт из файла» или «Сканировать QR-код».
     - Укажите файл `WARP.conf` или отсканируйте QR-код.
   - **Для WireGuard**: Перед импортом удалите из конфига следующие строки:
     ```plaintext
     S1 = 0
     S2 = 0
     Jc = 4
     Jmin = 40
     Jmax = 70
     H1 = 1
     H2 = 2
     H3 = 3
     H4 = 4
     MTU = 1280
     I1 = ...
     ```

3. Подключитесь к VPN.

---

## Проверка подключения

После подключения убедитесь, что VPN работает:
1. Проверьте ваш внешний IP:
   ```bash
   curl ifconfig.me
   ```
2. Убедитесь, что трафик идёт через Cloudflare WARP:
   ```bash
   curl https://www.cloudflare.com/cdn-cgi/trace
   ```
   В выводе должно быть `warp=on`.
3. Проверьте доступ к заблокированным ресурсам:
   ```bash
   ping google.com
   ```

---

## Настройка параметров

Если соединение нестабильно, настройте параметры в конфиге для обхода блокировок провайдера. Основные параметры:

| Параметр | Описание | Рекомендуемые значения |
|----------|----------|-----------------------|
| `Jc` | Количество Junk-пакетов перед началом сессии | 4–6 |
| `Jmin` | Минимальный размер Junk-пакетов | 20–50 |
| `Jmax` | Максимальный размер Junk-пакетов | 50–100 |
| `S1` | Размер случайных данных в init-пакете | 0 (удалить для WireGuard) |
| `S2` | Размер случайных данных в ответе | 0 (удалить для WireGuard) |
| `H1` | Заголовок первого байта рукопожатия | 1 (удалить для WireGuard) |
| `H2` | Заголовок первого байта ответа | 2 (удалить для WireGuard) |
| `H3` | Заголовок пакета UnderLoad | 3 (удалить для WireGuard) |
| `H4` | Заголовок пакета данных | 4 (удалить для WireGuard) |
| `MTU` | Максимальный размер пакета | 1280 (удалить или оставить) |

**Рекомендации для мобильных сетей**:
```plaintext
Jc = 4
Jmin = 40
Jmax = 70
```

**Для низкоскоростных соединений**:
```plaintext
Jc = 2
Jmin = 20
Jmax = 50
```

Экспериментируйте с параметрами, пока не найдёте подходящие для вашей сети.

---

## Устранение неполадок

| Проблема | Решение |
|----------|---------|
| **Трафик не идёт (0 Б в AmneziaWG)** | 1. Проверьте, удалены ли параметры `S1`, `S2`, `Jc`, и т.д. для WireGuard.<br>2. Измените параметры `Jc`, `Jmin`, `Jmax`.<br>3. Убедитесь, что UDP-порты не блокируются провайдером. |
| **Скрипт не скачивается** | 1. Используйте VPN для обхода блокировок.<br>2. Скачайте скрипт вручную: [warp_generator.sh](https://github.com/KnowerLife/VPN/raw/refs/heads/main/warp_generator.sh). |
| **Не удаётся подключиться** | 1. Проверьте правильность конфига.<br>2. Попробуйте другой сервер или порт.<br>3. Обновите клиент до последней версии. |

---

## Поддержка

- **Чат**: [Telegram](https://t.me/KnowerLifeBot)
- **Документация**:
  - [AmneziaWG](https://amnezia.org/)
  - [WireGuard](https://www.wireguard.com/)
  - [Cloudflare WARP](https://developers.cloudflare.com/warp/)
- **Обратная связь**: Если у вас есть предложения по улучшению скрипта или инструкции, напишите в чат или создайте issue на [GitHub](https://github.com/KnowerLife/VPN).

---

## Пример конфига

Пример конфигурации для WireGuard (чувствительные данные удалены):

```plaintext
[Interface]
PrivateKey = <your_private_key>
Address = 192.168.0.1/32
DNS = 1.1.1.1, 1.0.0.1

[Peer]
PublicKey = <cloudflare_public_key>
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = engage.cloudflareclient.com:2408
```

---

## Дополнительные замечания

- **Безопасность**: Перед выполнением скрипта проверьте его код на [GitHub](https://github.com/KnowerLife/VPN) для безопасности.
- **Ограничения**: Некоторые провайдеры могут блокировать WireGuard. В таком случае попробуйте альтернативные протоколы, такие как OpenVPN или Shadowsocks.
- **Обновления**: Регулярно проверяйте обновления скрипта и клиентов для совместимости.

---
