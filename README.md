# HTML Integrator (HTML Inliner) 📄📦

**HTML Integrator**는 웹페이지에 구성된 외부 리소스(CSS 스타일시트, Javascript 스크립트, 이미지 및 배경 에셋)를 자동으로 다운로드 및 추출하여 단일 HTML 파일 내부로 결합(Inlining)해주는 파이썬 유틸리티입니다.

이 도구를 사용하면 카카오톡, 이메일 공유 시 모바일(iPhone, iPad, Android) 및 PC 오프라인 브라우저 환경에서 에셋 유실이나 깨짐 현상 없이 언제 어디서나 정상 작동하는 **100% 자립형 무결성 통합본(Single File HTML)**을 즉시 빌드할 수 있습니다.

## ✨ 주요 기능
- **CSS Stylesheets 인라이닝**: `<link rel="stylesheet">` 태그를 파싱하여 내용을 `<style>` 태그로 자동 삽입합니다.
- **Javascript 인라이닝**: `<script src="...">` 태그의 스크립트 본문을 `<script>` 태그 내로 직접 변환 삽입합니다.
- **이미지 리소스 Base64 변환**: HTML 내 `<img>` 태그의 `src` 및 인라인 CSS의 `background-image: url(...)` 에셋을 자동으로 Base64 스트링(`data:image/...;base64`)으로 부호화하여 임베딩합니다.
- **로컬 & 원격 리소스 대응**: 로컬 경로의 파일뿐만 아니라, 외부 CDN(예: cdnjs, unpkg 등) 서버로부터 리소스를 실시간으로 다운로드하여 통합 결합합니다.
- **오프라인 완벽 구동**: 변환이 완료된 하나의 파일은 무선 네트워크나 통신망 연결이 완벽하게 차단된 오프라인 환경에서도 레이아웃 및 동적 애니메이션이 손상 없이 100% 정상 작동합니다.

## 🚀 사용법 (Usage)

### 1. 요구 사항
- Python 3.x 이상
- BeautifulSoup4
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

## 🛠️ 활용 예시
- **슬라이드 발표자료(Reveal.js 등) 공유**: 회의실 PC나 개인 태블릿(iPad, 갤럭시탭 등)에서 자료 폴더 누락 없이 파일 1개만 다운로드하여 완벽한 모션 발표 진행
- **카카오톡/이메일 배포**: 모바일 환경에서 사용자가 클릭만 하면 경고 없이 로딩 속도 지연 없이 즉시 브라우저로 뷰어 구동 가능
- **아카이빙**: 특정 시점의 웹 프로젝트나 뉴스레터 템플릿의 무결성 백업 보관
