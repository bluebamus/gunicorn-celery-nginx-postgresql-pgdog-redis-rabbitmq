"""
Gunicorn 설정 파일
- 웹 서버 성능을 제어하기 위한 파라미터 모음입니다.
- 공식 문서: https://docs.gunicorn.org/en/stable/settings.html
"""

# 서버 바인딩 주소 및 포트
bind = "0.0.0.0:8000"

# 워커 수 (CPU 수에 따라 조정)
workers = 4

# 스레드 수 (요청 병렬 처리용)
threads = 4

# 요청 처리 최대 시간
timeout = 60

# keep-alive 연결 시간
keepalive = 2

# 로깅 레벨 (debug, info, warning, error, critical)
loglevel = "info"

# worker class: sync(default), gevent, eventlet 등
# worker_class = "sync"

# access log 파일 경로 (기본: stdout)
# accesslog = "-"

# error log 파일 경로
# errorlog = "-"

# preload 앱 설정 (실행 전에 로딩하여 메모리 공유)
# preload_app = False

# 요청 제한 (DoS 방지)
# limit_request_line = 4094
# limit_request_fields = 100
# limit_request_field_size = 8190
