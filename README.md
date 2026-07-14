Lotto 추첨기
=================

간단한 로또(6/45) 번호 생성기입니다.

사용법:

```bash
python lotto.py -n 5        # 5개 티켓 생성
python lotto.py -n 3 -s 42  # 시드를 고정하여 재현 가능한 결과
```

생성된 각 티켓은 6개의 고유한 숫자(1~45)를 오름차순으로 출력합니다.

웹 UI 사용법:

1. 브라우저에서 [web/index.html](web/index.html) 파일을 여세요.
2. 생성 개수와 시드(선택)를 입력한 뒤 `번호 생성` 버튼을 누르세요.
3. `복사` 버튼으로 결과를 클립보드에 복사할 수 있습니다.

Supabase 연동:

1. Supabase 프로젝트를 만들고 `lotto_draws` 테이블을 생성합니다.
   - 컬럼 예시: `ticket_index` (integer), `seed` (text), `numbers` (integer[]), `formatted` (text)
2. Vercel 환경변수에 아래 값을 추가합니다.
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_TABLE_NAME` `lotto_draws` 권장
3. 이 저장소는 `/api/env.js`를 통해 Vercel 환경변수를 프론트에 주입합니다.
4. 웹 UI에서 번호를 생성한 뒤 `저장` 버튼을 누르면 DB에 기록됩니다.

로컬 개발용으로는 `.env.example` 파일을 참고해 `.env`를 구성하면 됩니다.
