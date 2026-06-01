# HTML Integrator (HTML Inliner) 📄📦

**HTML Integrator**는 웹페이지에 구성된 외부 리소스(CSS 스타일시트, Javascript 스크립트, 이미지 및 배경 에셋)를 자동으로 다운로드 및 추출하여 단일 HTML 파일 내부로 결합(Inlining)해주는 파이썬 유틸리티이자, AI 코딩 에이전트를 위한 **통합본 제작 스킬(Skill)** 패키지입니다.

이 도구를 사용하면 카카오톡, 이메일 공유 시 모바일(iPhone, iPad, Android) 및 PC 오프라인 브라우저 환경에서 에셋 유실이나 깨짐 현상 없이 언제 어디서나 정상 작동하는 **100% 자립형 무결성 통합본(Single File HTML)**을 즉시 빌드할 수 있습니다.

---

## 🎨 AI 에이전트 스킬로 설치 및 사용법 (Agent Skill Installation)

이 리포지토리는 AI 에이전트(Antigravity, Claude, Cursor 등)가 사용할 수 있는 스킬 구조(`SKILL.md` 포함)로 설계되어 있습니다. 다른 컴퓨터나 새로운 작업 공간에서 이 스킬을 다운로드받아 에이전트에게 지시하려면 아래 순서대로 수행하십시오.

### 1. 스킬 다운로드 (Git Clone)
작업 공간의 에이전트 스킬 디렉터리(`.agent/skills/`)로 이동한 후, 폴더명을 `html`로 지정하여 이 저장소를 복제합니다.

```bash
# 에이전트의 스킬 디렉터리 내부로 복제 (폴더명: html)
git clone https://github.com/sunjongos/html_inliner.git .agent/skills/html
```

### 2. 에이전트 실행 명령어 (`/html`)
스킬이 설치되면 에이전트에게 채팅창에 **/html** 슬래시 명령어를 사용하거나 아래와 같이 지시하여 대화를 시작할 수 있습니다.
> **지시 예시**: "이 HTML 파일을 카톡으로 보내도 안 깨지게 /html 스킬로 통합본 만들어줘."

---

## 🚀 파이썬 도구 단독 사용법 (Python CLI Usage)

에이전트 없이 단독 유틸리티 프로그램으로 수동 빌드하려는 경우에도 사용이 가능합니다.

### 1. 요구 사항
- Python 3.x 이상
- BeautifulSoup4 설치
  ```bash
  pip install beautifulsoup4
  ```

### 2. 실행 명령어
```bash
# 기본 사용법 (입력파일 경로 전달 시 [파일명]_integrated.html 형태로 저장됨)
python html_inliner.py "경로/파일명.html"

# 출력파일 이름을 수동으로 지정할 경우
python html_inliner.py "경로/입력파일.html" "경로/출력파일.html"
```

---

## ✨ 주요 기능
- **CSS Stylesheets 인라이닝**: `<link rel="stylesheet">` 태그를 파싱하여 내용을 `<style>` 태그로 자동 삽입합니다.
- **Javascript 인라이닝**: `<script src="...">` 태그의 스크립트 본문을 `<script>` 태그 내로 직접 변환 삽입합니다.
- **이미지 리소스 Base64 변환**: HTML 내 `<img>` 태그의 `src` 및 인라인 CSS의 `background-image: url(...)` 에셋을 자동으로 Base64 스트링(`data:image/...;base64`)으로 부호화하여 임베딩합니다.
- **로컬 & 원격 리소스 대응**: 로컬 경로의 파일뿐만 아니라, 외부 CDN(예: cdnjs, unpkg 등) 서버로부터 리소스를 실시간으로 다운로드하여 통합 결합합니다.
- **오프라인 완벽 구동**: 변환이 완료된 하나의 파일은 무선 네트워크나 통신망 연결이 완벽하게 차단된 오프라인 환경에서도 레이아웃 및 동적 애니메이션이 손상 없이 100% 정상 작동합니다.
