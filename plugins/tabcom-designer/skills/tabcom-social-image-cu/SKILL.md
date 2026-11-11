---
name: tabcom-social-image-cu
description: BẢN CŨ — quy trình BÁM MẪU. Tạo ảnh social Tabcom bằng cách tìm mẫu nước ngoài trên Pinterest (hoặc mẫu người dùng gửi), phân tích 8 khía cạnh, giữ bố cục mẫu, đổi 3 "dấu vân tay", áp nhận diện Tabcom, gọi Codex render 1 lần rồi soát. Dùng khi người dùng nói "skill cũ", "bản cũ", "làm theo kiểu cũ", "bám mẫu", "biến ảnh này thành của Tabcom", hoặc gửi một mẫu cụ thể để chuyển thành Tabcom. Quy trình ý tưởng trước (brainstorm) nằm ở skill tabcom-social-image-moi.
---

# Tabcom social image — BẢN CŨ (bám mẫu)

> Bản mới (ý tưởng trước, brainstorm 8–10 ý): skill `tabcom-social-image-moi`.

Prompt mẫu của người dùng:
`Giúp tôi tạo hình ảnh [dạng A/B] cho bài viết có nội dung/tiêu đề sau [nội dung] [tỷ lệ nếu có]`

Luồng **dừng người dùng đúng 1 lần**: đưa 3–5 mẫu Pinterest để người dùng chọn (A2). Chọn xong thì chạy thẳng tới ảnh hoàn thiện
(chỉ có 1 điểm chuyển nội bộ: A3a phân tích song song do phiên chính chạy). Bàn giao kèm phân tích và mẫu gốc.
Người dùng gửi kèm một mẫu cụ thể ("biến ảnh này thành của Tabcom") → bỏ A2, dùng mẫu đó.

**Những việc người dùng đã dặn nhiều lần — không được quên:**
1. Prompt gửi Codex **luôn có khối DESIGN QUALITY RULES** (nguyên tắc thiết kế cốt lõi), kể cả khi bám mẫu.
2. Trước khi bàn giao **luôn chấm ảnh theo nguyên tắc cốt lõi (A7.2) bằng số đo**, không chỉ soát chính tả/nhận diện.
3. **Mẫu người dùng gửi đã hoàn hảo, không rối.** Ảnh ra bị rối là do mình đọc sai cách họ làm rồi **phóng đại**
   (mẫu có 2–3 thứ thì mình làm thành 5–6, mẫu mờ dịu thì mình làm to rực). Mọi phần tử trong prompt phải
   **≤ mẫu về số lượng và ≤ mẫu về cường độ** (kiểm đếm ở A3, soát ở A5b). Không "bỏ bớt" thứ của mẫu với lý do mẫu rối.
4. **Mỗi ấn phẩm chỉ render 1 lần.** Mọi khâu soát làm trên prompt (A5b) **trước** khi render. Không render → soát → render lại.
   Sau render: soát để báo cáo, lỗi nhỏ trên nền trơn sửa bằng code; render lại chỉ khi người dùng yêu cầu.
5. **Logo, SĐT, domain đặt theo đúng bản gốc**: mẫu đặt thông tin thương hiệu ở đâu, cỡ bao nhiêu % khung, trong hình khối gì
   (tab, dải chân trang, ô trắng…) thì làm y vậy, chỉ thay nội dung + màu. Codex vẽ luôn; chỉ sửa bằng code nếu vẽ sai logo/số.
   Không tự sáng tác vị trí mới, không ép chân trang Tabcom.
6. **Nhân vật người Việt phải mô tả cụ thể ngay trong prompt** (gương mặt, nước da, tóc + câu cấm "NOT South Asian…").
   Chỉ ghi "Vietnamese" thì Codex bám người mẫu trong ảnh gốc (ảnh 5: ra người Nam Á).
7. **Tránh bị coi là copy bằng bước A3c "Dấu vân tay"**: đổi 3 chi tiết nhận ra được theo kiểu 1-đổi-1, không thêm.
8. **KHÔNG đính kèm ảnh mẫu khi gửi Codex** (người dùng chốt 03/11/2026). Ảnh mẫu chỉ dùng để phân tích (A3). Lần render
   chỉ gửi `prompt.md` + logo. Đính kèm mẫu thì Codex chép ~95% bản gốc (lỗi đã gặp ở bài "đơn hoàn mất ship 2 chiều").
   Vì vậy prompt phải **tự mô tả đủ** bố cục, lớp, trục, khoảng trống, cường độ — không có câu "like image 1".

**Nguồn quy tắc (đọc trước mỗi lần làm):**
- `${CLAUDE_PLUGIN_ROOT}/brand/TABCOM-BRAND-VISUAL-GUIDELINE.md` — nhất là **mục 0 (quy tắc cứng)**, mục 4 (màu),
  mục 10 (nguyên tắc thiết kế có số đo). Mục 0 thắng mọi mục khác.
- `${CLAUDE_PLUGIN_ROOT}/docs/huong-dan-design-co-ban.md` — kiến thức design chung
  (phân cấp, căn gióng, xa gần, chữ, màu, hình, đường; bảng số chuẩn mục 0; checklist mục 8). Dùng để phân tích mẫu (A3)
  và đối chiếu ảnh (A7).

Đường dẫn dùng chung (viết tắt `BRAND` = `${CLAUDE_PLUGIN_ROOT}/brand`, `SK` = thư mục skill này):
- Logo trắng: `${CLAUDE_PLUGIN_ROOT}/assets/logos/tabcom-white-green-transparent.png`
- Logo navy (nền sáng): `${CLAUDE_PLUGIN_ROOT}/assets/logos/tabcom-navy-green-transparent.png`
- Vẽ phác thảo: `BRAND/wireframe/render_wireframe.py`
- Thư mục bàn giao: `outputs/hinh-anh/yy.mm.dd - <ten-bai-khong-dau>/`

**Cần có trên máy:** [Codex CLI](https://github.com/openai/codex) đã đăng nhập (lệnh `codex`, dùng để tạo ảnh), Python 3.10+ với `pip install pillow numpy`; bản cũ cần thêm Pinterest MCP (`npm i -g pinterest-mcp-server`). Thiếu gì thì báo người dùng cài trước. Thư mục `outputs/` tính từ thư mục đang làm việc, không ghi vào thư mục plugin.

## Dạng B — Case study

Chưa có quy trình. Người dùng sẽ hướng dẫn sau (có mẫu riêng). Nếu được gọi Dạng B: báo người dùng là chưa cài,
hỏi họ có muốn hướng dẫn ngay không. **Không tự chế quy trình.**

## Dạng A — Banner chủ đề

### A1. Đọc yêu cầu
- Nội dung/tiêu đề bài → viết **1 câu thông điệp** + **tiêu đề trên ảnh ≤ 8 từ** (tiếng Việt nói tự nhiên: câu ngắn, động từ
  mạnh, không danh từ hoá kiểu dịch từ tiếng Anh) + tối đa 1 dòng phụ + CTA nếu hợp (mặc định "Nhận tư vấn miễn phí →").
- Sàn của bài: Shopee hay TikTok Shop (quy tắc mục 0.4 — màn hình chỉ được là sàn đó).
- Tỷ lệ: theo prompt; mặc định 1:1. Cỡ xuất: 1:1 → 1080x1080 · 4:5 → 1080x1350 · 3:4 → 1080x1440 · 9:16 → 1080x1920 · 16:9 → 1920x1080.

### A2. Tìm mẫu trên Pinterest
- Từ khoá mặc định: `Ecommerce service social design`. Thêm 1 lượt tìm từ khoá tiếng Anh theo chủ đề bài
  (vd. "online store growth social media post", "livestream selling banner design").
- Công cụ: `mcp__pinterest__pinterest_search_and_download` (keyword, limit 12, headless true) — ảnh lưu vào `outputs/pinterest-refs/<keyword>/`.
  Nếu công cụ MCP chưa có trong phiên: `node SK/scripts/pinterest_search.cjs "<keyword>" 12 "outputs/pinterest-refs"`.
- Xem từng ảnh (Read). **Loại**: poster/banner Việt Nam (chữ tiếng Việt, thương hiệu Việt) · màu neon · thẻ nổi 3D (3D floating card) ·
  quá rối/nhiều chữ · không hợp tỷ lệ yêu cầu (trừ khi bố cục dễ chuyển).
- **Ưu tiên** mẫu có: phân cấp 3 bậc rõ; **chiều sâu** (vật ở góc tràn mép, có người hoặc tay thật, xếp lớp chữ–hình, sàn/sân khấu).
  Mẫu quá tối giản, phẳng (ít lớp, ít vật) dễ cho ra ảnh flat — nếu đưa vào danh sách thì ghi rõ điểm yếu này.
- Lọc còn **3–5 ứng viên**, ghép thành 1 ảnh tờ liên hệ có đánh số, mở cho người dùng xem kèm 1 dòng/ứng viên
  (bố cục gì, hợp bài ở điểm nào). **Dừng, chờ người dùng chọn.** Không tự audit AI — người dùng tự chọn mẫu.
- Mẹo tìm mẫu do người thật thiết kế: thêm "behance" hoặc "dribbble" vào từ khoá (vd. `ecommerce agency social media post behance`).
- Người dùng chọn xong → copy mẫu vào thư mục bàn giao `ref-source.jpg`, chạy tiếp A3.

### A3. Phân tích mẫu + kiểm đếm + kế hoạch biến tấu (bắt buộc, trước khi viết prompt)

**A3a. Phân tích song song bằng 8 agent (người dùng yêu cầu, để soi kỹ từng điểm).**
Phiên chính (không phải agent con — agent con không gọi được agent khác) chạy **8 agent `tabcom-ref-analyst` song song trong
một lượt**, mỗi agent một khía cạnh: `phan-cap` · `xep-lop-chieu-sau` · `can-giong` · `xa-gan` · `khoang-trong` · `chu` · `mau` ·
`hinh-duong-kiem-dem`. Prompt mỗi agent: khía cạnh + đường dẫn `ref-source.jpg` + thư mục bàn giao + chủ đề bài.
Kết quả: `<thư mục>/analysis/<khía cạnh>.md`.
- Nếu đang chạy trong agent `tabcom-designer`: sau khi người dùng chọn mẫu và đã copy `ref-source.jpg`, **dừng và báo phiên chính**
  "Cần chạy A3a: 8 agent tabcom-ref-analyst cho <thư mục>". Phiên chính chạy xong thì gửi lại cho designer làm tiếp A3b.

**A3b. Tổng hợp** 8 file thành `phan-tich-mau-goc.md`. Chỗ các agent mâu thuẫn
thì mở ảnh kiểm lại. File tổng hợp gồm 8 mục dưới đây + bảng kiểm đếm + bảng chuyển sang Tabcom:
1. **Phân cấp**: bậc 1–4 là gì, vì sao nổi (cỡ, sáng, lớp, màu); tỷ lệ cỡ chữ giữa các bậc.
2. **Xếp lớp & chiều sâu**: thứ tự lớp từ sau ra trước (chữ nằm lớp nào; vật nào đè lên chữ); vật tràn mép; sàn/bóng đổ; vật mờ.
3. **Căn gióng**: có mấy trục, nằm ở đâu, khối nào bám trục nào; góc xoay chung.
4. **Xa gần**: nhóm nào đứng sát nhau, khoảng giữa nhóm.
5. **Khoảng trống**: ~bao nhiêu % trống, nằm ở vùng nào.
6. **Chữ**: số họ font, độ đậm ghép thế nào, in hoa/thường, khoảng dòng.
7. **Màu**: họ màu nền, **số màu nhấn và nằm ở đâu**, màn hình cùng tông hay khác tông.
8. **Hình & đường**: đạo cụ, người, màn hình, đường dẫn mắt.

**Bảng kiểm đếm (bắt buộc)** — mỗi loại phần tử của mẫu: số lượng · chiếm bao nhiêu % khung · độ mờ · tương phản với nền ·
độ rực màu. Ví dụ: "vật bay: 3, mỗi vật < 5% khung, mờ nặng, tương phản thấp, màu dịu". Đây là **trần** cho prompt.

**Bảng chuyển sang Tabcom** — từng yếu tố "mẫu gốc → Tabcom":
- **Giữ**: bố cục, thứ tự lớp, trục, khoảng cách, khoảng trống, kiểu chữ, logic màu, năng lượng — và **giữ nguyên cường độ**.
- **Màu**: họ màu nền của mẫu → một họ màu Tabcom; **số màu nhấn giữ đúng như mẫu** (mẫu 1 màu nhấn → Tabcom 1 màu nhấn,
  thường là teal hoặc cam); mọi thứ khác về trung tính (trắng kem, xanh cùng họ nền). Không để màu thương hiệu (cam…)
  rải thêm thành điểm nhấn mới. Cam Shopee nằm trong màn hình thì được.
- **Bỏ (mục 0.5)**: mọi logo, tên thương hiệu, SĐT, email, web, QR, handle của mẫu; thẻ nổi 3D (mục 0.3).
- **Biến tấu bắt buộc (mục 0.8)** — liệt kê cụ thể:
  - nhân vật mới người Việt: giới tính/tuổi, kiểu tóc, gương mặt, trang phục **khác mẫu**, tư thế giữ tinh thần mẫu;
  - thay **≥ 2 đạo cụ/item** bằng thứ hợp nội dung bài và ngành TMĐT Việt;
  - màn hình → giao diện Shopee hoặc TikTok Shop với nội dung hợp bài;
  - màu → bộ màu Tabcom (không neon);
  - nhận diện: logo (trắng trên nền đậm, navy trên nền sáng), `0786.668.222`, `tabcomgroup.vn` **đặt đúng chỗ, đúng cỡ
    (đo % khung: rộng logo, cao dải chân trang, cỡ chữ) và đúng hình khối** như mẫu đặt logo/thông tin liên hệ. Ghi số đo vào bảng.
- **Sửa lỗi thiết kế của mẫu** (nếu có) theo mục 10 — chỉ sửa lỗi rõ ràng, không đổi phong cách.

**A3c. Dấu vân tay (tránh bị coi là copy)** — thêm bảng vào `phan-tich-mau-goc.md`:
1. Liệt kê các chi tiết **nhìn thấy là nhận ra mẫu** (dáng/tư thế người, đồ ngồi, khối nổi/vệ tinh, phông nền, hướng bố cục,
   nhãn nghiêng, dấu nhấn lớn…). Logo/SĐT/domain **không** tính vào đây (giữ đúng kiểu mẫu, quy tắc 5).
2. Chọn **3** chi tiết để đổi, mỗi chi tiết **1-đổi-1**: cùng số lượng, cùng % diện tích, cùng độ sáng/độ mờ, cùng vai trò
   (ví dụ 4 khung laptop mờ ~9% → 4 hộp đơn trên kệ, tối, ~9%). Đổi chứ không thêm.
3. Không đụng phần đo được: khoảng trống, phân cấp độ sáng, số màu nhấn, trục, các trần kiểm đếm.
4. Đổi hướng bố cục → viết thẳng bố cục đã lật vào prompt (vật nào bên trái/phải, toạ độ gần đúng). Không đính kèm ảnh mẫu (quy tắc 8).
   Đổi dáng người → mô tả dáng mới + câu cấm dáng cũ ("do NOT raise an arm behind her head…").
Bảng: `chi tiết mẫu · đổi thành · giữ trần (số lượng / % / độ sáng)`.

### A4. Phác thảo whiteboard bằng code (không gọi AI)
Viết `brief.json` (định dạng như `BRAND/wireframe/example-v7-brief.json`; `canvas` = cỡ xuất) rồi:
`python -I "BRAND/wireframe/render_wireframe.py" brief.json wireframe.png`. Xem lại wireframe; sửa chỗ chồng chéo.

### A5. Viết prompt cho Codex (`prompt.md`, tự đủ)
Codex **chỉ tạo ảnh**, không đọc file, không chạy lệnh. **Ảnh đính kèm duy nhất là logo (image 1)** — không kèm ảnh mẫu (quy tắc 8).
Cấu trúc bắt buộc:
- `COMPOSITION`: phân cấp, thứ tự lớp, trục, khoảng cách, kiểu chữ, khoảng trống, logic màu — viết từ bảng phân tích A3,
  kèm cường độ (nhỏ/mờ/dịu) đúng như mẫu, **mô tả bằng chữ + toạ độ gần đúng**, không nhắc tới ảnh mẫu.
- `TABCOM ADAPTATION`: màu (mã HEX, ghi rõ **màu nhấn duy nhất** và chỗ dùng), người, đạo cụ, màn hình, logo.
  **Người Việt mô tả cụ thể**: tuổi, gương mặt Việt / Đông Á (mặt trái xoan mềm, mắt một mí hoặc hai mí nhẹ, sống mũi thấp nhỏ),
  da sáng tông ấm, tóc đen; câu cấm "She must NOT look South Asian, Indian, Middle Eastern or Western".
- `BRAND` (logo + liên hệ): vị trí, cỡ (% khung, quy ra px) và hình khối **chép từ số đo mẫu**, ví dụ "footer strip ONLY ≈ 50 px
  = 4.7% of the height".
  **Liệt kê đủ mọi vật được có, kèm số lượng**, và câu "no other objects".
- `TEXT`: từng dòng, đúng dấu, vị trí/cỡ gần đúng; chữ có dấu khó (Ậ, Ọ, Ă…) ghi tách từng ký tự.
- `DESIGN RULES`: thứ tự đọc, tỷ lệ cỡ, trục căn, vùng phải trống, chồng lớp được phép, lề chữ ≥ 64 px.
- Vị trí: dùng ngôn ngữ khung hình kèm toạ độ **gần đúng**. Không viết spec từng pixel (model không theo, dễ tự mâu thuẫn).
- **Khung (framing)**: chữ luôn nằm trong lề. **Vật ở góc được tràn mép nếu mẫu làm vậy** (đó là cách mẫu tạo chiều sâu);
  không ép mọi vật nằm trọn trong khung khi mẫu không làm thế.

### A5b. Soát prompt chống rối (bắt buộc, trước khi gửi Codex)
Đọc lại prompt, so với bảng kiểm đếm A3 và file hướng dẫn design:
- [ ] Không phần tử nào **nhiều hơn** mẫu (số vật, số khối chữ, số dòng, số con số trên màn hình).
- [ ] Không phần tử nào **to hơn / rực hơn / nét hơn** mẫu (vật mờ vẫn mờ, vệt sáng vẫn nhẹ, màn hình không dày số liệu hơn mẫu).
- [ ] Số màu nhấn = số màu nhấn của mẫu; ≤ 5 màu.
- [ ] Phân cấp 3 bậc rõ; bậc 2 không giành bậc 1.
- [ ] Khoảng trống tương đương mẫu; vùng trống được ghi rõ.
- [ ] Mọi khối chữ (không xoay) chung trục như mẫu; lề chữ ≥ 64 px.
- [ ] **Nhân vật**: có mô tả gương mặt/nước da/tóc Việt + câu cấm; dáng khác mẫu nếu dáng nằm trong 3 dấu vân tay.
- [ ] **Dấu vân tay**: đủ 3 chi tiết đã đổi, mỗi cái ghi rõ số lượng / % / độ sáng bằng cái cũ; đổi hướng thì đã viết bố cục lật trong prompt.
- [ ] **Không đính kèm ảnh mẫu**; prompt không còn câu "image 1 = source / like image 1"; image 1 chính là logo.
- [ ] **Logo, SĐT, domain**: vị trí, cỡ (%), hình khối đúng số đo mẫu; không phóng to (lỗi đã gặp: footer dày gấp đôi mẫu).
- [ ] **Số liệu trong prompt không tự mâu thuẫn**: toạ độ các khối không chồng nhau (người vs vệ tinh vs chữ); khoảng thở
      giữa tiêu đề và người ghi bằng vị trí đỉnh đầu cụ thể; tổng các khoảng cộng lại khớp khung.
- [ ] Không còn câu nào thừa từ prompt cũ (vd. "orange inside screen" khi đã bỏ màn hình).
Có mục không đạt → sửa prompt rồi mới gửi. **Đây là lần soát cuối — sau bước này chỉ render 1 lần.**

Khung prompt cũ (chỉ lấy phần TEXT/BRAND/DESIGN QUALITY RULES; dòng STYLE SOURCE đã bỏ — không kèm ảnh mẫu, logo là image 1):

```
Generate ONE image with your image generation tool. Do not read any files, do not run any shell commands, do not write code. Just call image generation once with the brief below, then reply "done".

=== IMAGE BRIEF ===
<Tỷ lệ + cỡ>, social media post for "Tabcom", a Vietnamese agency that runs Shopee and TikTok Shop stores.
<Nếu tỷ lệ ≠ ảnh Codex xuất (1:1 hoặc 2:3/3:2): "Compose for <tỷ lệ>; keep every important element inside the central <tỷ lệ> area; extend only background beyond it.">

COMPOSITION: <mô tả đầy đủ bố cục, lớp, trục, khoảng trống, cường độ — viết từ phân tích A3, không nhắc ảnh mẫu>

SCENE:
- Person: <nhân vật Việt mới — tóc, mặt, trang phục khác mẫu>
- Items: <item mẫu> → <item mới>, <item mẫu> → <item mới>
- Screen: <Shopee/TikTok Shop UI, nội dung>
- Background/colours: <màu Tabcom cụ thể bằng mã HEX>
- Remove everything from the source brand: logos, names, phone numbers, emails, websites, QR codes.

TEXT (spell EXACTLY with every Vietnamese diacritic; only these texts):
<từng dòng chữ, ghi rõ kiểu chữ/màu/vị trí, ngắt dòng>

BRAND:
- Tabcom logo exactly as attached image 1 (<trắng/navy>), at <vị trí>; small and clean.
- Contacts "0786.668.222" and "tabcomgroup.vn" at <vị trí theo mẫu>, clean sans, small simple icons.

DESIGN QUALITY RULES (apply inside the source style):
- Hierarchy: ONE dominant element (<phần tử chính, thường là tiêu đề>); everything else clearly smaller; contacts smallest but readable.
- Alignment: all text blocks share as few alignment edges as possible (one shared left edge, or the source's single axis); same rotation angle.
- Readability: no object, hand, hair or screen overlaps any text; white text only on dark areas; text colours exactly as given.
- Proximity: related items close together; unrelated groups separated by clear empty space (at least ~50 px), the headline never squeezed against objects.
- Spacing: objects never touch each other, text, faces or screens; even spacing; repeated elements share one style.
- FRAMING / margins: every text block at least ~64 px from the edges. Objects follow the source framing: if the source lets a
  corner object or a forearm bleed off the edge, keep that; otherwise keep objects inside the frame.
- Max 5 colours plus natural product colours. NO neon colours, NO glow.
- NO 3D floating card effect: UI cards are flat or inside real devices.
- Screens show only Shopee or TikTok Shop interfaces.
- People are Vietnamese / East Asian.
- Simplicity: nothing beyond the listed elements.
```

### A6. Tạo ảnh — chỉ 1 lần
```
python -I "SK/scripts/codex_image.py" --prompt prompt.md --out codex.png --size <WxH> --image <logo trắng hoặc navy>
```
Script in token đã dùng, số lần tạo ảnh (phải = 1), số lệnh shell (phải = 0), % hạn mức Codex.
**Không chạy 2 lệnh Codex song song** (script nhận nhầm phiên).

1. Render **1 lần** → soát A7 → ghi `doi-chieu.md`: bảng "quy tắc · ảnh đang thế nào (số đo) · cách xử lý".
2. Lỗi vị trí nhỏ trên **nền trơn** (lệch trục, lề thiếu, logo to quá, sai số/logo) → sửa bằng code trên ảnh.
3. Lỗi bố cục/hình/nhân vật → **không tự render lại**: bàn giao kèm danh sách lỗi + đề xuất, người dùng quyết.
   Ghi lỗi đó thành một dòng soát mới ở A5b để lần sau chặn từ prompt.

### A7. Tự soát (bắt buộc trước khi bàn giao — cả 2 phần)

**A7.1 Nhận diện & quy tắc cứng** — `python -I "SK/scripts/qa_measure.py" final.png` (nền trơn: lề mỗi phía ≥ 48 px;
nền phức tạp `busy_background`: soát lề bằng mắt), rồi xem ảnh (Read) và kiểm từng mục:
  - [ ] Chính tả tiếng Việt đúng từng dấu; không chữ lạ ngoài danh sách; dấu thanh không tách rời thành ký tự lạ.
        **Soát trên ảnh crop phóng to ≥ 2 lần** từng khối chữ, không kết luận từ ảnh thu nhỏ (dấu nặng của chữ to
        nằm sát dòng dưới, nhìn nhỏ dễ tưởng là vết lạ).
  - [ ] Logo Tabcom đúng (chữ + biểu tượng α bạc hà); SĐT, web đúng từng số.
  - [ ] Không còn dấu vết thương hiệu/thông tin của mẫu gốc.
  - [ ] Màn hình chỉ là Shopee/TikTok Shop.
  - [ ] Người Việt/châu Á; khác mẫu rõ (mặt, tóc, trang phục) và ≥ 2 item đã thay.
  - [ ] Không neon, không glow, không thẻ nổi 3D.

**A7.2 Nguyên tắc thiết kế cốt lõi** (guideline mục 10) — đo bằng pixel trên `final.png` (crop vùng chữ, tìm mép, lấy màu),
ghi bảng kết quả vào `notes.md` và báo người dùng:

| Nguyên tắc | Đo gì | Đạt khi |
|---|---|---|
| Phân cấp | Kích thước khối chữ/hình chính vs phần còn lại | Đúng 1 thứ áp đảo; tiêu đề đọc được trong 1 cái liếc; không 2 khối cùng tranh |
| Căn lề | Mép trái (hoặc trục) từng khối chữ | Lệch ≤ 8 px trong cùng nhóm; số trục căn ≤ 2 |
| Lề / khung | Khoảng cách chữ tới 4 mép | Chữ ≥ 64 px mỗi phía; vật chỉ tràn mép khi mẫu cũng tràn mép ở đúng chỗ đó |
| Không phóng đại | So từng loại phần tử với bảng kiểm đếm A3 | Số lượng, cỡ, độ rực, độ nét ≤ mẫu; số màu nhấn = mẫu |
| Trắng đen | Bản grayscale | Bậc 1 nổi nhất; chữ tách khỏi nền; trang trí chìm nhất |
| Gần nhau | Khoảng trống giữa các nhóm không liên quan | ≥ 48 px; trong nhóm sát nhau, đều nhau |
| Tương phản | Tỉ lệ WCAG chữ/nền (lấy màu thật trên ảnh) | Chữ thường ≥ 4,5:1; chữ lớn/đậm ≥ 24 px ≥ 3:1; màu chữ đúng mã yêu cầu |
| Màu | Đếm màu thiết kế (không tính màu tự nhiên da/vải/sản phẩm) | ≤ 5; không neon; đúng bộ màu Tabcom |
| Hướng / đường nét | Hướng xếp các khối, mũi tên, biểu đồ | Tăng trưởng đi lên/sang phải; không đi xuống khi thông điệp tích cực |
| Lặp lại | Kiểu nhãn, bo góc, icon, font | Cùng loại thì cùng style; ≤ 3 kiểu chữ |
| Đơn giản | Phần tử ngoài danh sách prompt | Không có phần tử thừa, không đạo cụ trang trí vô nghĩa |
| Cỡ chữ | Chiều cao chữ nhỏ nhất (ngoài UI trong màn hình) | ≥ 22 px ở khổ 1080 |

- Lỗi (A7.1 hoặc A7.2) → xử lý theo A6 (code nếu nền trơn; còn lại báo người dùng, không tự render lại).
- Soát thêm gương mặt nhân vật trên ảnh crop phóng to: đúng người Việt.

### A8. Bàn giao
Thư mục `outputs/hinh-anh/yy.mm.dd - <ten-bai>/`: `final.png`, `codex.png` (bản render gốc),
`ref-source.jpg` (chỉ để lưu, không gửi Codex), `phan-tich-mau-goc.md` (có bảng dấu vân tay), `prompt.md`, `doi-chieu.md`,
`wireframe.png`, `brief.json`. Mở `final.png` cho người dùng xem. Báo ngắn gọn: thông điệp đã chọn, mẫu đã dùng,
3 dấu vân tay đã đổi, sửa gì bằng code, mục A7.2 chưa đạt (nếu có), token đã dùng.
