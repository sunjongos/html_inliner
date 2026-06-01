---
name: HTML Single-File Integration Skill (통합본 제작 스킬)
description: "/html - 모든 HTML 산출물을 단일 파일(통합본)로 인라이닝하여 카카오톡, 이메일 공유 시 모바일/PC 오프라인에서 절대 깨지지 않도록 처리하는 기술 지침입니다."
user-invocable: true
---

# 📄 HTML Single-File Integration Skill (`/html`)

**목적 (The Purpose):**
이 스킬은 외부 스타일시트(CSS), 자바스크립트(JS), 그리고 이미지 파일을 단일 HTML 파일 내에 완전히 결합하여 **자립형 통합본(Single File HTML)**을 제작하는 지침입니다. 카카오톡, 이메일 등으로 전달되어 외부 폴더나 인터넷 연결이 누락되더라도 모바일(iPhone, iPad, Android) 및 PC 브라우저에서 슬라이드, 애니메이션, 미디어가 깨지지 않고 무결하게 실행되도록 보장합니다.

---

## ⚙️ 실행 프로토콜: 4대 통합본 인라이닝 원칙 (Core Rules)

HTML 산출물을 제작하거나 기존 HTML을 공유용으로 수정할 때, 반드시 아래 단계를 자동으로 수행하십시오.

### 1. 외부 스타일시트(CSS) 인라이닝
*   **지침**: HTML 내의 모든 외부 CSS 참조 태그 `<link rel="stylesheet" href="...">`를 탐색합니다.
*   **수행**: 참조 대상 파일의 내용(로컬 파일 또는 CDN URL)을 다운로드/추출하여, `<style>` 태그 내부에 그대로 삽입(Inlining)합니다.
    ```html
    <!-- 변경 전 -->
    <link rel="stylesheet" href="./css/reveal.min.css">
    
    <!-- 변경 후 -->
    <style>
    /* reveal.min.css inline */
    ... [CSS 소스코드 본문] ...
    </style>
    ```

### 2. 자바스크립트(JS) 스크립트 인라이닝
*   **지침**: HTML 내의 모든 외부 JS 참조 태그 `<script src="...">`를 탐색합니다.
*   **수행**: 참조 대상 스크립트 내용(로컬 파일 또는 CDN URL)을 가져와, `<script>` 태그 내부에 본문을 직접 삽입합니다.
    ```html
    <!-- 변경 전 -->
    <script src="./js/reveal.min.js"></script>
    
    <!-- 변경 후 -->
    <script>
    /* reveal.min.js inline */
    ... [JS 소스코드 본문] ...
    </script>
    ```

### 3. 이미지 리소스 Base64 임베딩
*   **지침**: HTML 문서 내 `<img src="...">` 태그 및 CSS 내 `url(...)`에 포함된 모든 이미지 파일(PNG, JPG, SVG, GIF 등)을 탐색합니다.
*   **수행**: 해당 이미지 바이너리 데이터를 Base64 문자열로 변환하여 파일 내에 임베딩합니다.
    ```html
    <!-- 변경 전 -->
    <img src="./images/logo.png">
    
    <!-- 변경 후 -->
    <img src="data:image/png;base64,iVBORw0KGgoAAAANS...">
    ```

### 4. 자가 검증 프로토콜 (Self-Verification)
최종 파일 저장 전, 다음 검증 코드를 수행하여 외부 리소스 잔존 여부를 확인합니다.
*   **검증 항목**:
    *   `href="http..."` 또는 `src="http..."` (단, 외부 페이지 이동 단순 하이퍼링크 `<a>` 태그는 제외)가 존재하지 않는가?
    *   `href="./..."` 또는 `src="./..."` 같은 상대 경로가 남아있지 않는가?
    *   오프라인(비행기 모드) 상태로 시뮬레이션했을 때 기능 및 디자인이 100% 정상 작동하는가?

---

## 💾 장기공유메모리 자동 보존 및 원격 공유 규칙 (Long-Term Shared Memory & Multi-Luca Sync)
이 스킬의 정의 및 최종 통합 산출물은 로컬 저장 영역뿐만 아니라 3대의 루카(Luca) PC가 즉각 상호 동기화하여 사용할 수 있도록 **장기공유메모리**에 항상 이중 저장되어 공유됩니다.

1. **스킬 헌법 동기화**:
   이 `/html` 스킬의 `SKILL.md` 및 핵심 스크립트(`html_inliner.py`) 파일은 로컬 설치 경로 외에도 항상 장기공유메모리 내 동일 스킬 디렉터리에 실시간 반영하여 백업 및 공유합니다.
   *   **로컬 설치 경로**: `c:\Users\sunjo\Desktop\luca연구에이전트\.agent\skills\html\`
   *   **공유 메모리 경로**: `C:\Users\sunjo\Desktop\luca연구에이전트\장기공유메모리\luca_brain_memory\.agents\skills\html\`

2. **통합본 산출물 자동 공유 배포**:
   에이전트가 `/html` 스킬을 사용하여 생성한 최종 통합본 HTML 파일은 카카오톡이나 메일 발송 외에도, 다른 루카 컴퓨터에서도 바로 접근하여 열고 활용할 수 있도록 **장기공유메모리 공용 공간**에 동시에 복사/보존합니다.
   *   **산출물 공유 저장 공간**: `C:\Users\sunjo\Desktop\luca연구에이전트\장기공유메모리\luca_brain_memory\`
