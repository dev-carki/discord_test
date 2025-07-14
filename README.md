# Dependency
![Python](https://img.shields.io/badge/Python-3.10.18-3776AB?style=social&logo=python&logoColor=3776AB)
![Discord](https://img.shields.io/badge/Discord-2.3.2-3776AB?style=social&logo=discord&logoColor=#5865F2)
![Discord](https://img.shields.io/badge/Discord.py-2.5.2-3776AB?style=social&logo=discord&logoColor=#5865F2)

# Setup Process
## 1. Discord 서버 생성

디스코드 좌측의 `+`클릭 후 -> `직접 만들기` -> `나와 친구들을 위한 서버` -> 채널 이름 입력 후 `만들기` 버튼 클릭

<img width="" height="500" alt="스크린샷 2025-07-15 오전 2 41 48" src="https://github.com/user-attachments/assets/99bdb3d8-1d33-4d16-b9e4-9be851293d0f" />

## 2. 봇 생성
### 1. [Discord 개발자 포털][gdh]로 이동 후 우측 상단의 `New Application` 클릭

[gdh]: https://goddaehee.tistory.com

<img width="2153" height="489" alt="스크린샷 2025-07-15 오전 1 31 39" src="https://github.com/user-attachments/assets/cf6ae171-6d09-4008-92fd-b309707ec5c4" />

### 2. 생성할 Application Name 입력 후 `Create` 클릭

<img width="505" height="325" alt="스크린샷 2025-07-15 오전 1 35 16" src="https://github.com/user-attachments/assets/6658545c-3e69-4695-8dca-4227cbd17ee9" />

### 3. 서버와 Bot 연결

#### 1. 좌측 `Settings`에서 `OAuth2`를 클릭하고 `SCOPES`에서 `bot`을 체크, `BOT PERMISSIONS`에서는 `Administrator`를 체크
<img width="1771" height="1060" alt="스크린샷 2025-07-15 오전 1 39 30" src="https://github.com/user-attachments/assets/3392eb34-ea33-4838-9952-d3baac906720" />

#### 2.하단에 생성된 URL을 `Copy`.
<img width="1365" height="93" alt="스크린샷 2025-07-15 오전 1 42 27" src="https://github.com/user-attachments/assets/9962d557-909d-49e3-b3b2-75601ab00f70" />

#### 3. Copy 한 URL을 브라우저에 붙여 넣고 해당 주소로 이동하면 Bot과 연결하는 안내 창이 활성화됨, 그 후 `계속하기`, `승인`을 클릭하여 서버와 Bot을 연결

#### 4. Bot 초대 상태 확인
<img width="322" height="59" alt="스크린샷 2025-07-15 오전 1 53 02" src="https://github.com/user-attachments/assets/5ad953fe-c2e3-47df-8f9a-171dd6647691" />

## 3. Bot TOKEN 확인
### 1. TOKEN 복사
처음 Bot을 만들때 `TOKEN`값을 저장하지 않았다면 `Reset Token`을 클릭하여 TOKEN값을 재생성

`Yes, do it`을 클릭 후 `패스워드` 입력 후 토큰값 새로 생성 후 `Copy`를 클릭하여 복사

<img width="1992" height="1000" alt="스크린샷 2025-07-15 오전 1 55 26" src="https://github.com/user-attachments/assets/8f71d938-1264-4c87-9f89-1bb1b7378bae" />

<img width="735" height="139" alt="스크린샷 2025-07-15 오전 2 00 39" src="https://github.com/user-attachments/assets/81624f9a-7c1c-49cd-a964-0ab7f7f166b1" />

## 4. Privileged Gateway Intents 권한 설정

Bot이 메시지를 발신하기 위해서는 권한 설정이 필요한데, 

`Privileged Gateway Intents` 영역에 `Message Content Intent`토글을 활성화한 후 `Save Changes`를 클릭.

<img width="1996" height="1043" alt="스크린샷 2025-07-15 오전 2 07 48" src="https://github.com/user-attachments/assets/5bb3a055-8aae-4ba5-bb62-8da9fcd20ab9" />

## 5. Discord Channel ID 확인
### 1. 개발자 모드 활성화

톱니바퀴(사용자 설정) 클릭 후 -> 앱 설정의 고급 선택 -> 개발자모드 토글 활성화

채팅 채널 `# 일반` 우클릭 후 `ID 복사하기` 클릭

<p align="center">
<img width="" height="400" alt="스크린샷 2025-07-15 오전 2 25 44" src="https://github.com/user-attachments/assets/a37017c2-6723-4a2e-81c0-983473f9fd02" />


<img width="" height="400" alt="스크린샷 2025-07-15 오전 2 28 52" src="https://github.com/user-attachments/assets/e99f725a-1014-4ed0-b84e-db80654b201d" />

<img width="" height="400" alt="스크린샷 2025-07-15 오전 2 37 55" src="https://github.com/user-attachments/assets/a1b8d914-440f-4b55-ad41-8a752967bbd2" />

</p>

## 6. Discord 패키지 설치

```Shell
pip install discord
```

## 7. 채널에 메시지를 전송하는 기능의 샘플 코드
```python
import discord
import constants as const # constant 관리 패키지 (없어도 됨)

class ClientSample(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(const.CHANNEL_ID)) # Here is important! -> const.CHANNEL_ID에 Bot이 메시지를 보낼 CHANNEL_ID를 넣어준다
        await channel.send("Hello, I'm Bot :)")
 
 
intents = discord.Intents.default()
intents.message_content = True
client = ClientSample(intents=intents)
client.run(const.TEST_TOKEN)  # Here is important! -> const.TEST_TOKEN에 Bot TOKEN 값을 넣어준다
```

<img width="202" height="65" alt="스크린샷 2025-07-15 오전 2 21 41" src="https://github.com/user-attachments/assets/6c5b1910-3c8c-43ea-a5f5-9eb44cc5f86d" />
