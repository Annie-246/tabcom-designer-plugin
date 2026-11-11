# Tabcom — Brand Visual Guideline

Trích từ 49 thiết kế carousel/bài đăng chính thức của Tabcom (02/11/2026). Mã màu đo trực tiếp trên file, không ước lượng bằng mắt.

**Dùng file này thế nào:** khi nhận một thiết kế mẫu bất kỳ (của đối thủ, Pinterest, template Canva…),
agent giữ bố cục/ý tưởng của mẫu, thay **nội dung** nhận diện (logo, SĐT, domain đặt đúng chỗ và đúng kiểu mẫu đặt — mục 0.1b)
và **bộ màu** theo file này. Tạo ảnh theo **quy trình chuẩn ở mục 11**; cuối file có checklist đối chiếu.

Máy đọc: [brand-tokens.json](brand-tokens.json) · Bảng màu: [tabcom-palette.png](tabcom-palette.png) ·
Thành phần cắt sẵn: [components/](components/)

---

## 0. QUY TẮC CỨNG (ưu tiên cao nhất — đè lên mọi mục bên dưới)

Áp cho mọi ảnh social Tabcom (skill `tabcom-social-image-cu`). Mục nào bên dưới mâu thuẫn thì theo mục 0.

1. **Chỉ cố định 4 thứ**: logo Tabcom, `0786.668.222`, `tabcomgroup.vn`, bộ màu cơ bản (mục 4, trừ màu neon).
   File này chỉ là guideline cơ bản về màu sắc, ngành hàng, hình ảnh — **không có khung nhận diện cố định**.
   Tab logo và dải chân trang ở mục 2–3 chỉ là một kiểu tham khảo, không bắt buộc.
1b. **Logo, SĐT, domain đặt theo đúng bản gốc** (người dùng chốt 02/11/2026): mẫu đặt logo / thông tin liên hệ ở đâu, cỡ bao
   nhiêu (đo % khung), trong hình khối gì (tab, dải chân trang, ô trắng…) thì bản Tabcom làm y như vậy, chỉ thay nội dung và màu.
   Không tự sáng tác vị trí mới, không ép dùng chân trang Tabcom. Codex vẽ luôn trong lần render; chỉ khi vẽ sai logo/số thì sửa bằng code.
2. **Không màu neon** (xanh lá chói, hồng/tím phát sáng, cyan chói…). `#5CE244` Up green ngừng dùng. Không glow, không viền phát sáng.
3. **Không hiệu ứng 3D Floating Card** (thẻ UI/màn hình nổi nghiêng có bóng đổ kiểu 3D lơ lửng). Thẻ thông tin nếu có thì phẳng.
4. **Màn hình sàn TMĐT / trang bán hàng chỉ là giao diện Shopee hoặc TikTok Shop** (theo chủ đề bài). Không Amazon,
   Lazada, Shopify, app nước ngoài hay giao diện bịa.
5. **Xoá sạch thông tin riêng của mẫu gốc**: logo, tên thương hiệu, SĐT, email, website, địa chỉ, mã QR, handle mạng xã hội.
6. **Nhân vật luôn là người Việt / châu Á — mô tả cụ thể ngay trong prompt**, không chỉ ghi "Vietnamese" (Codex sẽ bám
   người mẫu trong ảnh gốc): gương mặt Việt / Đông Á (mặt trái xoan mềm, mắt một mí hoặc hai mí nhẹ, sống mũi thấp nhỏ),
   da sáng tông ấm, tóc đen thẳng; kèm câu cấm "must NOT look South Asian, Indian, Middle Eastern or Western".
7. **Mẫu tham khảo chỉ lấy banner nước ngoài, do người thật thiết kế**; không học, không copy poster/banner của Việt Nam;
   **không dùng ảnh do AI tạo làm mẫu** — agent đưa 3–5 mẫu, người dùng tự chọn.
8. **Không copy-paste mẫu**: giữ bố cục, nhịp, ý tưởng của mẫu nhưng phải biến tấu thật — nhân vật mới (gương mặt, kiểu tóc,
   trang phục khác), thay ít nhất 2 đạo cụ/item cho hợp nội dung bài, bối cảnh/hình minh hoạ theo thông điệp mới.
   Chỉ đổi màu là **không đạt**.
8b. **Không phóng đại mẫu**: mẫu người dùng chọn đã hoàn hảo, không rối. Bản Tabcom giữ **số lượng và cường độ** của từng
   phần tử ≤ mẫu (số vật, cỡ, độ mờ, độ rực, mật độ số liệu trên màn hình) và **giữ đúng số màu nhấn** của mẫu — không để màu
   thương hiệu (cam…) rải thêm thành điểm nhấn mới.
8c. **Dấu vân tay (tránh bị coi là copy)**: liệt kê các chi tiết nhận ra được của mẫu (dáng người, khối nổi, phông, hướng
   bố cục, nhãn/dấu nhấn…), đổi **3** chi tiết theo kiểu **1-đổi-1** (cùng số lượng, diện tích, độ sáng, vai trò). Đổi chứ không
   thêm; không đụng các trần đo được (khoảng trống, phân cấp độ sáng, số màu nhấn). **Logo/SĐT/domain không nằm trong 3 chi tiết
   này** (theo 1b). Muốn đổi hướng bố cục thì viết thẳng bố cục đã lật vào prompt.
8d. **Không đính kèm ảnh mẫu khi render** (người dùng chốt 03/11/2026): ảnh mẫu chỉ để phân tích; Codex chỉ nhận prompt tự đủ
   + logo. Đính kèm mẫu thì ảnh ra giống ~95% bản gốc.
9. Quy tắc thiết kế (mục 10) luôn đưa vào prompt để ảnh không rối, kể cả khi bám mẫu.
10. **Mỗi ấn phẩm chỉ render 1 lần** (người dùng chốt 02/11/2026). Mọi khâu soát (kiểm đếm, chống rối, nhân vật, vị trí logo/liên
   hệ, số liệu không tự mâu thuẫn) làm **trên prompt, trước khi render**. Sau render chỉ soát để báo cáo; lỗi nhỏ trên nền trơn sửa
   bằng code; không render lại trừ khi người dùng yêu cầu.

---

## 1. Canvas

- Khổ chuẩn **vuông 1:1, 1080×1080 px** (file gốc 940,5 pt). Mọi số đo dưới đây quy ra px ở khổ 1080.
- Vùng an toàn: **không đặt nội dung ở y ≤ 84** (logo tab) và **y ≥ 996** (chân trang). Lề trái/phải ~48 px.

## 2. Logo

- File gốc: `../assets/logos/tabcom-white-green-transparent.png` (880×192, nền trong suốt).
- Cấu tạo: chữ **"T bcom" màu trắng** bo tròn + biểu tượng **chữ "α" gradient xanh bạc hà**
  (`#07EDAD` → `#75DAD1`) thay cho chữ "a".
- Logo **luôn trắng** và **luôn nằm trong tab gradient** ở giữa mép trên. Không đặt logo trần lên nền,
  không đổi màu chữ, không kéo méo.

### Tab logo (cố định trên 100% thiết kế)
- Hình thang úp, cạnh trên chạm mép ảnh, hai cạnh xiên thu vào, **hai góc dưới bo tròn**.
- Gradient ngang **`#005FB2` (trái) → `#00A7A1` (phải)**.
- Kích thước: rộng ~500 px ở mép trên (x 296–797), cao **72 px**, căn giữa ngang.
- Logo trong tab: rộng ~171 px, cao ~37 px, y 15–52, căn giữa.
- Mẫu cắt sẵn: `components/top-logo-tab_light-bg.png`, `components/top-logo-tab_dark-bg.png`.

## 3. Chân trang (cố định trên 100% thiết kế)

Hai thông tin, một trái một phải, cùng hàng, tâm dọc ~y 1020:

| Vị trí | Icon | Chữ |
|---|---|---|
| Trái, chữ bắt đầu x ≈ 96 | Điện thoại | `0786.668.222` |
| Phải, chữ kết thúc x ≈ 1036 | Quả địa cầu | `tabcomgroup.vn` |

- Font **Inter Bold, ~34 px**.
- **Biến thể nền tối / dải xanh đáy** (phổ biến nhất): chữ trắng; icon trắng trong **hình tròn xanh `#00C39C`**
  (Ø ~39 px); đáy ảnh là dải xanh royal `#003AB0`. → `components/footer_dark-band.png`
- **Biến thể nền sáng**: chữ **gradient thương hiệu xanh dương → teal**; icon dạng nét màu navy, không có
  hình tròn. → `components/footer_light-bg.png`, `components/footer_light-bg-blue-text.png`

## 4. Bộ màu

### Gradient thương hiệu (màu chủ đạo — nhận diện số 1)
**`#0048B6` → `#0082A8` → `#00BE9D`** (xanh dương → xanh lơ → teal), luôn chạy **trái → phải**.
Dùng cho: chữ tiêu đề trên nền sáng, thanh highlight, chữ chân trang nền sáng.

| Nhóm | Tên | HEX | Dùng cho |
|---|---|---|---|
| Thương hiệu | Blue | `#0048B6` | Đầu gradient |
| | Mid | `#0082A8` | Giữa gradient |
| | Teal | `#00BE9D` | Cuối gradient |
| | Heading blue | `#1173C8` | Dòng tiêu đề phụ chữ đặc (vd "ĐỪNG VỘI BƠM ADS!") |
| Nền xanh | Royal | `#003AB0` | Dải đáy, nền xanh đậm |
| | Deep | `#03368C` | Nền xanh tối |
| | Navy | `#05173D` | Nền rất tối (bài ảnh thật, case study) |
| | Sky | `#2194FC` | Vùng sáng của nền royal (góc trên, vệt sáng) |
| Nền sáng | Paper | `#FCFDFF` | Nền trắng xanh |
| | Ice | `#E7F1FE` | Nền xanh nhạt |
| | Mist | `#D0E5FE` | Vùng đậm hơn của nền sáng |
| Nhấn | Orange | `#F27335` | Từ khoá Shopee, nhấn cam |
| | Red-orange | `#E45A2A` | Số liệu ấn tượng trên nền tối ("X100 LẦN") |
| | Shopee red | `#E94723` | Chữ "SHOPEE"/"TIKTOK SHOP" khi nhấn mạnh |
| | Icon green | `#00C39C` | Hình tròn icon chân trang |
| | ~~Up green~~ | ~~`#5CE244`~~ | **Ngừng dùng (neon, mục 0).** Số tăng trưởng dùng teal đậm `#007F73` |
| Chữ | Body | `#1E1E1E` | Chữ thường trong pill/nền sáng |
| | Navy text | `#001F54` | Chữ đậm trên nền sáng |
| | White | `#FFFFFF` | Chữ trên nền tối/thanh gradient |

Tỉ lệ ước tính: ~60% họ xanh dương, ~25% trắng/xanh nhạt, ~10% teal, ~5% cam/đỏ nhấn.
**Không dùng** tím, hồng, vàng làm màu chính; cam/đỏ chỉ để nhấn từ khoá, không làm nền.

## 5. Typography

| Vai trò | Font | Cỡ (px @1080) | Kiểu |
|---|---|---|---|
| Tiêu đề chính | **Inter Black / ExtraBold** (thay thế: Montserrat ExtraBold, Mulish Black) | 57–88 | IN HOA, căn giữa (hoặc trái khi có người bên phải) |
| Chữ trong thanh highlight | Inter ExtraBold / Mulish Black | 33–47 | IN HOA, trắng |
| Câu dẫn trong pill | Asap Italic / Bold Italic (thay thế: Mulish Italic) | 26–30 | Thường, nghiêng; từ khoá in đậm và tô màu |
| Chân trang | Inter Bold | 34 | — |
| Số liệu, bảng | Inter Bold / Montserrat Bold | 18–24 | — |

Inter và Mulish tải miễn phí ở Google Fonts; Asap và Montserrat thì dùng font thay thế ở bảng trên.

## 6. Thành phần tiêu đề (chọn 1–3, ghép theo thứ tự)

1. **Tiêu đề gradient** — chữ IN HOA tô gradient thương hiệu, 1–2 dòng, trên nền sáng.
   Dòng 2 có thể là chữ đặc `#1173C8`. → `components/heading_gradient-text_pill-subtitle_p1.png`
2. **Thanh highlight** — hình chữ nhật gradient `#0058B2 → #00BE9C`, chữ trắng IN HOA, nằm ngay dưới
   tiêu đề, rộng vừa chữ. Dùng được trên cả nền sáng lẫn tối. → `components/heading_with-highlight-bar_p5.png`
3. **Pill câu dẫn** — khung bo tròn hoàn toàn, nền trắng, viền xanh mảnh, chữ nghiêng `#1E1E1E` 1–2 dòng.
   Chỉ dùng trên nền sáng. → `components/heading_gradient_bar_pill_p9.png`
4. **Nền tối**: tiêu đề chữ trắng IN HOA; con số/từ "giật" tô cam đỏ `#E45A2A`; thanh highlight dùng
   như cũ. → `components/heading_dark-bg_orange-accent_p37.png`
5. Dòng nhãn nhỏ phía trên tiêu đề (vd "TRAFFIC NGOẠI SÀN"): chữ đen/navy, IN HOA, cỡ nhỏ.

## 7. Nền (4 họ)

| Họ | Mô tả | Mẫu |
|---|---|---|
| **Sáng 3D** | Trắng → xanh nhạt, sóng/lụa xanh dương ở nửa dưới, vệt sáng teal | p1, p5, p9, p14 |
| **Studio sáng** | Phòng trắng-xanh nhạt, ghế/sàn mềm, người ngồi | p45–p49 |
| **Royal blue** | Gradient xanh royal `#003AB0`→sky `#2194FC`, lưới kẻ mờ, góc trên sáng | p15–p28, p40–p44 |
| **Navy/ảnh thật** | Nền rất tối `#05173D` hoặc ảnh chụp thật phủ tối, chữ trắng | p29–p32, p36 |

## 8. Hình ảnh & đồ hoạ

- **Người đại diện**: người Việt trẻ (chủ yếu nữ, 20–30 tuổi), biểu cảm rõ (chỉ tay, bất ngờ, suy nghĩ,
  khoanh tay), mặc **áo polo xanh dương có logo Tabcom** hoặc áo thun xanh lá. Cắt nền, đặt giữa/phải khung.
- **Icon/đồ vật**: túi Shopee cam, túi TikTok đen, giỏ hàng, hộp carton, sản phẩm thật theo ngành hàng của bài.
  Dùng tiết kiệm, có bóng mềm tự nhiên. (Bản cũ có "icon 3D bóng, glow" — đã bỏ theo mục 0.)
- **Ảnh chụp màn hình thật** (dashboard Shopee/TikTok Shop, số liệu) đặt trong khung điện thoại/laptop/
  màn hình, có thể khoanh đỏ số liệu quan trọng. Màn hình đặt phẳng/thẳng hoặc trong thiết bị thật, không thẻ nổi 3D.
- Hiệu ứng: ánh sáng mềm tự nhiên. **Không glow, không neon, không thẻ nổi 3D** (mục 0).

## 9. Không được làm

- Đổi số điện thoại/website; đặt logo/liên hệ khác chỗ và khác kiểu mẫu đã đặt (mục 0.1b).
- Dùng màu ngoài bảng ở mục 4 làm màu chủ đạo; đảo gradient (teal → xanh dương).
- Font có chân (serif) hoặc font viết tay làm tiêu đề chính (ngoại lệ: chữ ký nhỏ kiểu "Day 01").
- Nhồi quá 3 tầng tiêu đề; chữ đè lên mặt người.

## 10. Nguyên tắc thiết kế cơ bản (áp cho mọi bài)

Rút từ đọc đủ 79 trang tài liệu "Graphic design and layout concepts" (UNDP/UN-REDD, Mairi Feeger, 2016),
gồm cả 2 poster tham chiếu p13 (yếu tố) và p30 (nguyên tắc). Cột "Kiểm bằng số" là phép đo agent phải chạy
trên ảnh đã render (đo pixel, không đoán bằng mắt).

### 10.1 Mục đích trước, đẹp sau (p6, p10, p56)
Thiết kế = "nghệ thuật có mục đích". Trước khi viết prompt, trả lời: thông điệp một câu là gì? Hình và chữ có
cùng kể câu đó không? (p5: "visual communication is part of the message"; p56 bước 6: "các yếu tố có phục vụ
thông điệp không?"). Người xem chỉ có ~50 ms ấn tượng đầu (p4) → một ý duy nhất.

### 10.2 Bảy nguyên tắc (p11, p30, p42–45)

| Nguyên tắc | Ý trong tài liệu | Áp vào bài Tabcom | Kiểm bằng số |
|---|---|---|---|
| **Phân cấp** | Cỡ chữ là cách phổ biến nhất (p43); poster tốt có 1 thứ áp đảo (p44) | Tiêu đề là khối lớn nhất. Logo nhỏ, yên (≤ ~20% chiều rộng). Liên hệ là chữ nhỏ nhất | Chiều cao chữ: tiêu đề > số liệu chính > thân bài ≥ nút > liên hệ. Logo rộng ≤ 220 px |
| **Căn lề** | "Mọi phần tử nối thị giác với một phần tử khác; không gì lạc chỗ" (p30) | Một mép trái chung cho logo, tiêu đề, thân bài, nút, liên hệ | Lệch mép trái giữa các khối ≤ 8 px |
| **Tương phản** | 4 cách: màu, sắc độ (value), kích thước/hình, hướng (p30) | Chữ đậm/nhạt, to/nhỏ rõ rệt; nền sáng trơn để chữ nổi | Chữ thường ≥ 4,5:1, chữ lớn ≥ 3:1 (WCAG). Teal sáng `#00BE9D` chỉ 2,3:1 trên nền sáng → **không dùng làm màu chữ**; chữ teal dùng `#007F73` (4,6:1) |
| **Cân bằng** | Cân bằng bất đối xứng: khối hình đối trọng khối chữ (p45) | Cột chữ trái ↔ người + thẻ phải | Không có góc nào chứa > 40% "khối nặng" |
| **Gần nhau** | Liên quan thì gần, không liên quan thì xa; giảm rối (p30) | Thân bài sát nút; số liệu sát người; liên hệ thành 1 cụm | Trong nhóm 24 px, giữa nhóm ≥ 48 px. Thứ không liên quan (tay người mẫu vs chữ) cách ≥ 48 px |
| **Lặp lại** | Đặt style cho mỗi loại phần tử rồi dùng lại (p30) | Một họ font (Inter), một kiểu bo góc (24 px), một kiểu bóng | Đếm họ font = 1, kiểu bo góc = 1 |
| **Chức năng** | Thiết kế để giải quyết vấn đề (p10–11) | Có lời kêu gọi hành động rõ (nút) + liên hệ | Có đúng 1 CTA |

### 10.3 Bố cục (p32–38)
- **Lưới**: chọn 1 lưới và theo nó (p32–34). Bài vuông Tabcom: lề 80 px đều 4 phía, khung nội dung x/y 80–1000.
- **Tỉ lệ vàng** (p37–38, 1 : 1,618): chia dọc vùng đầu ~38% (logo + tiêu đề) / vùng nội dung ~62%; vùng nội dung
  chia cột chữ ~38% / cột hình ~62%. Mẫu "Header – Content 1 (367) – Content 2 (593) – Footer" ở p38.
- **Một phần ba** (p35): mặt người / điểm nhấn hình đặt gần giao điểm các đường 360/720.
- **Khoảng trống** (p13, p26–28, p69): để mắt nghỉ, làm nổi thứ quan trọng. Vùng cạnh tiêu đề để trống.

| Kiểm bằng số | Ngưỡng |
|---|---|
| Chữ, thẻ thông tin nằm trong khung | x 64–1016, y 64–1016 |
| Người, đồ vật | Theo mẫu: **vật ở góc / cẳng tay được tràn mép nếu mẫu tràn mép ở đúng chỗ đó** (cách mẫu tạo chiều sâu). Mẫu không tràn thì giữ trọn trong khung, không cắt giày/đồ vật |
| Chênh lề trái–phải, trên–dưới | ≤ 20 px |

### 10.4 Yếu tố thị giác (p13–24)
- **Đường/hướng** (p15): chéo đi lên = lạc quan, thành công; chéo đi xuống = suy giảm. Dãy thẻ/biểu đồ tăng trưởng
  phải xếp **đi lên sang phải**.
- **Màu** (p13, p16–20, p66): ấm (cam, đỏ) = chủ động, gây chú ý; lạnh (xanh) = bình tĩnh, tin cậy. **≤ 5 màu**, dùng màu
  tiết kiệm để làm nổi thông tin quan trọng. Tabcom: navy `#0B1F4F`, royal `#0048B6`, teal (đậm cho chữ / sáng cho chi tiết),
  nền sáng; cam Shopee + đen TikTok chỉ trong icon nhỏ.
- **Hình** (p22–24): hình lạ/khác thường hút mắt → chỉ dùng cho điểm cần nhấn.
- **Kích thước/sắc độ** (p13): dùng để định mức quan trọng và dẫn mắt.

### 10.5 Chữ (p39–41, p67)
- Font phải đọc được và hợp giọng: sans sạch = "clean, cool, collected" (p40) → hợp Tabcom (dịch vụ, số liệu).
- Bài đăng xem trên điện thoại (1080 → ~360 px): **chữ nhỏ nhất ≥ 24 px** ở khổ 1080.
- Không ngắt dòng giữa tên riêng ("TikTok / Shop"); ghi sẵn ngắt dòng trong prompt.
- Chữ luôn nằm ngang; không xoay, không nghiêng, không dùng nhiều font (ví dụ xấu p77–79).

### 10.6 Điểm chốt (p66–75)
Callout dùng tiết kiệm (≤ 2 thẻ nổi) · Minh hoạ chỉ khi giúp hiểu · Icon đơn giản, phổ quát · Dữ liệu gộp: 1 số chính
+ 1 xu hướng, không rải nhiều số lẻ · Tỉ lệ biểu đồ đúng, không bóp méo · Bỏ 3D chart, hoa văn, đạo cụ thừa ·
"Hoàn hảo là khi không còn gì để bỏ" (p75).

### 10.7 Ví dụ xấu cần tránh (p77–79)
Nhiều font lẫn lộn, nhiều màu chọi nhau, mảng màu và chữ xếp xiên chồng chéo, kín chữ không chỗ thở.

## 11. Quy trình chuẩn tạo ảnh bằng Codex (bắt buộc)

**Phân vai:** agent (Claude) đọc file này + ảnh mẫu → **tự viết prompt đầy đủ** → Codex **chỉ tạo ảnh**.
Không bảo Codex đọc guideline hay file nào khác. Đã đo: cách này rẻ hơn ~30–50% token và ra ảnh sát ý hơn
(bản v3 ~14k token so với ~28k khi để Codex tự đọc guideline).

1. **Phân tích mẫu bằng 8 agent `tabcom-ref-analyst` chạy song song** (phân cấp, xếp lớp & chiều sâu, căn gióng, xa gần,
   khoảng trống, chữ, màu, hình & đường & kiểm đếm), rồi tổng hợp thành `phan-tich-mau-goc.md`: bảng kiểm đếm số lượng +
   cường độ từng phần tử (trần cho prompt) và bảng "mẫu gốc → Tabcom". Chi tiết: skill `tabcom-social-image-cu` mục A3.
2. Agent soát bố cục theo mục 10 (phân cấp, căn lề, lưới, ≤5 màu, bỏ đạo cụ thừa, 1 callout).
2b. **Phác thảo whiteboard → người dùng duyệt (bắt buộc, chưa duyệt thì chưa làm ảnh thật).**
   - Agent viết **design brief** ngắn: thông điệp 1 câu · lưới và vùng (lề, tỉ lệ vàng) · danh sách phần tử theo thứ tự đọc ·
     toàn bộ chữ (đúng từng chữ, đúng ngắt dòng) · màu dự kiến cho từng phần tử · hình người/đạo cụ.
   - **Vẽ bằng code, KHÔNG gọi Codex/AI tạo ảnh** (tốn token vô ích). Viết brief thành JSON rồi chạy:
     `python -I "wireframe/render_wireframe.py" brief.json wireframe.png` → phác thảo đen–trắng kiểu bảng trắng
     (nét run tay): khung lề, đường chia lưới nét đứt, hộp ghi nhãn kèm nội dung chữ thật, người vẽ que + ghế lười,
     thẻ bo góc, số thứ tự đọc, mũi tên, khung "để trống", bảng ghi chú brief bên phải (thông điệp, thứ tự đọc, màu, font, luật).
     Mẫu: `wireframe/example-v7-brief.json` → `wireframe/example-v7-wireframe.png`.
     Toạ độ trong JSON là pixel trên canvas 1080 — chính là bố cục sẽ đo lại sau khi render ảnh thật.
   - Gửi người dùng ảnh phác + brief. Người dùng duyệt hoặc sửa (đổi chữ, dời khối, bỏ/thêm phần tử) → agent sửa brief,
     phác lại nếu thay đổi lớn. Chỉ khi được duyệt mới sang bước 3.
   - Prompt ảnh thật ở bước 3 phải viết **từ brief đã duyệt**, không tự thêm phần tử mới.
3. Agent viết prompt **tự đủ**, gồm:
   - Dòng mở: *"Generate ONE image with your image generation tool. Do not read any files, do not run any shell commands, do not write code. Just call image generation once with the brief below, then reply "done"."*
   - Khổ, phong cách; khối DESIGN PRINCIPLES; danh sách ELEMENTS (chỉ những thứ được phép có); BACKGROUND;
     TEXT với chữ tiếng Việt chính xác từng dấu; FIXED BRAND ELEMENTS ghi rõ mã màu, vị trí, tỉ lệ; DON'T.
   - Ghi rõ "rectangular highlight bar with square 90-degree corners — not slanted, not rounded" (Codex hay vẽ lệch).
4. Gọi Codex, **chỉ đính kèm logo** (trắng `../assets/logos/tabcom-white-green-transparent.png` hoặc navy
   `../assets/logos/tabcom-navy-green-transparent.png`) — **không kèm ảnh mẫu** (mục 0.8d):
   `codex exec --skip-git-repo-check -s read-only -i <logo> - < prompt.md`
5. Lấy ảnh mới nhất trong `~/.codex/generated_images/<session-id>/`, resize về 1080×1080.
6. Agent tự soát ảnh theo checklist mục 12 **và chạy các phép đo ở mục 10** (mép trái, khung lề, tương phản), soát thêm
   "có chỗ nào phóng đại so với mẫu không" (mục 0.8b). **Chỉ render 1 lần** (mục 0.10): soát kỹ prompt trước khi render;
   sau render lỗi nhỏ trên nền trơn sửa bằng code, còn lại ghi vào báo cáo cho người dùng quyết.

**Kinh nghiệm viết prompt (đã thử v4→v7):**
- Model ảnh **không theo toạ độ pixel** (v6 ghi "right edge at x=1000" vẫn tràn ra mép). Dùng ngôn ngữ khung hình thay vào:
  *"camera ZOOMED OUT; the man and beanbag are SMALL in the frame (~45% width), empty background visible on their right and below"*,
  *"the area to the RIGHT of the headline must stay completely EMPTY"*, *"card BELOW the headline, never beside it"*.
- Ghi sẵn từng dòng chữ và chỗ ngắt dòng; ghi "only the texts quoted above".
- Nêu màu chữ đủ tương phản (navy, royal, teal đậm `#007F73`), đừng để model tự chọn teal sáng cho chữ.
- Prompt tự đủ cho bài nền sáng chỉ cần đính 1 ảnh: logo navy `../assets/logos/tabcom-navy-green-transparent.png`. (~6–16k token/lần).

Không dùng Flux (Cloudflare) để ra thẳng bài có chữ: đã thử, sai dấu tiếng Việt, lặp số điện thoại ở chân trang,
chữ trên màn hình vô nghĩa. Flux chỉ dùng cho ảnh nền/minh hoạ không chữ.

## 12. Checklist khi chuyển một thiết kế mẫu sang Tabcom

- [ ] Khổ 1080×1080; nội dung nằm trong y 84–996.
- [ ] Logo, `0786.668.222`, `tabcomgroup.vn` đúng chỗ, đúng cỡ (% khung) và đúng hình khối như mẫu đặt thông tin thương hiệu (mục 0.1b).
- [ ] Màu chủ đạo thay hết sang họ xanh dương/teal; nhấn cam/đỏ chỉ cho từ khoá.
- [ ] Tiêu đề IN HOA font sans đậm, có ít nhất một thành phần thương hiệu: chữ gradient **hoặc** thanh highlight.
- [ ] Nền thuộc một trong 4 họ ở mục 7.
- [ ] Hình người/icon theo mục 8; không giữ lại logo, màu, font của thương hiệu gốc trong mẫu.
- [ ] Đạt mục 10: một thứ to nhất, các khối chữ thẳng một mép, ≤5 màu, không đạo cụ thừa, tối đa 1 callout.
- [ ] Tiếng Việt đúng từng dấu; người mẫu là người Việt.
