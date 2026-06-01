---
name: HTML Single-File Integration Skill (통합본 제작 스킬)
description: "/html - 모든 HTML 산출물을 단일 파일(통합본)로 인라이닝하여 카카오톡, 이메일 공유 시 모바일/PC 오프라인에서 절대 깨지지 않도록 처리하는 기술 지침입니다."
user-invocable: true
---

# 📄 HTML Single-File Integration Skill (`/html`)

**핵심 정의 (Core Concept):**
HTML(구조) + CSS(디자인) + JS(동작) + 이미지 파일(Base64 임베딩)을 단 하나의 HTML 파일에 통합(Inliner)하여 100% 자립형 통합본(Single File HTML)을 제작합니다. 카카오톡/이메일 배포 시 오프라인/모바일에서도 레이아웃 깨짐 현상 없이 고화질 슬라이드를 완벽하게 실행하기 위한 스킬입니다.

---

## ⚙️ 실행 프로토콜 (Execution Protocol)

에이전트가 `/html` 명령어를 받았을 때, 다음 단계를 순서대로 진행하십시오.

1. **외부 에셋 파일 파싱**:
   HTML 파일 내부에 포함된 `<link rel="stylesheet">`, `<script src="...">`, `<img>` 태그 및 CSS `url()` 구문을 추적합니다.

2. **단일 HTML 내로 인라이닝**:
   - 외부/로컬 CSS ➡️ `<style>` 태그 내에 소스 삽입
   - 외부/로컬 JS ➡️ `<script>` 태그 내에 스크립트 삽입
   - 이미지 에셋 ➡️ Base64 바이너리 인코딩 문자열(`data:image/...;base64`)로 인코딩하여 `src`에 직접 내장

3. **Inliner 도구 실행**:
   이 기능은 이 스킬 폴더 내부에 포함된 `html_inliner.py` 파이썬 스크립트를 사용하여 직접 수행할 수 있습니다.
   ```bash
   python html_inliner.py <입력_html_경로>
   ```

4. **검증**:
   출력된 `[파일명]_integrated.html` 파일에 어떠한 로컬/외부 링크 에셋도 남아있지 않고 독립 실행되는지 검증합니다.
